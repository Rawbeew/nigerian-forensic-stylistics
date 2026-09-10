# nigerian-forensic-stylistics

**Forensic stylometry of contemporary Nigerian authors tested against LLM imitations.**

> **The Computable Voice: Can a Machine Speak Like ?**
> *Stylometric forgery detection in contemporary Nigerian literature*

**Author:** Rabiu Raji ([ORCID 0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620))
**Status:** Manuscript in preparation
**Target venue:** *Journal of African Cultural Studies* (Q1) or *Digital Scholarship in the Humanities*

## Authors in cohort

| Author | Domain | Why include |
|---|---|---|
| **** | Prof, novelist, poet, literary critic | Writes BOTH poetry and criticism — intra-author control |
| **Sule Egya / E.E. Sule** | Prof, novelist, poet, critic | Writes BOTH fiction AND criticism — intra-author control |
| **** | Poet, critic, Niger State | Tiv, writes poetry AND reviews — intra-author control |
| **Toyin Shittu** | Poet, Osun State University, playwright | ANA KMVL shortlist 2025; contemporary relevance |

## Repository structure

```
.
├── README.md                              # This file
├── OUTLINE.md                             # Full paper outline (13 sections)
├── corpus/
│   ├── metadata.csv                       # Author, ID, type, source, license
│   ├── egya_poem_01_do_you_know.txt      # Seed: Sule Egya poem (151 words, lyrikline.org)
│   └── [more to be added]
├── pipeline/
│   ├── stylometric_pipeline.ipynb         # Colab notebook (Burrows + Biber + classifier)
│   ├── llm_prompts.md                     # 4 models × 3 prompt conditions
│   └── run.sh                             # Local execution script
├── drafts/
│   └── manuscript_v1.md                   # First draft (to be written)
├── figures/
│   └── (plots to be generated)            # Dendrograms, MDS, SHAP
├── CITATION.cff                          # GitHub-style citation
├── LICENSE                                # CC-BY-4.0
└── .gitignore                            # Standard excludes
```

## Status

- [x] Repo created
- [x] Outline drafted
- [x] Sule Egya poem extracted (lyrikline.org)
- [x] Colab pipeline adapted for 4 authors
- [x] **Corpus assembled: 18 excerpts, 9,016 words**
  - : 5 excerpts (interviews, news, panel coverage)
  -: 6 excerpts (interviews, his own critical writing in Channels TV, Shamsrumi, Musefair)
  - Shittu: 6 excerpts (his own academic articles + ANA news)
  - Egya: 10 excerpts (5 poetry, 4 critical essays, 1 interview)
- [ ] Pull remaining Sule Egya excerpts (poetry + critical)
- [ ] Build LLM imitation corpus (160 passages)
- [ ] Run analysis
- [ ] Draft paper
- [ ] arXiv preprint
- [ ] Journal submission

## Public excerpt sources (all fair use)

- **Sule Egya:** [lyrikline.org](https://www.lyrikline.org/en/authors/e-e-sule), [africanwriter.com](https://www.africanwriter.com/e-e-sule-a-burden-to-get-it-right/)
- **:** [Daily Trust interview](https://dailytrust.com/how-near-death-experience-prompted-my-novel-maryam-/), Amazon *Burning Bright* listing
- **Toyin Shittu** bio at Osun State University (ujws.uniosun.edu.ng/ajllcs/issue/view/49)
- **Toyin Shittu:** [Berkeley Publications (Oseni & Hamzah 2024)](https://berkeleypublications.com/bjhss/article/view/134), [Daily Trust](https://dailytrust.com/daily-trust-corps-member-shortlisted-for-ana-poetry-prize/), Osun State University

## Data availability

The corpus used in this study consists of copyrighted literary works. For copyright reasons, the corpus is not publicly distributed. Excerpts used in the paper (200-500 words each) are within fair use limits for scholarly analysis under Nigerian Copyright Act §9 (criticism, review, scholarship) and comparable international frameworks.

Researchers interested in replicating this study may contact the corresponding author (Rabiu Raji, [raj.rawbeew@gmail.com](mailto:raj.rawbeew@gmail.com)) for guidance on corpus construction following standard academic fair use principles.

## Running the pipeline

```bash
# Open the Colab notebook
pipeline/stylometric_pipeline.ipynb

# Or run locally
cd pipeline
jupyter notebook stylometric_pipeline.ipynb
```

## Citation

If you use this work, please cite:

```bibtex
@misc{raji2026computable,
  author = {Raji, Rabiu},
  title = {The Computable Voice: Forensic Stylometry of Four Contemporary Nigerian Authors Tested Against LLM Imitations},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Rawbeew/nigerian-forensic-stylistics}},
  note = {Manuscript in preparation}
}
```

## License

Code: MIT (this repository's pipeline code)
Manuscript text: CC-BY-4.0 (when published)
Corpus excerpts: Public excerpt excerpts only, fair use, not redistributable

## Contact

- **Author:** Rabiu Raji
- **ORCID:** [0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620)
- **Email:** raj.rawbeew@gmail.com
- **Telegram:** same Hermes thread

Last updated: 2026-09-10
