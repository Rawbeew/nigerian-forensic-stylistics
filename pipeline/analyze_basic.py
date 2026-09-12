"""Basic stylometric analysis: human vs LLM imitations.

Computes a small set of stylistic features for both human and LLM-generated
text, then reports distributions and a basic per-author classifier.

Features (kept deliberately small for the v9-minimal preprint):
- Mean sentence length (chars)
- Type-token ratio (TTR) over words
- Mean word length (chars)
- Punctuation density (per word)
- Function-word ratio (from a small stopword list)
- Average syllable estimate per word (vowel-group count)

The output is a CSV with one row per passage + a summary JSON.
"""

import csv
import json
import re
import statistics
from collections import Counter
from pathlib import Path


CORPUS_ROOT = Path(__file__).resolve().parent.parent / "corpus"
LLM_OUT = CORPUS_ROOT / "synthetic"


# Tiny English function-word list. Stopwords only - no need for accuracy here.
FUNCTION_WORDS = set("""
a an the and or but if then else when while of in on at to from for with without about as by
is are was were be been being have has had do does did will would shall should may might can could
i you he she it we they me him her us them my your his its our their this that these those
not no nor so very much more most
""".split())


def tokenize_words(text: str) -> list:
    """Split text into word tokens, lowercased."""
    return re.findall(r"\b[a-zA-Z']+\b", text.lower())


def split_sentences(text: str) -> list:
    """Rough sentence split on . ! ? followed by whitespace + capital."""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]


def count_syllables(word: str) -> int:
    """Very rough syllable estimate: count vowel groups."""
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prev_vowel = False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    return max(1, count)


def punctuation_density(text: str, words: list) -> float:
    """Count of .,;:!?()[]{}\"' per word."""
    punct_chars = set(".,;:!?()[]{}\"'")
    pcount = sum(1 for c in text if c in punct_chars)
    return pcount / max(1, len(words))


def ttr(words: list) -> float:
    """Type-token ratio: unique / total."""
    return len(set(words)) / max(1, len(words))


def mean_word_length(words: list) -> float:
    return statistics.mean(len(w) for w in words) if words else 0.0


def function_word_ratio(words: list) -> float:
    fw = sum(1 for w in words if w in FUNCTION_WORDS)
    return fw / max(1, len(words))


def mean_syllables_per_word(words: list) -> float:
    if not words:
        return 0.0
    return statistics.mean(count_syllables(w) for w in words)


def mean_sentence_length_chars(text: str) -> float:
    sents = split_sentences(text)
    return statistics.mean(len(s) for s in sents) if sents else 0.0


def sentence_length_std(text: str) -> float:
    sents = split_sentences(text)
    if len(sents) < 2:
        return 0.0
    return statistics.pstdev(len(s) for s in sents)


def extract_features(text: str) -> dict:
    words = tokenize_words(text)
    return {
        "n_words": len(words),
        "n_sents": len(split_sentences(text)),
        "mean_sentence_len_chars": round(mean_sentence_length_chars(text), 2),
        "sent_len_std": round(sentence_length_std(text), 2),
        "ttr": round(ttr(words), 4),
        "mean_word_len": round(mean_word_length(words), 3),
        "punct_density_per_word": round(punctuation_density(text, words), 4),
        "function_word_ratio": round(function_word_ratio(words), 4),
        "mean_syllables_per_word": round(mean_syllables_per_word(words), 3),
    }


def gather_corpus() -> list:
    """Return list of dicts with author, source, text, features."""
    rows = []
    # Human corpus
    for f in sorted((CORPUS_ROOT).glob("*.txt")):
        text = f.read_text(encoding='utf-8', errors='replace').strip()
        if not text:
            continue
        # Author from filename prefix
        if f.stem.startswith('egya'):
            author = 'egya'
        elif f.stem.startswith('shittu'):
            author = 'shittu'
        else:
            continue
        rows.append({
            "author": author,
            "source": "human",
            "id": f.stem,
            "text": text,
            "features": extract_features(text),
        })

    # LLM corpus
    llm_dir = CORPUS_ROOT / "synthetic"
    if llm_dir.exists():
        for f in sorted(llm_dir.glob("*.txt")):
            if f.name.startswith('_'):
                continue
            text = f.read_text(encoding='utf-8', errors='replace').strip()
            if len(text) < 100:
                continue
            parts = f.stem.split('__')
            if len(parts) < 3:
                continue
            author = parts[1]
            rows.append({
                "author": author,
                "source": "llm",
                "id": f.stem,
                "model": parts[0],
                "text": text,
                "features": extract_features(text),
            })
    return rows


def main():
    rows = gather_corpus()
    print(f"Loaded {len(rows)} passages ({sum(1 for r in rows if r['source']=='human')} human, {sum(1 for r in rows if r['source']=='llm')} LLM)")

    # Write per-passage CSV
    out_csv = CORPUS_ROOT.parent / "results_v9" / "passages.csv"
    out_csv.parent.mkdir(exist_ok=True)
    fieldnames = ["id", "author", "source", "model"] + list(rows[0]['features'].keys())
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            row = {"id": r["id"], "author": r["author"], "source": r["source"], "model": r.get("model", "")}
            row.update(r["features"])
            writer.writerow(row)
    print(f"Wrote {out_csv}")

    # Compute aggregate stats by (author, source)
    agg = {}
    for r in rows:
        key = (r['author'], r['source'])
        agg.setdefault(key, []).append(r['features'])

    summary = {}
    for key, features_list in agg.items():
        n = len(features_list)
        feature_names = list(features_list[0].keys())
        sums = {name: sum(f[name] for f in features_list) for name in feature_names}
        means = {name: round(sums[name] / n, 4) for name in feature_names}
        # Compute stdev for a few key features
        stdevs = {}
        for name in ['mean_sentence_len_chars', 'ttr', 'mean_word_len', 'function_word_ratio', 'mean_syllables_per_word']:
            vals = [f[name] for f in features_list]
            stdevs[name] = round(statistics.pstdev(vals), 4) if len(vals) > 1 else 0.0
        summary[f"{key[0]}_{key[1]}"] = {"n": n, "means": means, "stdevs": stdevs}

    out_summary = CORPUS_ROOT.parent / "results_v9" / "summary.json"
    out_summary.write_text(json.dumps(summary, indent=2))
    print(f"Wrote {out_summary}")

    # Print summary table
    print(f"\n{'Group':25} {'n':>3} {'sent_len':>10} {'ttr':>7} {'word_len':>9} {'fw_ratio':>9} {'syl/word':>9}")
    print("-" * 80)
    for key in sorted(summary.keys()):
        s = summary[key]
        m = s['means']
        print(f"{key:25} {s['n']:>3} {m['mean_sentence_len_chars']:>10.1f} {m['ttr']:>7.4f} {m['mean_word_len']:>9.3f} {m['function_word_ratio']:>9.4f} {m['mean_syllables_per_word']:>9.3f}")


if __name__ == "__main__":
    main()
