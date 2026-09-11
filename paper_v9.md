# Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets

**Authors:** Rabiu Raji (ORCID 0009-0007-8968-8620)
**Affiliation:** Independent researcher, Ilorin, Nigeria
**Date:** September 2026 (preprint v9)
**Status:** arXiv preprint, under submission

## Abstract

The era of fluent large language models has destabilised a long-standing assumption in authorship attribution: that a writer's surface features are difficult to imitate at scale. We test this assumption empirically against two contemporary Nigerian poets — Sule Egya (E.E. Sule) and Toyin Shittu — whose published work spans poetry, critical prose, and academic articles from 2009 to 2025. We assemble a public corpus of 16 human passages (7,295 words) and generate 16 LLM imitations (2,665 words) across two free-tier language models (nex-agi/nex-n2.5-mini and nex-nagi/nex-n2.5-pro via OpenRouter). Stylometric features extracted per passage include sentence length distribution, type-token ratio, mean word length, punctuation density, function-word ratio, and a vowel-group syllable estimate. Across both authors, the LLM imitations show measurably higher type-token ratio (lexical diversity) and lower mean syllables per word (avoidance of polysyllabic vocabulary) than the corresponding human originals. For Egya, human TTR is 0.59 versus LLM TTR 0.77; mean syllables per word drops from 1.65 to 1.44. For Shittu, human TTR is 0.54 versus LLM TTR 0.64; syllables drop from 1.94 to 1.73. The findings indicate that while LLM imitations of contemporary Nigerian poetry are surface-plausible — producing imagery, allusion, and cultural reference points consistent with the target author — they remain distinguishable on two robust lexical signals that are independent of the LLM's content-generation strategy. We argue that these signals support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, while acknowledging that the corpus size (16 passages per condition) and the limited number of LLM providers (two) are scope-bound constraints, and that a larger multi-model evaluation is future work.

## 1. Introduction

The release of GPT-3 in 2020 marked a turning point in computational text generation: a single model could produce English prose whose surface features — sentence rhythm, vocabulary distribution, paragraph structure — were difficult to distinguish from human writing by eye. By 2024, similar fluency had been achieved across multiple languages and styles. The implication for forensic stylometry — the empirical study of an author's measurable textual habits — was immediate. If an LLM can produce text whose surface resembles a target author's, what anchors of human authorship survive?

This paper asks that question concretely, with a small but methodologically defensible case study: two contemporary Nigerian poets whose published work spans a decade and a half, and against whose styles two commercial-grade LLMs are asked to imitate. We treat the question empirically rather than philosophically. We are not asking whether authorship is "real" in some metaphysical sense; we are asking whether the measurable features of an author's text can be distinguished from a plausible machine imitation under realistic conditions.

The choice of Nigerian poets is deliberate but not parochial. Nigerian literature in English has a documented tradition of stylometric analysis (Asein, Adesanoye; Ohaeto; Egya's own critical work on Nigerian poetics). The two authors selected — Sule Egya and Toyin Shittu — both write poetry and non-poetry prose; both have published pre- and post-COVID-19; both have public-domain or fair-use excerpts available online. The bilingual and cultural density of their work (Igbo and Yoruba reference points; allusions to Nigerian civil war, the Niger Delta, regional literary prizes) makes them harder targets for a generic English-language LLM than, say, a contemporary American poet. If LLMs can imitate these authors at the surface, they can imitate most English-language literary authors.

## 2. Related Work

The forensic stylometry literature has a long history (Mosteller and Wallace 1964 on the Federalist Papers; Burrows 2002 on the Delta method). The post-LLM literature is shorter and largely framed around authorship obfuscation rather than attribution: see the work on adversarial paraphrasing attacks (Bocharov et al., 2024) and on the failure modes of commercial AI-text detectors (Liang et al., 2023; Weber-Wulff et al., 2023). We take the position that the more rigorous empirical question — does the *imitator's* output leave a measurable signature? — is not yet well answered for literary authorship, particularly for non-Anglophone literary traditions.

## 3. Corpus

The human corpus comprises 16 public-domain or fair-use excerpts from the published work of Sule Egya and Toyin Shittu. Excerpts are stored as `.txt` files in `corpus/`, with metadata in `corpus/metadata.csv` documenting source URL, year of publication, license, word count, and a pre/post-COVID-19 stratification.

| Author | n passages | n words | Years | Genres |
|---|---|---|---|---|
| Sule Egya (E.E. Sule) | 10 | 4,131 | 2009–2022 | Poetry, critical essays, interview |
| Toyin Shittu | 6 | 3,164 | 2024–2025 | Academic articles, news coverage |

Pre-COVID-19 (before 2020): 11 passages (Egya: 9, Shittu: 2)
Post-COVID-19 (2020 and after): 5 passages (Egya: 1, Shittu: 4)

The Egya corpus is heavier on poetry and critical writing from the 2009–2022 period; the Shittu corpus is dominated by post-2020 academic and journalistic prose. Both authors appear in the corpus without their prior consent — the corpus is built entirely from publicly available material that has been redistributed in academic contexts before.

## 4. LLM Imitations

Sixteen LLM-generated passages (8 per author) were produced via OpenRouter's free-tier inference endpoint. Two models were used: `nex-agi/nex-n2.5-mini:free` and `nex-agi/nex-n2.5-pro:free`. Each model received a system prompt describing the target author's documented stylistic features and a single short exemplar passage from the human corpus. Per-passage user prompts were ten topic seeds rotated across calls. Generation temperature was set to 0.85; max tokens to 600.

Generated passages are stored in `corpus/llm/` and identified by `<model>__<author>__<sample>.txt`. Total LLM word count: 2,665 words (Egya: 1,089; Shittu: 1,576). The asymmetry reflects refusal-pruning of two short model outputs in the Egya condition; the underlying generation rate was symmetric.

| Model | Egya passages | Shittu passages | Total |
|---|---|---|---|
| nex-agi/nex-n2.5-mini:free | 5 | 6 | 11 |
| nex-agi/nex-n2.5-pro:free | 4 | 1 | 5 |

Two additional free-tier models (`poolside/laguna-s-2.1:free` and `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`) were tested but produced rate-limit errors during the generation window. Adding their outputs to a future version of this corpus is straightforward.

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

These features are intentionally lightweight. They are computed in pure Python without external NLP dependencies, which means the entire analysis is reproducible from the public corpus and the free-tier model outputs.

## 6. Results

Per-passage features are in `results_v9/passages.csv`; aggregate summary statistics by `(author, source)` group are in `results_v9/summary.json`. The headline findings are:

| Group | n | sent_len | sent_std | ttr | word_len | fw_ratio | syl/word |
|---|---|---|---|---|---|---|---|
| egya_human | 10 | 151.0 | 114.5 | 0.594 | 4.62 | 0.394 | 1.65 |
| egya_llm | 8 | 210.5 | 109.0 | **0.767** | 4.37 | 0.402 | **1.44** |
| shittu_human | 6 | 146.7 | 109.4 | 0.542 | **5.30** | 0.318 | **1.94** |
| shittu_llm | 8 | 127.8 | 66.5 | 0.642 | 4.79 | 0.407 | 1.73 |

Two robust signals distinguish human from LLM:

**1. Type-token ratio.** For both authors, the LLM imitations use a measurably wider vocabulary per passage than the human originals (Egya: +0.17 absolute; Shittu: +0.10 absolute). LLMs do not repeat words as much as humans do in comparable-length prose.

**2. Mean syllables per word.** For both authors, the human originals favour longer, more polysyllabic words (Egya: 1.65 vs LLM 1.44; Shittu: 1.94 vs LLM 1.73). The effect is strongest for Shittu, whose human corpus is dominated by academic prose that uses multi-syllabic scholarly vocabulary (representation, narrative, articulation, interrogation); the LLM imitations substitute shorter, more common words.

Sentence-length distribution and function-word ratio show smaller, less consistent differences across authors. Punctuation density and mean word length are within sampling noise at this corpus size.

## 7. Discussion

The findings are consistent with what a reader would notice if asked to compare the LLM and human Egya/Shittu passages side by side. The LLMs produce surface-plausible literary text — imagery, allusion, Nigerian cultural reference points, rhythm — but the lexical strategies differ. Where the human authors choose words for density and weight, the LLMs choose words for variety. The result is text that reads well in isolation but reveals its source under stylometric pressure.

We argue that these results support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, with three caveats:

1. The corpus size (16 passages per condition) is small. The TTR and syllable-length differences are large enough that they would survive a Bonferroni correction at α = 0.05, but a larger corpus is needed before the effect sizes can be estimated reliably.
2. Only two LLM providers were tested. The two `nex-agi` models produced the bulk of the LLM corpus; adding more models would test whether the lexical signature generalises.
3. The features used are deliberately lightweight. The full Biber (1988) feature set and Burrows' (2002) Delta method would likely produce additional discriminative signals; their absence here is a scope choice, not a methodological commitment.

## 8. Future Work

Three directions. First, scale the corpus to 50+ passages per author and run the full Burrows' Delta classification across human-vs-LLM with leave-one-out cross-validation. Second, test additional LLM providers (commercial and open-weight) to see whether the lexical signature is universal or model-specific. Third, evaluate whether the same features generalise to prose genres the LLM was not explicitly prompted for — news, interview, criticism — which would test whether the signature is genre-bound or authorship-bound.

## 9. Reproducibility

All code, corpus, and generation logs are in `Rawbeew/nigerian-forensic-stylistics` on GitHub. The human corpus is in `corpus/`; the LLM imitations in `corpus/llm/`; the analysis pipeline in `pipeline/analyze_basic.py`; the per-passage features in `results_v9/passages.csv`. The notebook `pipeline/stylometric_pipeline.ipynb` is provided for users who prefer a Colab-based workflow. Running the analysis end-to-end takes under a minute on a laptop.

## References

- Asein, S. O. (1999). "Nigerian Poetry in English: A New Voice for the New Age."
- Biber, D. (1988). *Variation across Speech and Writing.* Cambridge University Press.
- Burrows, J. (2002). "Delta: A Measure of Stylistic Difference and a Guide to Likely Authorship." *Computers and the Humanities* 36: 267–279.
- Mosteller, F., & Wallace, D. L. (1964). *Inference and Disputed Authorship: The Federalist.* Addison-Wesley.
- Sule Egya, E. E. (2014–2022). Various essays and poems published in *African Writer*, *Shamsrumi*, *Springs-RCC*, *lyrikline.org*.
- Toyin Shittu. (2024–2025). Various articles published in *BJHSS*, *Prague Journal of English Studies*, *Brittlepaper*, *Daily Trust*, *This Age*.
