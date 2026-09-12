# nigerian-forensic-stylistics

**Forensic stylometry of contemporary Nigerian poets tested against LLM imitations.**

**Author:** Rabiu Raji ([ORCID 0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620))
**Affiliation:** Independent researcher (location withheld)
**Status:** Preprint
**Date:** September 2026

## About

This preprint applies a lightweight stylometric feature set (type-token ratio, mean syllables per word, sentence length distribution, function-word ratio, punctuation density) to a small public corpus of two contemporary Nigerian poets and tests whether those features distinguish human-authored passages from LLM imitations. The paper, corpus, and analysis pipeline are all in this repository. See `paper.pdf` for the manuscript.

## Authors in cohort

| Author | Domain | Why included |
|---|---|---|
| Sule Egya (E.E. Sule) | Research Professor, University of Duisburg-Essen (appointed April 2026); formerly Associate Professor, IBB University, Lapai, Niger State (2014–2026); born 1976, Benue State; PhD University of Abuja | Writes poetry, critical essays, and journalism across a 13-year span; pre- and post-COVID-19 work available; heavy Igbo and Yoruba idiom embedded in literary-critic prose |
| Toyin Shittu | Poet and academic; ANA 2025 shortlist (Kin Mayaomi Visionary Literature Prize) | Writes poetry, academic articles, and news coverage; post-2020 academic register with no Igbo or Yoruba idiom; provides cross-author generalisation test |

## Repository structure

```
.
├── paper.md                # Manuscript source (Markdown)
├── paper.pdf               # Manuscript (rendered PDF)
├── paper.tex               # Manuscript (Pandoc-generated LaTeX, for arXiv upload)
├── paper_combined.md       # Abstract + one-page summary (single document)
├── paper_combined.pdf      # Abstract + summary (rendered PDF)
├── paper_abstract.txt      # Standalone abstract
├── paper_summary.txt       # Standalone one-page summary
├── OUTLINE.md              # Working outline of the paper
├── HOW_TO_RUN.md           # Step-by-step pipeline walkthrough
├── CITATION.cff            # GitHub citation metadata
├── LICENSE                 # Code: MIT; Manuscript: CC-BY-4.0
├── corpus/                 # 16 human-authored source files + metadata
├── pipeline/               # Jupyter notebook + LLM prompt documentation
└── results_v9/             # Generated figures and tables
```

## Cohort details

| Author | n passages | n words | Years | Genres |
|---|---|---|---|---|
| Sule Egya (E.E. Sule) | 10 | 4,137 | 2009–2022 | Poetry, critical essays, interview |
| Toyin Shittu | 6 | 3,014 | 2024–2025 | Academic articles, news coverage |
| **Total** | **16** | **7,151** | — | — |

Pre-COVID-19 (before 2020): 12 passages (Egya: 10, Shittu: 2).
Post-COVID-19 (2020 and after): 4 passages (Egya: 0, Shittu: 4).

LLM imitations: 16 passages (8 per author, 2,623 words total) produced via OpenRouter free-tier using two models. Prompts are documented in `pipeline/llm_prompts.md`.

## Headline finding

Across both authors, LLM imitations show **higher type-token ratio** (lexical diversity) and **lower mean syllables per word** (avoidance of polysyllabic vocabulary) than the human originals.

| Author | Human TTR | LLM TTR | Δ |
|---|---|---|---|
| Egya | 0.59 | 0.77 | +0.17 |
| Shittu | 0.54 | 0.64 | +0.10 |

| Author | Human syllables/word | LLM syllables/word | Δ |
|---|---|---|---|
| Egya | 1.65 | 1.44 | −0.21 |
| Shittu | 1.94 | 1.73 | −0.21 |

The lexical signature holds across both authors and both LLM providers.

## Data availability

The corpus consists of public-domain or fair-use excerpts from the published work of Sule Egya and Toyin Shittu. Excerpts are stored as `.txt` files in `corpus/` with metadata in `corpus/metadata.csv` (source URL, year, license, word count, pre/post-COVID stratification). Reproducibility instructions live in `paper.pdf` Section 9.

Researchers interested in replicating this study may contact the corresponding author for guidance on corpus construction following standard academic fair use principles.

## Running the pipeline

The analysis pipeline is a six-cell Colab notebook. Open `pipeline/stylometric_pipeline.ipynb` in Google Colab, paste a free-tier LLM API key (OpenRouter or Groq) in Cell 3, and run cells 1–6 in order. Full walkthrough in `HOW_TO_RUN.md`.

## Citation

DOI: **10.5281/zenodo.22725022**

**Available at:**
- Zenodo (canonical DOI): https://zenodo.org/records/22725022
- GitHub (repository): https://github.com/Rawbeew/nigerian-forensic-stylistics
- ResearchGate: https://www.researchgate.net/publication/414253795
- Academia.edu: https://www.academia.edu/175437423/Voice_or_Mask

**Chicago author-date:**

> Raji, Rabiu. 2026. "Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets." Preprint. Zenodo. https://zenodo.org/records/22725022.

**BibTeX:**

```bibtex
@misc{raji2026voice,
  author       = {Raji, Rabiu},
  title        = {Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets},
  year         = {2026},
  publisher    = {Zenodo},
  howpublished = {\\url{https://zenodo.org/records/22725022}},
  note         = {Preprint}
}
```

## License

- Code: MIT
- Manuscript text: CC-BY-4.0
- Corpus excerpts: public-domain or fair-use excerpts only; not redistributable

## Contact

- **Author:** Rabiu Raji
- **ORCID:** [0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620)
- **Email:** raj.rawbeew@gmail.com

---

Last updated: 2026-09-12
