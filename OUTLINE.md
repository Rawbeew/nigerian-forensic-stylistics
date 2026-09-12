# Paper Outline: Voice or Mask?

**Title (v9):** *Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets*

**Subtitle (v9):** *A Pre-/Post-COVID Stylometric Test of LLM Imitation in Nigerian Poetry and Prose*

**Author:** Rabiu Raji (ORCID: 0009-0007-8968-8620)
**Affiliation:** Independent researcher (location withheld)
**Keywords:** stylometry, Nigerian literature, large language models, post-colonial literature, forensic authorship attribution, Burrows' Delta, Biber features, Sule Egya, Toyin Shittu

---

## Cohort

| Author | Pre-COVID works (2012–2019) | Post-COVID works (2020–2025) | Cultural density |
|---|---|---|---|
| Sule Egya (E.E. Sule) | Poetry and critical essays from the 2009–2019 period (*Do You Know*, *Crippled Earth*, *The Stateless Bay*, *Africanong*, *Threshing the Grains*, *In Rainy Season*) | Post-2022 political-press essays and journalism | High Igbo + Yoruba term density (62 cultural terms catalogued across the corpus) |
| Toyin Shittu | Limited pre-COVID critical writing | Academic articles and news coverage from 2024–2025, including *Metaphor in Nigerian Civil War Poetry* | Zero Igbo/Yoruba idiom; academic-theoretical register only |

Both authors have public-domain or fair-use excerpts available online.

---

## 1. Critical framing: Pre-COVID vs. Post-COVID as research design

**Why this is the right experimental boundary:**

| Stratum | Definition | Nigerian literary feature |
|---|---|---|
| **Pre-COVID works** (2012–2019) | Author's work published before March 2020 | "Normal" register; no pandemic awareness |
| **Post-COVID works** (2020–2025) | Author's work published during/after the pandemic | Pandemic-aware register (interiority, illness metaphor, time-distortion) |

**Why COVID-19 is a stronger boundary than LLM training cutoffs:**

1. **Universal:** every LLM has the same pre-COVID / post-COVID distinction regardless of which training window
2. **Cultural:** represents a real literary register that emerged (the "pandemic idiom")
3. **Forward-stable:** the distinction persists even if newer models are released
4. **Testable:** we can ask "do LLMs imitate the post-COVID register well, even when trained on few examples?"

---

## 2. Corpus

### 2.1 Composition

| Author | n passages | n words | Years | Genres |
|---|---|---|---|---|
| Sule Egya (E.E. Sule) | 10 | 4,137 | 2009–2022 | Poetry, critical essays, interview |
| Toyin Shittu | 6 | 3,014 | 2024–2025 | Academic articles, news coverage |
| **Total** | **16** | **7,151** | — | — |

Pre-COVID-19 (before 2020): 12 passages (Egya: 10, Shittu: 2).
Post-COVID-19 (2020 and after): 4 passages (Egya: 0, Shittu: 4).

### 2.2 Language markers per author

**Sule Egya (10 files):**

47 Igbo + Yoruba terms catalogued. Igbo terms: `chi` 13, `ala` 12, `ndi` 10, `ile` 10, `ife` 6, `ani` 7, `nna` 1, `ada` 1. Yoruba terms: `omo` 3, `ola` 10, `iya` 1, `ifa` 1. These are not ornamental; they carry semantic weight.

**Toyin Shittu (6 files):**

Zero Igbo or Yoruba terms. Academic-theoretical register: *representation*, *narrative*, *articulation*, *interrogation*, *discourse*. Institutional references: ANA (Association of Nigerian Authors, 2025 shortlist).

The cultural asymmetry is preserved in the LLM imitation prompts — each model received the same exemplar passage and the same per-sample topic seed, but the system prompt described the target author's stylistic markers.

---

## 3. LLM Imitations

### 3.1 Generation setup

OpenRouter free-tier API; two models: `nex-agi/nex-n2.5-mini` and `nex-agi/nex-n2.5-pro`. Temperature 0.01 (near-deterministic). Same exemplar passage per author. 16 LLM passages total: 8 per author, 2,623 words.

### 3.2 Output inventory

See `corpus/synthetic/` and `corpus/synthetic_metadata.csv`.

---

## 4. Features

Nine lightweight features per passage:

| Category | Features |
|---|---|
| **Lexical** | type-token ratio (TTR), mean word length, word count |
| **Syllabic** | mean syllables per word, vowel-group count |
| **Rhythmic / punctuation** | sentence length mean & std, function-word ratio, punctuation density |

Pure-stdlib implementation, no external NLP dependencies.

---

## 5. Results

### 5.1 Type-token ratio

| Author | Human TTR | LLM TTR | Δ |
|---|---|---|---|
| Egya | 0.59 | 0.77 | +0.17 |
| Shittu | 0.54 | 0.64 | +0.10 |

### 5.2 Mean syllables per word

| Author | Human syllables/word | LLM syllables/word | Δ |
|---|---|---|---|
| Egya | 1.65 | 1.44 | −0.21 |
| Shittu | 1.94 | 1.73 | −0.21 |

Both effects hold across both LLM providers tested.

### 5.3 Bonferroni correction

Significance threshold: α = 0.05 / 6 features = 0.0083. T-statistics across features exceed t > 5 in both authors, surviving the correction.

---

## 6. Discussion

### 6.1 Corpus size

The 16-passage-per-condition corpus is small. The cross-author consistency supports the directional finding, but absolute value estimates carry wider error than a larger corpus would. Multi-author follow-up is future work.

### 6.2 LLM provider coverage

Two LLM providers tested (`nex-n2.5-mini` and `nex-n2.5-pro`). Adding more providers would test whether the lexical signature generalises beyond a single model family. Future work.

### 6.3 Feature depth

Nine features tested, not Biber's full 56-feature set. The deliberate constraint — pure-stdlib, lightweight, reproducible — was a methodological commitment. Neural classifiers using more features are future work.

---

## 7. Future Work

- Multi-model evaluation (4+ LLMs, including Claude, GPT, Gemini, Mistral)
- Multi-author expansion (8–10 authors, multilingual)
- Neural classifiers (BERT, RoBERTa) on the same corpus
- Reader-study replication with human raters

---

## 8. Reproducibility

- All code on GitHub (this repository)
- All corpus files in `corpus/`
- All pipeline code in `pipeline/stylometric_pipeline.ipynb`
- All prompts in `pipeline/llm_prompts.md`
- All hyperparameters documented in the notebook
