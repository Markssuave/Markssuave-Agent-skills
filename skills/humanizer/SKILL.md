---
name: humanizer
description: >-
  Rewrites AI-sounding prose and documentation to read with natural, human cadence without altering core facts.
---

<what-to-do>

## Objective
Strip predictable statistical artifacts, rhetorical clichés, and synthetic "AI tells" from text. Restore human rhythm, varied sentence lengths, and direct, confident tone without modifying facts, metrics, technical constraints, or author intent.

## The Multi-Pass Execution Loop
Whenever invoked on a target text, draft, or file, execute these four passes in order:

### 1. Catalog Scan (Detect Tells)
Scan the source text and identify patterns from the **Anti-Pattern Taxonomy** below. Rank them mentally from strongest tells (e.g. forced triads, false grandeur) to subtle tells (e.g. em-dash crutches, copula avoidance).

### 2. Root-Level Rewrite (Reconstruct from Scratch)
Do **not** perform superficial word-swaps or regex-style synonym replacements. Discard the rigid syntactic skeleton of the flawed sentence. Reconstruct each idea from scratch using direct active voice, authentic conversational pacing, and deliberate rhythm variation (mixing short punchy clauses with longer explanatory sentences).

### 3. Self-Critique Pass (The AI Mirror)
Inspect the generated rewrite and ask:
> *"If an experienced human editor read this, what remaining phrasing or transitions would tip them off that an LLM drafted it?"*
Prune any residual hedging, synthetic cheerleading, or formulaic summary closers.

### 4. Semantic Fidelity Audit (Zero Hallucination Gate)
Cross-reference the rewritten text against the original source:
- Verify that **100% of core facts, numbers, dates, technical claims, and author arguments** are preserved.
- Ensure no new claims or external opinions were hallucinated.
- If the original contained an explicit technical distinction, ensure the rewrite did not blur it for stylistic flair.

---

## Engineering Safeguards (Strict Exclusions)
When processing technical documentation, READMEs, or architectural records:
1. **Never alter code blocks or inline code**: Everything inside backticks (``` or `) is immutable.
2. **Never alter RFC 2119 imperatives**: `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHOULD`, `RECOMMENDED`, `MAY` must remain exact.
3. **Never randomize domain terminology**: In code contracts and API docs, identical repetition is a virtue. Do not introduce varied synonyms for strict architectural terms (e.g. do not alternate between "token", "ticket", and "credential" if the API strictly uses "token").
4. **Never rewrite file paths or URLs**.

</what-to-do>

<supporting-info>

## Anti-Pattern Taxonomy & Corrections

### 1. Forced Parallel Triads ("The Rule of Three")
- **The Tell**: Grouping items into rigid triplets because probabilistic language models naturally cluster three items.
- **Bad (AI)**: *"The architecture is robust, scalable, and intuitive."*
- **Correction**: Break the formula. Use one strong adjective, a pair, or an uneven structure: *"The architecture scales well without requiring complex configuration."*

### 2. False Grandeur & Unearned Significance
- **The Tell**: Elevating ordinary facts into epochal milestones using hyperbolic, breathless framing.
- **Trigger Phrases**: *"stands as a testament to"*, *"pivotal role"*, *"serves as a cornerstone"*, *"a rich tapestry of"*, *"delve into"*, *"beacon of"*.
- **Bad (AI)**: *"This cache implementation stands as a testament to efficient memory management."*
- **Correction**: Be direct and factual: *"This cache reduces memory consumption by 30%."*

### 3. Copula Avoidance & Weak Verbs
- **The Tell**: Using verbose periphrastic verbs instead of direct copulas (*is*, *are*, *has*).
- **Trigger Phrases**: *"serves to provide"*, *"functions as a mechanism for"*, *"acts as an interface"*, *"represents a shift"*.
- **Bad (AI)**: *"The service serves as a bridge between Redis and PostgreSQL."*
- **Correction**: *"The service bridges Redis and PostgreSQL."* or *"The service connects Redis to PostgreSQL."*

### 4. Throat-Clearing & Staged Run-Ups
- **The Tell**: Padded transitional phrases at the start of paragraphs that add zero informational value.
- **Trigger Phrases**: *"In today's fast-paced digital world..."*, *"It is important to remember that..."*, *"When it comes to..."*, *"At its core..."*, *"Needless to say..."*.
- **Correction**: Delete the opener entirely. Start with the actual subject and action.

### 5. Theatrical Contrast Framing
- **The Tell**: Formulaic dramatic setup pairing negative or limited clauses with glowing expansions.
- **Trigger Phrases**: *"Not only X, but also Y"*, *"It's not just a tool; it's a movement"*, *"Far from being a simple bug, it was..."*.
- **Correction**: State both facts plainly: *"It handles logging and automates rollback."*

### 6. Em-Dash Overuse & Punctuation Crutches
- **The Tell**: Chronically deploying em-dashes (`—`) in every paragraph to simulate artificial nuance and conversational pause.
- **Correction**: Use standard periods and commas. If a thought is tangential, make it a separate sentence or cut it.

### 7. Formulaic Closers & Summary Sentences
- **The Tell**: Tacking a synthetic philosophical wrap-up onto the end of a section.
- **Trigger Phrases**: *"Ultimately, the journey has just begun."*, *"Only time will tell, but one thing is clear."*, *"As we look to the future..."*.
- **Correction**: Conclude immediately after the final factual point. Stop speaking when the information ends.

---

## Voice Calibration (Optional)
If the user provides 2–3 paragraphs of their own authentic writing before invoking the skill:
1. Analyze their typical sentence length distribution (e.g. short/clipped vs. layered/academic).
2. Note their punctuation preferences (e.g. semicolon tolerance, parenthetical usage).
3. Calibrate the rewrite to reflect their personal vocabulary and cadence while enforcing the catalog protections.

</supporting-info>
