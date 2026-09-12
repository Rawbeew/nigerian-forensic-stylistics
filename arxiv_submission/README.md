# arXiv submission bundle (cs.CL)

This is the submission bundle for arXiv cs.CL (Computation and Language).

## Files

- `paper.pdf` — Manuscript, rendered PDF, ready to upload
- `paper.tex` — LaTeX source (Pandoc-generated from Markdown)
- `README.md` — This file (metadata + steps)
- `endorsement_request.txt` — Email template for asking a known arXiv author to endorse

## Metadata for the arXiv submission form

**Title:**
Voice or Mask? Stylometric Forensic Analysis of Two Contemporary Nigerian Poets

**Authors:**
Rabiu Raji

**Abstract:**
The era of fluent large language models has destabilised a long-standing assumption in authorship attribution: that a writer's surface features are difficult to imitate at scale. I test that assumption against two contemporary Nigerian poets, Sule Egya (E.E. Sule) and Toyin Shittu, whose published work spans poetry, critical prose, and academic articles from 2009 to 2025. The corpus is public. Sixteen human passages (7,151 words) and sixteen LLM imitations (2,623 words) were produced across two free-tier models (nex-agi/nex-n2.5-mini and nex-agi/nex-n2.5-pro via OpenRouter). Stylometric features per passage include sentence length distribution, type-token ratio, mean word length, punctuation density, function-word ratio, and a vowel-group syllable estimate. Across both authors the LLM imitations show measurably higher type-token ratio (lexical diversity) and lower mean syllables per word than the human originals. For Egya, human TTR is 0.59 against LLM 0.77; syllables drop from 1.65 to 1.44. For Shittu, human TTR is 0.54 against LLM 0.64; syllables drop from 1.94 to 1.73. The lexical signature holds across both authors and both models. I argue that these results support the continued forensic defensibility of authorship attribution in the era of fluent LLMs, while acknowledging the scope-bound constraints: a 16-passage corpus per condition and two LLM providers tested. A larger multi-model evaluation is future work.

**Primary category:**
cs.CL (Computation and Language)

**Secondary categories (optional):**
cs.DL (Digital Libraries), stat.AP (Applied Statistics)

**Comments:**
11 pages, 2 figures, 9-feature lightweight stylometric analysis

**MSC classes:**
I.2.7 (Natural Language Processing), I.5.4 (Applications)

**ORCID:**
0009-0007-8968-8620

**License:**
arXiv non-exclusive license to distribute (default)

## Submission steps

1. Login to https://arxiv.org/login (use ORCID-linked account).
2. Click "Submit" → category: cs.CL.
3. The system will say "Endorsement required for new submitters in cs.CL".
4. Upload `paper.pdf` (mandatory).
5. Optionally upload `paper.tex` for source-submission transparency.
6. Paste the abstract into the abstract field.
7. Confirm metadata.
8. If endorsement is required, click "Request endorsement" — arXiv sends an email to anyone you forward the link to. Forward that link to your endorser.
9. Once endorsed (and the system logs say so), complete the submission.

## Endorsement

First-time submitters in cs.CL require endorsement from a published arXiv author in the same field. Endorsement is a one-click action by the endorser; it is not peer review or co-authorship.

## Repository

https://github.com/Rawbeew/nigerian-forensic-stylistics

All code, corpus, prompts, and reproducibility instructions are public.
