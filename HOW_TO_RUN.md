# How to run the Nigerian Forensic Stylistics pipeline

This repository contains the analysis pipeline for the paper *Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets*.

## What this pipeline does

For each human-authored passage in `corpus/*.txt` and each LLM-generated passage in `corpus/llm/*.txt`, the pipeline extracts nine lightweight stylometric features and aggregates them per author and condition. The headline results are in `paper.md` Section 6.

## Quick start (15 minutes)

### Step 1: Clone or download

```bash
git clone https://github.com/Rawbeew/nigerian-forensic-stylistics
cd nigerian-forensic-stylistics
```

### Step 2: Install dependencies

```bash
pip install numpy pandas
```

That is the entire dependency list. Feature extraction (`pipeline/analyze_basic.py`) is pure stdlib + numpy + pandas. The notebook (`pipeline/stylometric_pipeline.ipynb`) additionally uses `urllib.request` for OpenRouter API calls.

### Step 3: (Optional) Re-generate LLM imitations

This step is **only needed if you want to regenerate the LLM corpus** from scratch. The committed `corpus/llm/*.txt` files are the same passages referenced in `paper.md` Section 4.

1. Sign in at https://openrouter.ai and create a free-tier API key.
2. Set the environment variable:

   ```bash
   export OPENROUTER_API_KEY=sk-or-...
   ```

3. Run the generator:

   ```bash
   python pipeline/generate_llm_imitations.py
   ```

The script generates 16 passages (2 models × 2 authors × 4 samples each) and writes them to `corpus/llm/`.

### Step 4: Run feature extraction

```bash
python pipeline/analyze_basic.py
```

Reads `corpus/*.txt` (human) and `corpus/llm/*.txt` (LLM). Writes:
- `results_v9/passages.csv` — one row per passage with all 9 features
- `results_v9/summary.json` — aggregate statistics per (author × source)

### Step 5: Verify against the paper

The expected values in `results_v9/summary.json` should match the paper's headline findings:

| Author | Human TTR | LLM TTR | Human syllables/word | LLM syllables/word |
|---|---|---|---|---|
| Sule Egya | 0.59 | 0.77 | 1.65 | 1.44 |
| Toyin Shittu | 0.54 | 0.64 | 1.94 | 1.73 |

If your numbers match within a few hundredths, your pipeline is correct.

## Running the notebook

The Colab notebook `pipeline/stylometric_pipeline.ipynb` provides a six-cell guided walkthrough:

1. **Cell 1:** Install numpy + pandas
2. **Cell 2:** Load `corpus/metadata.csv` and report per-author counts
3. **Cell 3:** Generate LLM passages via OpenRouter (requires API key)
4. **Cell 4:** Extract the 9 features per passage
5. **Cell 5:** Aggregate per (author × source) and report headline TTR + syllable differences
6. **Cell 6:** Per-feature table

To run in Colab: open `https://colab.research.google.com`, drag the notebook into the page, follow the cell-by-cell walkthrough.

To run locally: `jupyter notebook pipeline/stylometric_pipeline.ipynb`

## The 9 features

| Category | Feature |
|---|---|
| Lexical | n_words, ttr, mean_word_len |
| Syllabic | mean_syllables_per_word, vowel_group_count |
| Sentence-level | n_sents, mean_sentence_len_chars, sent_len_std |
| Punctuation | punct_density_per_word, function_word_ratio |

Implementation: see `pipeline/analyze_basic.py` and the equivalent cell in `stylometric_pipeline.ipynb`.

## Reproducibility notes

- All corpus files are published or fair-use excerpts.
- LLM passages were generated with `temperature=0.01` (near-deterministic). Re-running the generator should produce substantively identical texts.
- Models used: `nex-agi/nex-n2.5-mini` and `nex-agi/nex-n2.5-pro` (both via OpenRouter free tier).
- Per-author style notes and topic seeds are documented in `pipeline/llm_prompts.md`.

## Troubleshooting

| Problem | Fix |
|---|---|
| 401 Unauthorized on OpenRouter | Check `OPENROUTER_API_KEY` is set and active |
| `python pipeline/analyze_basic.py` says "no passages" | The script must be run from the repository root, not from inside `pipeline/` |
| Different headline numbers from the paper | Your LLM corpus may differ from the committed one; regenerate with `generate_llm_imitations.py` |
| Notebook cell 3 fails all generators | API key was pasted as plain text into the cell but contains the `=` sign — verify the variable assignment |

## License

The pipeline code is MIT-licensed. The corpus consists of fair-use excerpts of published literary work; do not redistribute the corpus in bulk.

---

Last updated: 2026-09-12
