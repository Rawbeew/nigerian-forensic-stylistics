# How to run the Nigerian Forensic Stylistics pipeline

## Quick start (15-20 min)

### Step 1: Open in Colab

Open the notebook `pipeline/stylometric_pipeline.ipynb` in Google Colab:
- Drag the file into https://colab.research.google.com
- Or: github.com → click notebook → Open in Colab

### Step 2: Get a free API key

Pick ONE of these (free tier works):

| Provider | URL | Variable name |
|---|---|---|
| **Groq (recommended)** | https://console.groq.com | `GROQ_API_KEY` |
| OpenRouter | https://openrouter.ai | `OPENROUTER_API_KEY` |
| Google AI Studio | https://aistudio.google.com | (need to add) |

Sign in → create API key → copy → paste in Cell 3

### Step 3: Run cells in order

1. **Cell 1** (Ctrl+F10): Install dependencies (~2 min)
2. **Cell 2**: Load human corpus (auto-loaded — no setup needed)
3. **Cell 3**: Paste API key → Run all generations (~10 min for 160 passages)
4. **Cell 4**: Feature extraction (~1 min)
5. **Cell 5**: Burrows' Delta + clustering + MDS (~30 sec)
6. **Cell 6**: Per-classifier + SHAP (~30 sec)

### Step 4: Download artifacts

At the end you'll have:
- `human_corpus.csv` — your 27 passages
- `synthetic_corpus.csv` — 160 LLM imitations
- `features.csv` — extracted features
- `dendrogram.png` — clustering visualization
- `mds_projection.png` — 2D projection
- `shap_importance.png` — feature importance
- `feature_importance.csv` — numeric feature ranks
- `delta_matrix.npy` — pairwise distances

## What to do with the output

1. Look at `dendrogram.png` — does human/author cluster separate from LLM clusters?
2. Look at `mds_projection.png` — clear separation?
3. Check `shap_importance.png` — what features matter most?
4. Check classifier Macro-F1 — how well does LR/RF distinguish?

## When you get your results

Send screenshots or the CSV outputs back. I'll help interpret them and start drafting the paper.

## Troubleshooting

| Problem | Fix |
|---|---|
| 401 Unauthorized on Groq | Get a fresh API key |
| "Module not found" | Re-run Cell 1 (install) |
| Cell 3 fails all generators | Check your API key — paste it carefully |
| Output is mostly 0-length passages | Empty API key or wrong format |
| Notebook too slow | Switch runtime to GPU (Runtime → Change runtime type → T4) |
| Want to test without full corpus | Use the 3-row sample data first |

## After getting results

Come back to the chat with:
- Macro-F1 score per author
- SHAP top 5 features
- Whether human/LLM clusters separated

We'll then:
1. Draft Section 5 (Results) of the paper
2. Draft Section 6 (Discussion)
3. Submit to arXiv
4. Then to journal (JACS or DSH)
