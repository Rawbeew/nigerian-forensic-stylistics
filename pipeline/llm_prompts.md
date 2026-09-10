# LLM Generation Prompts

This file documents the prompt conditions used to generate LLM imitations of the four authors in the corpus. Used in Colab Cell 3 of the stylometric pipeline.

## Configuration

- **Models:** GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, Llama 3-70B
- **Per model × per author:** 10 passages
- **Total synthetic passages:** 4 models × 4 authors × 10 = 160
- **Generation parameters:** temperature 0.7, top-p 1.0, max_tokens 750

## Prompt Conditions

### P1 — Generic style imitation

```
Write a 500-word literary fiction passage in the style of {author_name}, 
a contemporary Nigerian writer known for {author_genre}. Capture their 
typical sentence rhythm, vocabulary, and thematic preoccupations.
```

### P2 — Genre-specific imitation

For poets (Egya, Liam, Shittu):
```
Write 500 words of contemporary Nigerian poetry in the voice of {author_name}. 
Use their typical line lengths, imagery, and structural patterns. Aim for 
the rhythms and themes characteristic of their published work.
```

For Awaisu (novelist):
```
Write 500 words of contemporary Nigerian prose fiction in the voice of 
{author_name}, who writes about {themes}. Capture the novelistic texture 
and cultural setting characteristic of her published work.
```

### P3 — Themed free generation

```
Write 500 words of contemporary Nigerian literary prose about {theme}, 
in a style appropriate for a literary journal. Focus on the texture of 
ordinary Nigerian life and the tensions between tradition and modernity.
```

Themes (cycled through):
- migration and japa
- illness and resilience
- love and family
- rural-urban tension
- religion and identity

## Per-Author Author-Specific Prompt Extensions

### Maryam Awaisu
- Themes: women's rights in Northern Nigeria, sickle cell disease, conservative Muslim family dynamics
- Style: formal and colloquial mix, vivid imagery, complex sentences for introspection
- Reference works: *The Thing About Compromise*, *Burning Bright*, *Ms. Joana's Rules*

### Sule Egya / E.E. Sule
- Themes: environmental degradation, Niger Delta, political corruption, national identity
- Style: dense figurative language, nature imagery, protest undertones
- Reference works: *Sterile Sky*, *Makwala*, *What the Sea Told Me*, *Nation, Power and Dissidence*

### Paul Liam
- Themes: barracks life, Tiv culture, religion and ethnic polarization, emerging northern voices
- Style: compact lines, often direct, journalistic clarity
- Reference works: *Indefinite Cravings*, *Saint Sha'ade and Other Poems*

### Toyin Shittu
- Themes: japa, migration, national disillusionment, historical memory
- Style: time-spanning structure, metaphorical density, ironic tone
- Reference works: *Niger Blues and other Poems*, *The Crash*, *Japa: Elegy for Nigerians*

## Implementation

See `stylometric_pipeline.ipynb` Cell 3 for the implementation. The `generate()` function tries each provider in order:

```python
def generate(prompt, model="default"):
    """Try each provider in order until one works."""
    for fn, m in [
        (lambda p: generate_groq(p), "llama-3.1-70b"),
        (lambda p: generate_openrouter(p), "llama-3-70b"),
    ]:
        result = fn(prompt)
        if result:
            return result, m
    return None, None
```

## Rate Limiting

- Groq free tier: 30 requests/minute
- OpenRouter free tier: 20 requests/minute
- Set `time.sleep(0.5)` between requests to avoid rate limit issues

## Cost

All providers have free tiers sufficient for 160 generations. Estimated cost: $0.00.

## Output

Generated passages are saved to `pipeline/output/synthetic_corpus.csv` with columns:
- `id` (synth_P1_001, etc.)
- `prompt_id` (P1, P2, or P3)
- `author` (awaisu, egya, liam, or shittu)
- `model` (gpt-4o, claude-3.5, gemini-1.5, or llama-3-70b)
- `text` (the generated passage)
- `generation_timestamp` (ISO format)
- `seed` (random seed if available)
