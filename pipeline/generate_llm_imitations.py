"""Generate LLM imitations of Nigerian authors via OpenRouter.

Generates 16 passages: 2 free models x 2 authors x 4 samples each.
Each model gets a system prompt that primes the imitation with the
target author's style, then a per-passage prompt with a topic seed.

Output: corpus/synthetic/<model>__<author>__<sample>.txt
"""

import json
import os
import random
import ssl
import time
import urllib.request
from pathlib import Path

# ---- Configuration ----

CORPUS_ROOT = Path(__file__).resolve().parent.parent / "corpus"
LLM_OUT = CORPUS_ROOT / "synthetic"
LLM_OUT.mkdir(parents=True, exist_ok=True)

# 2 free models from OpenRouter
MODELS = [
    ("openrouter", "nex-agi/nex-n2.5-mini", "https://openrouter.ai/api/v1/chat/completions"),
    ("openrouter", "nex-agi/nex-n2.5-pro", "https://openrouter.ai/api/v1/chat/completions"),
]

# Per-author style notes. Kept neutral — describe what to imitate, not who.
AUTHOR_STYLES = {
    "egya": (
        "Contemporary Nigerian poet. Stylistic markers: nature imagery interwoven "
        "with postcolonial memory, elegiac tone, irregular line lengths, occasional "
        "Igbo words, long sentences with embedded subordinate clauses. Cultural "
        "reference points: Nigerian landscape, civil war memory, ancestral invocation, "
        "the river as metaphor."
    ),
    "shittu": (
        "Contemporary Nigerian poet and literary scholar. Stylistic markers: structured "
        "argumentative prose, careful sentence rhythm, mix of Nigerian and Western "
        "literary allusions, paragraph-length paragraphs with clear topic sentences, "
        "occasional critical-theoretical vocabulary (discourse, narrative, representation)."
    ),
}

AUTHORS = ["egya", "shittu"]
SAMPLES_PER_AUTHOR_MODEL = 4  # 2 models × 2 authors × 4 = 16 total
TARGET_WORDS = 250


def _load_env():
    """Load API keys from a known .env file. Falls back to os.environ."""
    candidates = [
        Path(__file__).resolve().parent.parent.parent.parent / "AppData" / "Local" / "hermes" / ".env",
        Path.home() / ".env",
        Path(__file__).resolve().parent.parent / ".env",
    ]
    for env_path in candidates:
        if not env_path.exists():
            continue
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            os.environ.setdefault(k, v.strip().strip('"').strip("'"))


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
    style = AUTHOR_STYLES[author]
    exemplar = EGYA_EXEMPLAR if author == "egya" else SHITTU_EXEMPLAR
    return f"""You are a fiction-writing assistant producing imitation passages \
that match a target author's style for academic forensic research.

Target author style:
{style}

Sample passage in the target style:
\"\"\"{exemplar}\"\"\"

Produce a passage that:
- Sounds like the target author
- Is roughly {TARGET_WORDS} words long
- Is on a general literary or cultural topic
- Avoids direct reference to real living people by name
- Does not include preamble, titles, or explanation — just the passage itself

You are helping build a forensic stylometry dataset; the imitation is for \
comparing machine vs human writing patterns, not for distribution."""


def build_user_prompt(author: str, sample_idx: int) -> str:
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


# ---- API call ----

def call_openrouter(model: str, system: str, user: str, timeout: int = 90) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY", "") or os.environ.get("OPENROUTER_KEY", "")
    if not api_key:
        raise RuntimeError("OpenRouter API key missing")
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "max_tokens": 700,
        "temperature": 0.01,
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


def generate(model_name: str, author: str, sample_idx: int) -> str:
    """Generate one passage; retry once on transient failure."""
    system = build_system_prompt(author)
    user = build_user_prompt(author, sample_idx)
    last_err = None
    for attempt in (1, 2):
        try:
            return call_openrouter(model_name, system, user)
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
    for _provider, model_name, _ in MODELS:
        for author in AUTHORS:
            for i in range(SAMPLES_PER_AUTHOR_MODEL):
                done += 1
                out_path = LLM_OUT / f"{model_name.split('/')[-1]}__{author}__{i:02d}.txt"
                if out_path.exists() and out_path.stat().st_size > 100:
                    print(f"[{done}/{total}] skip (exists): {out_path.name}")
                    continue
                print(f"[{done}/{total}] {model_name} -> {author}/{i:02d}")
                try:
                    text = generate(model_name, author, i)
                    out_path.write_text(text.strip(), encoding="utf-8")
                    log.append({"model": model_name, "author": author,
                                "sample": i, "ok": True, "chars": len(text.strip())})
                except Exception as e:
                    print(f"  ERROR: {e}")
                    log.append({"model": model_name, "author": author,
                                "sample": i, "ok": False, "error": str(e)})
                time.sleep(1.0)
    (LLM_OUT / "_generation_log.json").write_text(json.dumps(log, indent=2))
    print(f"\nDone. {sum(1 for x in log if x['ok'])} / {len(log)} successful.")


if __name__ == "__main__":
    main()
