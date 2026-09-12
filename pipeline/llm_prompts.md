# LLM Generation Prompts

This file documents the prompt conditions used to generate LLM imitations of the two authors in the corpus. Used in Colab Cell 3 of the stylometric pipeline.

## Configuration

- **Models:** Two OpenRouter models: `nex-agi/nex-n2.5-mini` and `nex-agi/nex-n2.5-pro`
- **Per model × per author:** 4 passages per author per model
- **Total synthetic passages:** 2 models × 2 authors × 4 = 16
- **Generation parameters:** temperature 0.01 (near-deterministic), top-p 1.0, max_tokens ~750

## Prompt Conditions

### P1 — Author-specific imitation

```
Write a 250-word literary passage in the style of {author_name},
a contemporary Nigerian poet/writer. Capture the typical sentence
rhythm, vocabulary, and thematic preoccupations of their published
work as documented in the corpus.
```

### P2 — Topic-seeded imitation

For each author, an exemplar passage from the corpus is provided; the
LLM is asked to write a passage on the same topic in the same author's
style. Used for Egya and Shittu separately.

```
You are given an example passage in the style of {author_name}.
Write a new 250-word passage on {topic_seed}, keeping the same
sentence rhythm, vocabulary level, and cultural register as the
example.
```

## Per-Author Specifications

### Sule Egya (E.E. Sule)

- Themes: environmental degradation, Niger Delta politics, national
  identity, communal land, Tiv and Igbo cultural vocabulary
- Style: dense figurative language, nature imagery, mid-paragraph
  rhythm shifts, embedded Igbo and Yoruba terms (chi, ala, ndi, ile)
- Reference works: *Crippled Earth*, *Stateless Bay*, *Nation, Power
  and Dissidence*, *Threshing the Grains*

### Toyin Shittu

- Themes: Nigerian civil war memory, japa, migration, academic
  discourse on metaphor, post-2020 disillusionment
- Style: academic register, mid-length sentences, critical-theoretical
  vocabulary, ironic tone
- Reference works: *Metaphor in Nigerian Civil War Poetry*, ANA 2025
  shortlist coverage

## Implementation

See `stylometric_pipeline.ipynb` Cell 3 for the implementation. The
`generate()` function tries each model in order:

```python
def generate(prompt, model="nex-n2.5-mini"):
    """Try the requested model via OpenRouter."""
    return call_openrouter(prompt, model)
```

## Rate Limiting

- OpenRouter free tier: 20 requests/minute
- Set `time.sleep(0.5)` between requests to avoid rate limit issues

## Cost

OpenRouter free tier is sufficient for 16 generations. Cost: $0.00.

## Output

Generated passages are saved to `corpus/synthetic/` with corresponding
metadata in `corpus/synthetic_metadata.csv`. Columns:

- `id` (synth_001, etc.)
- `author` (egya or shittu)
- `model` (nex-n2.5-mini or nex-n2.5-pro)
- `topic_seed` (the seed used for that passage)
- `text` (the generated passage)
- `generation_timestamp` (ISO format)
