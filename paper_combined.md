# Voice or Mask? Abstract + One-Page Summary

**Authors:** Rabiu Raji (ORCID [0009-0007-8968-8620](https://orcid.org/0009-0007-8968-8620))


**Date:** September 2026

**Repository:** <https://github.com/Rawbeew/nigerian-forensic-stylistics>

**Status:** Preprint
**DOI:** 10.5281/zenodo.22725022 (https://zenodo.org/records/22725022)

---

## Abstract

The era of fluent large language models has destabilised a long-standing assumption in authorship attribution: that a writer's surface features are difficult to imitate at scale. This paper tests that assumption against two contemporary Nigerian poets, Sule Egya (E.E. Sule) and Toyin Shittu, whose published work spans poetry, critical prose, and academic articles from 2009 to 2025. The corpus is public. Sixteen human passages (7,151 words) and sixteen LLM imitations (2,623 words) were produced across two free-tier models (nex-agi/nex-n2.5-mini and nex-nagi/nex-n2.5-pro via OpenRouter). Stylometric features per passage include sentence length distribution, type-token ratio, mean word length, punctuation density, function-word ratio, and a vowel-group syllable estimate. Across both authors the LLM imitations show measurably higher type-token ratio (lexical diversity) and lower mean syllables per word than the human originals. For Egya, human TTR is 0.59 against LLM 0.77; syllables drop from 1.65 to 1.44. For Shittu, human TTR is 0.54 against LLM 0.64; syllables drop from 1.94 to 1.73. The lexical signature holds across both authors and both models. I argue that these signals support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, while acknowledging the scope-bound constraints: a 16-passage corpus per condition and two LLM providers tested. A larger multi-model evaluation is future work.

---

## One-Page Summary

### The question

When LLMs produce text that reads like a particular author, what survives of authorship forensics? Surface features (sentence rhythm, vocabulary, paragraph shape) are now reproducible by any fluent model. The deeper question is whether anything measurable in the output still distinguishes machine imitation from the author it imitates.

### What I did

Built a public corpus of 16 published passages by two contemporary Nigerian poets (7,151 words) and generated 16 LLM imitations (2,623 words) using two free-tier models (nex-agi/nex-n2.5-mini and nex-nagi/nex-n2.5-pro via OpenRouter). Each model received the same per-author system prompt describing documented stylistic markers and a single short exemplar passage. The imitations are stored alongside the human corpus and the analysis pipeline; everything is reproducible from `pipeline/analyze_basic.py`.

### What I measured

Nine lightweight stylometric features per passage: type-token ratio, mean syllables per word, sentence length distribution, mean word length, punctuation density, function-word ratio. Pure-stdlib, no external NLP dependencies.

### What I found

Across both authors, LLM imitations show **higher type-token ratio** (lexical diversity) and **lower mean syllables per word** (avoidance of polysyllabic vocabulary) than the human originals.

| Group | TTR | syllables / word |
|---|---|---|
| Egya human | 0.59 | 1.65 |
| Egya LLM | **0.77** | **1.44** |
| Shittu human | 0.54 | **1.94** |
| Shittu LLM | 0.64 | 1.73 |

The lexical signature is consistent across both authors and both LLM providers.

### What this means

LLMs produce surface-plausible literary text: imagery, allusion, Nigerian cultural reference points, rhythm. But the lexical strategies differ. Human authors choose words for density and weight. LLMs choose words for variety. The result is text that reads well in isolation but reveals its source under stylometric pressure.

The cultural-density asymmetry is also a finding. Egya deploys 47 Igbo and Yoruba terms across his corpus (chi, ala, ndi, ile, ife, omo, ola, ifa). Shittu's academic corpus contains none. The LLM imitations did not fully replicate Egya's cultural-idiom embedding.

### What this does NOT claim

- The corpus is 16 passages per condition. Small.
- Two LLM providers tested. Same model family.
- The features used are deliberately lightweight; Biber (1988) feature set and Burrows' (2002) Delta method would likely produce additional discriminative signals.
- "Bonferroni survives at α = 0.05" is verified by t-statistic magnitude, but effect-size confidence intervals require a larger corpus.

### Why this paper is interesting

1. **Methodology is portable.** The pipeline works on any author pair in any language. The 9-feature lightweight set is faster and more reproducible than Biber's full feature set.
2. **Free-tier reproducible.** No paid APIs. No private data. Two free models on OpenRouter. Anyone can rerun this for any target author.
3. **Two distinct cultural profiles.** Egya (literary-cultural vocabulary) and Shittu (academic-theoretical vocabulary) test different parts of LLM imitation. The lexical signature generalises across both.
4. **Negative result for LLM detection tools.** Liang et al. (2023) and Weber-Wulff et al. (2023) showed GPT detectors fail on non-native English writing. Our work shows that **even on fluent native-register literary text**, the machine origin is detectable via basic stylometry. This matters because the current discourse around AI detection has focused on commercial detectors, not the forensic-stylometry question.

### What I would value from a reviewer

- Whether 16 passages per condition is too small for the effect-size claim
- Whether the two-model-family limitation undermines external validity
- Whether a more rigorous feature set (Biber, Burrows Delta) would change the headline finding
- Whether the cultural-density cataloguing (Igbo/Yoruba terms per author) is a useful contribution or anecdotal

### Data and code

- `corpus/`: 16 human `.txt` files + `metadata.csv`
- `corpus/llm/`: 16 LLM imitations
- `pipeline/analyze_basic.py`: feature extractor
- `pipeline/generate_llm_imitations.py`: LLM generator
- `results_v9/passages.csv` and `summary.json`: full results
- `paper_v9.md`: full paper
