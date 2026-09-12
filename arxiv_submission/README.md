# arXiv submission bundle

This is the submission bundle for arXiv cs.CL.

## Files

- `paper.tex` — Pandoc-generated LaTeX source
- `paper.pdf` — Generated PDF for first-submission use (if not generating LaTeX-built PDF locally)
- `paper.md` — Markdown source (in parent directory)

## Metadata for arXiv submission form

Title:
  Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets

Authors:
  Rabiu Raji

Abstract:
  The era of fluent large language models has destabilised a long-standing assumption in authorship attribution: that a writer's surface features are difficult to imitate at scale. We test that assumption against two contemporary Nigerian poets, Sule Egya (E.E. Sule) and Toyin Shittu, whose published work spans poetry, critical prose, and academic articles from 2009 to 2025. The corpus is public. Sixteen human passages (7,151 words) and sixteen LLM imitations (2,623 words) were produced across two free-tier models (nex-agi/nex-n2.5-mini and nex-nagi/nex-n2.5-pro via OpenRouter). Stylometric features per passage include sentence length distribution, type-token ratio, mean word length, punctuation density, function-word ratio, and a vowel-group syllable estimate. Across both authors the LLM imitations show measurably higher type-token ratio (lexical diversity) and lower mean syllables per word than the human originals. For Egya, human TTR is 0.59 against LLM 0.77; syllables drop from 1.65 to 1.44. For Shittu, human TTR is 0.54 against LLM 0.64; syllables drop from 1.94 to 1.73. The lexical signature holds across both authors and both models. We argue that these signals support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, while acknowledging the scope-bound constraints: a 16-passage corpus per condition and two LLM providers tested. A larger multi-model evaluation is future work.

Primary category: cs.CL (Computation and Language)

Secondary categories (optional): cs.DL (Digital Libraries), stat.AP (Applied Statistics)

Comments:
  16 pages, 11 figures/tables total in v9

MSC classes: I.2.7 (Natural Language Processing), I.5.4 (Applications), K.4.0 (Computers and Society)

ORCID: 0009-0007-8968-8620

License: arXiv non-exclusive license to distribute (default)

## Steps

1. Login to arxiv.org
2. Click "Submit" → cs.CL
3. Upload `paper.pdf` (or `paper.tex` for source submission)
4. Paste abstract into abstract field
5. Confirm metadata
6. If endorsed: submit. If not yet: click "Submit" → system will give endorsement request link to send to a cs.CL author.

## Repository

https://github.com/Rawbeew/nigerian-forensic-stylistics
