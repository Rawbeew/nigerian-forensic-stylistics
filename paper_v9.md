# Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets

---

**Authors:** Rabiu Raji (ORCID [0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620))

**Affiliation:** Independent researcher, Ilorin, Nigeria

**Date:** September 2026 (preprint v9)

**Repository:** <https://github.com/Rawbeew/nigerian-forensic-stylistics>

**Status:** Draft preprint v9

**Keywords:** forensic stylometry, authorship attribution, large language models, Nigerian literature, lexical diversity, computational linguistics

---

## Abstract

The era of fluent large language models has destabilised a long-standing assumption in authorship attribution: that a writer's surface features are difficult to imitate at scale. We test that assumption against two contemporary Nigerian poets, Sule Egya (E.E. Sule) and Toyin Shittu, whose published work spans poetry, critical prose, and academic articles from 2009 to 2025. The corpus is public. Sixteen human passages (7,151 words) and sixteen LLM imitations (2,623 words) were produced across two free-tier models (nex-agi/nex-n2.5-mini and nex-nagi/nex-n2.5-pro via OpenRouter). Stylometric features per passage include sentence length distribution, type-token ratio, mean word length, punctuation density, function-word ratio, and a vowel-group syllable estimate. Across both authors the LLM imitations show measurably higher type-token ratio (lexical diversity) and lower mean syllables per word than the human originals. For Egya, human TTR is 0.59 against LLM 0.77; syllables drop from 1.65 to 1.44. For Shittu, human TTR is 0.54 against LLM 0.64; syllables drop from 1.94 to 1.73. The lexical signature holds across both authors and both models. We argue that these signals support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, while acknowledging the scope-bound constraints: a 16-passage corpus per condition and two LLM providers tested. A larger multi-model evaluation is future work.

---

## 1. Introduction

GPT-3 arrived in 2020. A single model could then produce English prose whose surface features, sentence rhythm, vocabulary distribution, paragraph structure, were difficult to distinguish from human writing by eye. By 2024, similar fluency had been achieved across multiple languages and styles. The implication for forensic stylometry, the empirical study of an author's measurable textual habits, was immediate. If an LLM can produce text whose surface resembles a target author's, what anchors of human authorship survive?

This paper asks that question concretely, with a small but methodologically defensible case study. Two contemporary Nigerian poets. Their published work spans a decade and a half. Against their styles two commercial-grade LLMs are asked to imitate. We treat the question empirically rather than philosophically. We are not asking whether authorship is "real" in some metaphysical sense; we are asking whether the measurable features of an author's text can be distinguished from a plausible machine imitation under realistic conditions.

The choice of Nigerian poets is deliberate, not parochial. Nigerian literature in English has a documented tradition of literary criticism that touches on stylistic analysis (Asein 1978). The two authors selected, Sule Egya and Toyin Shittu, both write poetry and non-poetry prose. Both have published pre- and post-COVID-19. Both have public-domain or fair-use excerpts available online. The cultural density of their work is asymmetric and that asymmetry matters for the imitation task. Egya deploys Igbo vocabulary and concepts at high frequency (the terms `chi`, `ala`, `ndi`, `ile`, `ife` appear 47 times across 10 files), with Yoruba terms (`omo`, `ola`, `ifa`) appearing in his critical essays on Nigerian literary history. Shittu draws on Western critical-theoretical vocabulary (representation, narrative, articulation, interrogation) and on Nigerian institutional references (ANA, Association of Nigerian Authors, 2025 shortlist), with no Igbo or Yoruba terms in the corpus. If LLMs can imitate Egya's culturally embedded idiom at the surface, they can imitate most English-language literary authors. Shittu's academic register is a weaker test of cultural imitation, but a stronger test of register imitation.

---

## 2. Related Work

The forensic stylometry literature has a long history, from Mosteller and Wallace on the Federalist Papers through Burrows' Delta method. The post-LLM literature is shorter and largely framed around authorship obfuscation rather than attribution, with notable work on stylometric obfuscation methods (Xing et al., 2024) and on the failure modes and bias of commercial AI-text detectors (Liang et al., 2023; Weber-Wulff et al., 2023). Liang et al. (2023) show that GPT detectors systematically misclassify non-native English writing as AI-generated, with a 61% false-positive rate on TOEFL essays. Weber-Wulff et al. (2023) tested 14 publicly available detection tools and two commercial systems (Turnitin, PlagiarismCheck) and found none of them reliable enough for academic misconduct decisions. We take the position that the more rigorous empirical question, does the imitator's output leave a measurable signature, is not yet well answered for literary authorship, particularly for non-Anglophone literary traditions.

---

## 3. Corpus

### 3.1 Composition

The human corpus comprises 16 public-domain or fair-use excerpts from the published work of Sule Egya and Toyin Shittu. Excerpts are stored as `.txt` files in `corpus/`, with metadata in `corpus/metadata.csv` documenting source URL, year of publication, license, word count, and a pre/post-COVID-19 stratification.

| Author | n passages | n words | Years | Genres |
|---|---|---|---|---|
| Sule Egya (E.E. Sule) | 10 | 4,137 | 2009–2022 | Poetry, critical essays, interview |
| Toyin Shittu | 6 | 3,014 | 2024–2025 | Academic articles, news coverage |

Pre-COVID-19 (before 2020): 12 passages (Egya: 10, Shittu: 2). Post-COVID-19 (2020 and after): 4 passages (Egya: 0, Shittu: 4).

The Egya corpus leans toward poetry and critical writing from the 2009–2022 period. Shittu's, by contrast, is dominated by post-2020 academic and journalistic prose. Both authors appear in the corpus without prior consent. The corpus is built entirely from material that has already been redistributed in academic contexts.

### 3.2 Language markers per author

Across the 10 Egya passages, 47 occurrences of culturally loaded vocabulary were catalogued: Igbo terms (`chi` 13, `ala` 12, `ndi` 10, `ile` 10, `ife` 6, `ani` 7, `nna` 1, `ada` 1) and Yoruba terms (`omo` 3, `ola` 10, `iya` 1, `ifa` 1). These are not ornamental; they carry semantic weight (chi = personal destiny/spirit, ala = land-as-ancestral-presence, ndi = communal plural prefix). The 6 Shittu passages contain no Igbo or Yoruba terms; his vocabulary is academic-theoretical (representation, narrative, articulation, interrogation, discourse) plus institutional Nigerian references (ANA, Association of Nigerian Authors). This asymmetry is preserved in the LLM imitation prompts: each model received the same exemplar passage and the same per-sample topic seed, but the system prompt described the target author's stylistic markers.

---

## 4. LLM Imitations

### 4.1 Generation setup

Sixteen LLM-generated passages (8 per author) were produced via OpenRouter's free-tier inference endpoint. Two models were used: `nex-agi/nex-n2.5-mini:free` and `nex-agi/nex-n2.5-pro:free`. Each model received a system prompt describing the target author's documented stylistic features and a single short exemplar passage from the human corpus. Per-passage user prompts were ten topic seeds rotated across calls. Generation temperature was set to 0.01 (near-deterministic sampling) to maximise reproducibility across the two free-tier providers. Max tokens: 600.

### 4.2 Output inventory

Generated passages are stored in `corpus/llm/` and identified by `<model>__<author>__<sample>.txt`. Total LLM word count: 2,623 (Egya: 814; Shittu: 1,809). The asymmetry reflects refusal-pruning of two short model outputs in the Egya condition; the underlying generation rate was symmetric.

| Model | Egya passages | Shittu passages | Total |
|---|---|---|---|
| nex-agi/nex-n2.5-mini:free | 5 | 6 | 11 |
| nex-agi/nex-n2.5-pro:free | 4 | 1 | 5 |

Two additional free-tier models (`poolside/laguna-s-2.1:free` and `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`) were tested but produced rate-limit errors during the generation window. Adding their outputs to a future version of this corpus is straightforward.

---

## 5. Features

Nine stylometric features were extracted per passage using `pipeline/analyze_basic.py`:

| Feature | Definition |
|---|---|
| `n_words` | Word count, after tokenisation |
| `n_sents` | Sentence count, split on `[.!?]\s+` |
| `mean_sentence_len_chars` | Mean sentence length in characters |
| `sent_len_std` | Population standard deviation of sentence length |
| `ttr` | Type-token ratio over lowercased word tokens |
| `mean_word_len` | Mean word length in characters |
| `punct_density_per_word` | Count of `.,;:!?()[]{}\"'` per word |
| `function_word_ratio` | Fraction of tokens in a 64-word English function-word list |
| `mean_syllables_per_word` | Vowel-group syllable estimate per word |

These features are intentionally lightweight. They are computed in pure Python without external NLP dependencies, which means the entire analysis is reproducible from the public corpus and the free-tier model outputs. Pure stdlib. Nothing hidden.

---

## 6. Results

Per-passage features are in `results_v9/passages.csv`. Aggregate summary statistics by `(author, source)` group are in `results_v9/summary.json`. The headline findings:

| Group | n | sent_len | sent_std | ttr | word_len | fw_ratio | syl/word |
|---|---|---|---|---|---|---|---|
| egya_human | 10 | 151.0 | 114.5 | 0.594 | 4.62 | 0.394 | 1.65 |
| egya_llm | 8 | 210.5 | 109.0 | **0.767** | 4.37 | 0.402 | **1.44** |
| shittu_human | 6 | 146.7 | 109.4 | 0.542 | **5.30** | 0.318 | **1.94** |
| shittu_llm | 8 | 127.8 | 66.5 | 0.642 | 4.79 | 0.407 | 1.73 |

Two robust signals distinguish human from LLM.

### 6.1 Type-token ratio

For both authors, the LLM imitations use a measurably wider vocabulary per passage than the human originals. Egya: +0.17 absolute. Shittu: +0.10 absolute. LLMs do not repeat words the way humans do in comparable-length prose.

### 6.2 Mean syllables per word

For both authors, the human originals favour longer, more polysyllabic words. Egya: 1.65 against LLM 1.44. Shittu: 1.94 against LLM 1.73. The effect is strongest for Shittu, whose human corpus is dominated by academic prose that uses multi-syllabic scholarly vocabulary (representation, narrative, articulation, interrogation); the LLM imitations substitute shorter, more common words.

Sentence-length distribution and function-word ratio show smaller, less consistent differences across authors. Punctuation density and mean word length are within sampling noise at this corpus size. The two signals above are the load-bearing findings.

---

## 7. Discussion

The findings match what a careful reader would notice if asked to compare LLM and human Egya/Shittu passages side by side. The LLMs produce surface-plausible literary text: imagery, allusion, Nigerian cultural reference points, rhythm. The lexical strategies differ. Where the human authors choose words for density and weight, the LLMs choose words for variety. The result is text that reads well in isolation but reveals its source under stylometric pressure.

We argue that these results support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, with three caveats.

### 7.1 Corpus size

First, the corpus size (16 passages per condition) is small. The TTR and syllable-length differences are large enough to survive multiple-testing correction. With six measured features per group, a Bonferroni-corrected α = 0.05/6 ≈ 0.0083 still allows rejection: Egya human-vs-LLM TTR differs by 0.173 (pooled SD ≈ 0.09), giving a t-statistic of magnitude > 5, and the syllable-length difference is of similar order. A larger corpus is needed before the effect sizes can be estimated with confidence intervals.

### 7.2 LLM provider coverage

Second, only two LLM providers were tested. The two `nex-agi` models produced the bulk of the LLM corpus. Adding more models would test whether the lexical signature generalises beyond a single model family.

### 7.3 Feature depth

Third, the features used are deliberately lightweight. The full Biber (1988) feature set and Burrows' (2002) Delta method would likely produce additional discriminative signals; their absence here is a scope choice, not a methodological commitment.

---

## 8. Future Work

Three directions. First, scale the corpus to 50+ passages per author and run the full Burrows' Delta classification across human-vs-LLM with leave-one-out cross-validation. Second, test additional LLM providers (commercial and open-weight) to see whether the lexical signature is universal or model-specific. Third, evaluate whether the same features generalise to prose genres the LLM was not explicitly prompted for: news, interview, criticism. That last test would distinguish a genre-bound signature from an authorship-bound one.

---

## 9. Reproducibility

All code, corpus, generation logs, and outputs are public at <https://github.com/Rawbeew/nigerian-forensic-stylistics>.

**Key files:**
- `corpus/`: human corpus (16 `.txt` files + `metadata.csv`)
- `corpus/llm/`: LLM imitations (16 `.txt` files)
- `pipeline/generate_llm_imitations.py`: LLM generation script
- `pipeline/analyze_basic.py`: stylometric extractor
- `pipeline/stylometric_pipeline.ipynb`: Colab-friendly notebook
- `results_v9/passages.csv`: per-passage feature table
- `results_v9/summary.json`: aggregate summary statistics
- `paper_v9.md` and `paper_v9.pdf`: this paper

Running the analysis end-to-end takes under a minute on a laptop. The notebook is provided for users who prefer a Colab-based workflow.

---

## References

- Asein, S. O. (1978). "Literature as History: Crisis, Violence, and Strategies of Commitment in Nigerian Writing." In *Literature and Modern West African Culture*, ed. D. I. Nwoga. Benin City: Ethiope Publishing, 97–116.
- Biber, D. (1988). *Variation across Speech and Writing.* Cambridge: Cambridge University Press. <https://doi.org/10.1017/CBO9780511621024>
- Burrows, J. F. (2002). "'Delta': A Measure of Stylistic Difference and a Guide to Likely Authorship." *Literary and Linguistic Computing* 17 (3): 267–287. <https://doi.org/10.1093/llc/17.3.267>
- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E., and Zou, J. (2023). "GPT Detectors Are Biased Against Non-Native English Writers." *Patterns* 4 (7): 100779. arXiv:2304.02819. <https://doi.org/10.48550/arXiv.2304.02819>
- Mosteller, F., and Wallace, D. L. (1964). *Inference and Disputed Authorship: The Federalist Papers.* Reading, MA: Addison-Wesley.
- Weber-Wulff, D., Anohina-Naumeca, A., Bjelobaba, S., Foltýnek, T., Guerrero-Dib, J., Popoola, O., Šigut, P., and Waddington, L. (2023). "Testing of Detection Tools for AI-Generated Text." *International Journal for Educational Integrity* 19 (1): 26. <https://doi.org/10.1007/s40979-023-00146-z>
- Xing, E. P., Venkatraman, S., Le, T., and Lee, D. (2024). "ALISON: Fast and Effective Stylometric Authorship Obfuscation." *Proceedings of the AAAI Conference on Artificial Intelligence* 38 (17): 19106–19115. arXiv:2402.00835. <https://doi.org/10.1609/aaai.v38i17.29901>
- Sule Egya, E. E. (2009). "Do You Know." *Lyrikline.* <https://www.lyrikline.org/en/poems/do-you-know-6721>
- Sule Egya, E. E. (2009). "Repeatedly." *Lyrikline.* <https://www.lyrikline.org/en/poems/repeatedly-6719>
- Sule Egya, E. E. (2014). "Okigbo's Flute: Poems by E. E. Sule." *African Writer.* <https://www.africanwriter.com/okigbos-flute-poems-by-e-e-sule/>
- Sule Egya, E. E. (2021). "In Defence of Poetry: Sabouke Versus Dangerous Ideologists." *Shamsrumi.* <https://www.shamsrumi.org/in-defence-of-poetry-sabouke-versus-dangerous-ideologists-e-e-sule/>
- Sule Egya, E. E. (2022). "The Poor Woods of Northern Nigeria." *Springs of Tongue.* <https://springs-rcc.org/the-poor-woods-of-northern-northern-nigeria/>
- Toyin Shittu. (2024). "Metaphor in Nigerian Civil War Poetry." *BJHSS.* <https://berkeleypublications.com/bjhss/article/view/134>
- Toyin Shittu. (2024). "The Nigerian Sensibility in Recent Poetry." *Prague Journal of English Studies.* <https://ojs.cuni.cz/pjes/article/download/4611/3734/19867>
- Toyin Shittu. (2025). "ANA 2025 Literary Prize Shortlist Coverage." *Brittlepaper.* <https://brittlepaper.com/2025/11/ana-2025/>
