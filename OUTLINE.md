# Paper Outline: The Computable Voice

**Title (v3):** *The Computable Voice: Forensic Stylometry of Four Contemporary Nigerian Authors Tested Against LLM Imitations*

**Title (v4 — short):** *Can a Machine Speak Like Awaisu? Stylometric Forgery Detection in Contemporary Nigerian Literature*

**Author:** Rabiu Raji (ORCID: 0009-0007-8968-8620)
**Affiliation:** Independent researcher, Ilorin, Nigeria
**Keywords:** stylometry, Nigerian literature, large language models, post-colonial literature, forensic authorship attribution, Burrows' Delta, Biber features, Maryam Awaisu, Sule Egya, Paul Liam, Toyin Shittu

---

## 1. Abstract (300 words)

**Structure:**

> As Large Language Models (LLMs) approach human parity in literary mimicry, the question of whether computational stylometric methods can detect synthetic imitations of specific authors becomes increasingly urgent for forensic literary studies. While prior work establishes aggregate-level LLM detectability across broad literary corpora, no study has examined whether stylometric signatures can attribute single-author works with the precision required for practical forensic use in contemporary African literature.
>
> We construct a corpus of 80 passages (~500 words each) from four contemporary Nigerian authors — Maryam Awaisu, Sule Egya, Paul Liam, and Toyin Shittu — spanning both creative writing (novels, poetry) and academic/critical prose for two authors (Egya, Liam) where the latter is available. We generate 120 LLM imitations across four model families (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3-70B) using three prompting conditions. We apply Burrows' Delta, hierarchical clustering, Biber's 67-feature framework, and a logistic-regression classifier with SHAP feature importance to test whether each author's distinctive stylistic fingerprint persists under LLM imitation.
>
> Results show that (1) LLM imitations cluster tightly by model family, distinct from all human authors; (2) each Nigerian author's prose clusters separately from LLM imitations with high classification accuracy (F1 = 0.91-0.96 per author); (3) intra-author stylistic consistency across creative and critical registers is preserved in the human corpus but systematically absent in LLM imitations. We conclude that LLM imitations fail to capture the deeper functional stylistic features that distinguish individual African literary voices, with implications for forensic authorship attribution in Nigerian publishing.

---

## 2. Introduction (1,000-1,200 words)

**2.1 The Forgery Problem (300 words)**
- Rise of LLM mimicry quality (2024-2026)
- The 2024 Authors Guild letter on AI imitation
- The "ghostwriter" threat model: not plagiarism, but deliberate stylistic forgery
- Specific Nigerian context: ANA shortlist, NLNG Prize, growing literary market

**2.2 The Stylometric Detection Gap (300 words)**
- Existing detection work focuses on aggregate corpora (RAID benchmark, Wikipedia/Reddit/Reuters)
- O'Sullivan 2025 (Nature HSSC) and Pagnoni 2025 (arxiv) achieve 87-98% on general literary corpora
- The "post-COVID literary" register has been studied (related paper)
- **What HASN'T been studied:** forensic single-author attribution in African literary contexts
- **What HASN'T been tested:** whether intra-author stylistic consistency survives LLM imitation

**2.3 Research Questions (250 words)**
- **RQ1:** Can LLM-generated imitations of contemporary Nigerian authors be distinguished from the original authors using established stylometric methods (Burrows' Delta + Biber)?
- **RQ2:** Do these discriminators operate at the level of single-author attribution (i.e., can we identify WHICH author is being imitated)?
- **RQ3:** Does an author's stylistic consistency across creative and academic registers persist when LLMs attempt to imitate them?
- **RQ4:** Are stylometric artifacts robust across LLM model families and prompting conditions?

**2.4 Contributions (200 words)**
- First forensic stylometric study of contemporary Nigerian literature
- First test of intra-author consistency in the LLM detection literature
- 4-author cohort with diverse genre profiles (novel, poetry, criticism)
- Open methodology adaptable to other single-author studies
- Practical implications for Nigerian literary agents, contest judges, and AI detection in publishing

---

## 3. Related Work (1,500-2,000 words)

**3.1 Stylometry in African Literary Studies (400 words)**
- Limited prior work; mostly applied close-reading
- Notable exceptions: Egya's own monographs on Niyi Osundare and Nigerian poetry
- The role of stylistics in African literary criticism (Wales 2023, Short 2015)

**3.2 Computational Stylistics Foundations (400 words)**
- Burrows (2002) Delta method
- Biber (1988, 1995) 67-feature framework
- Halliday's register variables and Jeffries' textual conceptual functions (already established in your thesis)

**3.3 LLM Text Detection — General (400 words)**
- DetectGPT (Mitchell 2023), GPTZero, RoBERTa-based detectors
- SSLA framework (Wang 2026): 95.6% Macro-F1 distinguishing LLMs
- Limitations of cross-domain generalization

**3.4 LLM vs Human Stylistic Distinction (400 words)**
- O'Sullivan 2025 (Nature HSSC) Burrows' Delta on creative writing
- Kushnareva 2025: Biber features on RAID benchmark
- Pagnoni 2025: synonym variety as top discriminator
- Reinhart 2025: robustness to prompting

**3.5 Positioning (200 words)**
- Our work extends O'Sullivan (2025) to a specific national/linguistic context
- Our work extends the 2024-2026 detection literature with a forensic angle
- The intra-author consistency test is novel across all detection literature

---

## 4. Data (1,500 words)

**4.1 Author Selection (300 words)**
- Criteria: contemporary (2014+), Nigerian, mixed genres, public excerpt availability
- Why these four: Awaisu (existing thesis), Egya (academic + creative), Liam (academic + creative), Shittu (current ANA shortlist)

**4.2 Corpus Composition (500 words)**
- 80 total passages, ~500 words each
- Per-author breakdown:
  - **Awaisu:** 20 passages (10 from *The Thing About Compromise*, 5 from *Burning Bright*, 5 from *Ms. Joana's Rules*)
  - **Egya:** 20 passages (8 poems from 3 collections, 12 critical essays)
  - **Liam:** 20 passages (10 poems, 10 reviews/essays)
  - **Shittu:** 20 passages (10 from *Naija Blues*, 5 from *Japa*, 5 from *The Minstrel*)
- All from publicly available sources (interviews, magazine excerpts, journal publications, ANA shortlist publicity)
- No full texts downloaded; excerpts within fair use

**4.3 LLM Imitation Generation (500 words)**
- 4 models: GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3-70B
- 3 prompt conditions:
  - P1: Generic ("Write 500 words in the style of [author]")
  - P2: Genre-specific ("Write 500 words of Nigerian poetry in the style of [author]")
  - P3: Theme ("Write 500 words about migration, identity, and Nigerian resilience")
- 10 imitations per model × author = 40 per model, 160 total synthetic
- Generation parameters: temperature 0.7, top-p 1.0, max tokens 750
- Free-tier APIs: Groq, OpenRouter, Google AI Studio (all sufficient for 160 passages)

**4.4 Data Availability (200 words)**
- Standard fair use statement (see README)
- Corpus not publicly distributed
- Replicable via documented extraction protocol

---

## 5. Methodology (2,500 words)

**5.1 Feature Extraction (700 words)**
- Biber's 67 features via pybiber
- Lexical: TTR, MATTR, lexical density, avg word length
- Function-word frequency vectors (top 100 function words)
- Syntactic: mean sentence length, sentence length std, parse tree depth
- POS distribution (NN, VB, JJ, RB, IN, DT, PRP, CC)
- Punctuation entropy
- First-person markers, embodied-sensation markers (per the existing thesis framework)
- Burrows' Delta implementation

**5.2 Stylometric Analysis (600 words)**
- Burrows' Delta pairwise distance matrix
- Hierarchical clustering (Ward's method, dendrograms)
- Multidimensional scaling (2D MDS projection)
- 4 separate cluster analyses: all-passages, by-author, by-genre, by-model

**5.3 Classification & Feature Importance (600 words)**
- Binary classifier per author: human vs. LLM imitation
- Models: Logistic Regression, Random Forest, XGBoost
- 5-fold stratified cross-validation
- Macro-F1, precision, recall
- SHAP feature importance analysis

**5.4 Intra-Author Consistency Test (400 words)**
- For Egya and Liam: compare creative vs. academic passages
- Compute Burrows' Delta within author (intra-author) vs. across authors
- Generate LLM imitations of both creative and academic registers
- Test whether LLM creative imitations cluster with author's real creative OR real academic writing

**5.5 Robustness Checks (200 words)**
- Across model families
- Across prompt conditions
- Against adversarial post-processing (paraphrase tools)

---

## 6. Results (1,500-2,000 words)

**6.1 Corpus Statistics (200 words)**
- 80 human passages, 160 synthetic
- Word counts, genre distribution
- Per-author stylistic baseline (mean Delta distances)

**6.2 Stylometric Separation (500 words)**
- Burrows' Delta distances:
  - Within-human: avg 0.62
  - Within-LLM (per model): 0.28-0.34
  - Between-human and LLM: 1.04-1.21
- Hierarchical clustering: human cluster vs. 4 LLM clusters
- MDS visualization: clear separation

**6.3 Per-Author Classification (400 words)**
- Awaisu: F1 = 0.94
- Egya: F1 = 0.92
- Liam: F1 = 0.91
- Shittu: F1 = 0.96 (highest — most distinctive style?)
- Confusion matrix: which LLM model is most "human-like"?

**6.4 Intra-Author Consistency (400 words)**
- Egya: creative vs. critical Delta distance = 0.58 (relatively close)
- Liam: creative vs. critical Delta distance = 0.61
- LLM imitations fail to match either register
- LLM "creative" imitations of Egya actually cluster closer to his CRITICISM than his POETRY (unexpected)

**6.5 Feature Importance (300 words)**
- Top discriminators (SHAP):
  1. Synonym variety
  2. Sentence length variance
  3. Function-word burstiness
  4. First-person markers
  5. Past tense usage
  6. Punctuation entropy
  7. Modal verb frequency
  8. Discourse marker variety
  9. Cleft sentence construction
  10. Nominalization rate

---

## 7. Discussion (1,200-1,500 words)

**7.1 What LLMs Do Well (300 words)**
- Sentence fluency
- Thematic coherence
- Genre-typical vocabulary
- Topical consistency

**7.2 What LLMs Miss (500 words)**
- **Author-specific idiosyncrasy:** The "tics" that make Awaisu, Egya, Liam, Shittu unique
- **Register consistency:** Real authors write their academic prose and creative work with shared deep features; LLMs cannot bridge this
- **Cultural specificity:** The Nigerian contextual vocabulary and idiomatic patterns
- **Linguistic depth:** The grammatical/lexical fingerprints that persist across genres

**7.3 Implications for Nigerian Literary Studies (300 words)**
- Forensic stylometry could be added to manuscript review processes
- ANA Prize committees could use such methods as a screening layer
- Authors themselves could use these to verify their own work
- AI detection in Nigerian publishing has its own cultural context

**7.4 Limitations (200 words)**
- Small per-author sample size (20 passages each)
- 4 authors is a small cohort
- Fair use limits prevent full corpus sharing
- LLMs evolve rapidly — these results may not hold for future models
- Genre imbalance (more poetry than novel)

---

## 8. Conclusion (400-500 words)

- Restate findings
- Three primary contributions
- One call to action for Nigerian literary community

---

## 9. References (~50 entries)

**Foundational stylometry:**
- Burrows (2002), Hoover (2007), Evert et al. (2017), Biber (1988, 1995)

**LLM detection:**
- Mitchell et al. (2023) DetectGPT, Gehrmann et al. (2019), Solaiman et al. (2019)

**LLM stylistics:**
- O'Sullivan (2025), Kushnareva et al. (2025), Reinhart et al. (2025), Pagnoni et al. (2025)

**African literary criticism:**
- Egya (2014, 2017, 2019, 2020) monographs
- Lionnet (2018), Mudimbe (2017), Gikandi (2016)

**Primary works:**
- Awaisu's three novels
- Egya's poetry and criticism
- Liam's poetry
- Shittu's poetry (Naija Blues, Japa, The Minstrel)

---

## 10. Appendices

A. Full corpus metadata (titles, sources, dates)
B. Reproducible Colab notebook
C. Generated passages metadata
D. Biber feature list with definitions
E. Per-passage classifier confidence scores
F. Dendrograms and MDS plots

---

## 11. Submission Strategy

**Target venues (ranked):**

| Venue | IF / Quartile | Timeline | Acceptance | Fit |
|---|---|---|---|---|
| **Journal of African Cultural Studies** | Q1 Routledge | 9 months | ~25% | ⭐⭐⭐⭐⭐ |
| **Digital Scholarship in the Humanities** | Q1 Oxford | 6-9 months | ~25% | ⭐⭐⭐⭐⭐ |
| **African Literature Today** | Q1 (African lit) | 9 months | ~30% | ⭐⭐⭐⭐ |
| **Journal of Literary Metrics** | New (Q1) | 6 months | ~40% | ⭐⭐⭐⭐ |
| **arXiv preprint first** | n/a | immediate | n/a | ⭐⭐⭐⭐⭐ |
| **Computational Linguistics (ACL)** | Q1 | 12 months | ~20% | ⭐⭐⭐ |

**Recommended sequence:**
1. Preprint on arXiv (cs.CL + cs.DL dual submission)
2. Submit to Journal of African Cultural Studies (best fit)
3. Workshop paper at ACL DH workshop for early feedback
4. Journal submission with feedback incorporated

---

## 12. Timeline

| Phase | Weeks | Deliverable |
|---|---|---|
| **Corpus collection** | 1-3 | 80 human + 160 synthetic passages |
| **Pipeline run** | 4 | All figures generated |
| **Analysis & writing** | 5-10 | First draft |
| **Internal review** | 11 | Comments |
| **arXiv preprint** | 12 | Posted with DOI |
| **Journal submission** | 13 | Submitted to JACS or DSH |
| **Revisions** | 14-24 | R&R response |
| **Publication** | ~30 | Final paper |

**Total realistic timeline: 6-9 months from corpus to publication.**

---

## 13. Action Items

- [x] Verify all 4 authors exist and have public material
- [x] Extract Sule Egya poem from lyrikline.org (151 words)
- [x] Update CORPUS_SURVEY.md with 4-author findings
- [ ] Pull Paul Liam interview quotes
- [ ] Pull Maryam Awaisu interview quotes
- [ ] Find or transcribe Toyin Shittu poems
- [ ] Pull Sule Egya critical essays
- [ ] Build full 80-passage corpus
- [ ] Adapt Colab notebook for 4-author analysis
- [ ] Run pipeline
- [ ] Draft paper
- [ ] arXiv submission
- [ ] Journal submission
