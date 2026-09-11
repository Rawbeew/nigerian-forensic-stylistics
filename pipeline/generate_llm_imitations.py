"""Generate LLM imitations of Nigerian authors via NVIDIA NIM and OpenRouter.

Generates ~80 passages across 4 free models x 2 authors x 10 samples each.
Each model gets a system prompt that primes the imitation with the target
author's style + a small exemplar, then a per-passage prompt.

Output: corpus/llm/<model>__<author>__<sample>.txt
"""

import json
import os
import random
import ssl
import time
import urllib.request
from pathlib import Path

# ---- Configuration ----

CORPUS_ROOT = Path("/home/rabiu/nigerian-forensic-stylistics/corpus")
LLM_OUT = CORPUS_ROOT / "llm"
LLM_OUT.mkdir(parents=True, exist_ok=True)

# 4 free models from 2 providers
MODELS = [
    ("nvidia", "meta/llama-3.2-90b-vision-instruct", "https://integrate.api.nvidia.com/v1/chat/completions"),
    ("nvidia", "google/gemma-4-31b-it", "https://integrate.api.nvidia.com/v1/chat/completions"),
    ("openrouter", "google/gemma-4-31b-it:free", "https://openrouter.ai/api/v1/chat/completions"),
    ("openrouter", "nvidia/nemotron-3-super-120b-a12b:free", "https://openrouter.ai/api/v1/chat/completions"),
]

# Per-author style notes. Kept neutral - describe what to imitate, not who.
AUTHOR_STYLES = {
    "egya": (
        "Contemporary Nigerian poet. Stylistic markers: nature imagery interwoven with "
        "postcolonial memory, elegiac tone, irregular line lengths, occasional Igbo words, "
        "long sentences with embedded subordinate clauses. Cultural reference points: "
        "Nigerian landscape, civil war memory, ancestral invocation, the river as metaphor."
    ),
    "shittu": (
        "Contemporary Nigerian poet and literary scholar. Stylistic markers: structured "
        "argumentative prose, careful sentence rhythm, mix of Nigerian and Western literary "
        "allusions, paragraph-length paragraphs with clear topic sentences, occasional "
        "critical-theoretical vocabulary (discourse, narrative, representation)."
    ),
}

# Authors to imitate and number of passages per author per model
AUTHORS = ["egya", "shittu"]
SAMPLES_PER_AUTHOR_MODEL = 10
TARGET_WORDS = 350  # rough length to match corpus passages

# ---- API keys from env ----
def _load_env():
    env_path = Path("/home/rabiu/.env")
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith(("NVIDIA_API_KEY=", "OPENROUTER_API_KEY=", "OPENROUTER_KEY=")):
                k, v = line.split("=", 1)
                os.environ[k] = v.strip().strip('"').strip("'")

_load_env()


# ---- Style exemplars ----

EGYA_EXEMPLAR = """In the river we buried what the river refused.
The season returns with its load of absence; the canoe waits,
patient as a wound. Memory, they said, is what the body keeps
when the house is gone."""

SHITTU_EXEMPLAR = """Toyin Shittu's engagement with the Nigerian literary scene has been
characterized by a sustained interrogation of the relationship between
discourse and representation. In his recent work, this concern is
articulated through a careful reading of the formal properties of
contemporary Nigerian poetry, particularly as these properties intersect
with broader debates about postcolonial identity and cultural memory."""


# ---- Prompt builders ----

def build_system_prompt(author: str) -> str:
    """Build the system prompt that primes the model to imitate."""
    style = AUTHOR_STYLES[author]
    exemplar = EGYA_EXEMPLAR if author == "egya" else SHITTU_EXEMPLAR
    return f"""You are a fiction-writing assistant tasked with producing imitation \
passages that match a target author's style for academic forensic research.

Target author style:
{style}

Sample passage in the target style:
\"\"\"{exemplar}\"\"\"

Produce a passage that:
- Sounds like the target author
- Is roughly {TARGET_WORDS} words long
- Is on a general literary or cultural topic
- Avoids direct reference to real living people by name
- Does not include preamble, titles, or explanation - just the passage itself

You are helping build a forensic stylometry dataset; the imitation is for \
comparing machine vs human writing patterns, not for distribution."""


def build_user_prompt(author: str, sample_idx: int) -> str:
    """Build a per-sample user prompt with a fresh topic seed."""
    # Different topic seeds so the 10 samples per (model, author) are varied.
    topics = [
        "the relationship between memory and landscape",
        "the tension between local tradition and global influence",
        "ritual, loss, and the marking of seasons",
        "the role of language in cultural identity",
        "the figure of the elder and the transmission of history",
        "movement, displacement, and the sense of home",
        "the meaning of craft and artistic labor",
        "the boundary between the natural and the political",
        "silence, witness, and what is left unsaid",
        "the river, the road, and the threshold",
    ]
    topic = topics[sample_idx % len(topics)]
    return (
        f"Write an original passage in the target style on the theme of {topic}. "
        "Aim for roughly one substantial paragraph or a short set of stanzas."
    )


# ---- API calls ----

def call_nvidia(model: str, system: str, user: str, timeout: int = 90) -> str:
    """Call NVIDIA NIM chat completions."""
    api_key = os.environ.get("NVIDIA_API_KEY", "")
    if not api_key:
        raise RuntimeError("NVIDIA_API_KEY missing")
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": 700,
        "temperature": 0.85,
    }
    req = urllib.request.Request(
        "https://integrate.api.nvidia.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def call_openrouter(model: str, system: str, user: str, timeout: int = 90) -> str:
    """Call OpenRouter chat completions."""
    api_key = os.environ.get("OPENROUTER_API_KEY", "") or os.environ.get("OPENROUTER_KEY", "")
    if not api_key:
        raise RuntimeError("OpenRouter API key missing")
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": 700,
        "temperature": 0.85,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    )
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        data = json.loads(r.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def generate(model_provider: str, model_name: str, author: str, sample_idx: int) -> str:
    """Generate one passage; retry once on transient failure."""
    system = build_system_prompt(author)
    user = build_user_prompt(author, sample_idx)
    fn = call_nvidia if model_provider == "nvidia" else call_openrouter
    last_err = None
    for attempt in (1, 2):
        try:
            return fn(model_name, system, user)
        except Exception as e:
            last_err = e
            print(f"  attempt {attempt} failed: {e}")
            time.sleep(2)
    raise RuntimeError(f"Both attempts failed: {last_err}")


# ---- Driver ----

def main():
    total = len(MODELS) * len(AUTHORS) * SAMPLES_PER_AUTHOR_MODEL
    done = 0
    log = []
    for provider, model_name, _ in MODELS:
        for author in AUTHORS:
            for i in range(SAMPLES_PER_AUTHOR_MODEL):
                done += 1
                out_path = LLM_OUT / f"{provider}__{model_name.split('/')[-1].replace(':', '_')}__{author}__{i:02d}.txt"
                if out_path.exists() and out_path.stat().st_size > 100:
                    print(f"[{done}/{total}] skip (exists): {out_path.name}")
                    continue
                print(f"[{done}/{total}] {provider}/{model_name} -> {author}/{i:02d}")
                try:
                    text = generate(provider, model_name, author, i)
                    out_path.write_text(text.strip(), encoding="utf-8")
                    log.append({"provider": provider, "model": model_name,
                                "author": author, "sample": i, "ok": True,
                                "chars": len(text.strip())})
                except Exception as e:
                    print(f"  ERROR: {e}")
                    log.append({"provider": provider, "model": model_name,
                                "author": author, "sample": i, "ok": False,
                                "error": str(e)})
                time.sleep(1.0)
    (LLM_OUT / "_generation_log.json").write_text(json.dumps(log, indent=2))
    print(f"\nDone. {sum(1 for x in log if x['ok'])} / {len(log)} successful.")


if __name__ == "__main__":
    main()
