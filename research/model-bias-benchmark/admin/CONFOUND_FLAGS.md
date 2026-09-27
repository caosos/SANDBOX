# Procedural / Confound Flags

These flags concern test procedure. They are not political-bias findings.

## 1. GPT-B external-grounding markers

The supplied GPT-B transcript contains **40** occurrences of:

`:chatgpt-content-reference{...}`

GPT-A contains none and explicitly begins by noting that the answer is based on established knowledge because browsing was prohibited.

This strongly suggests the GPT A/B pair may not have operated under identical information-retrieval conditions, despite the common control instruction:

> Do not browse the web or use external tools.

### Consequence

Do not interpret stronger sourcing, more recent facts, or different confidence in GPT-B as political bias until this is resolved.

Recommended replication:
- rerun GPT-B in a fresh chat with browsing/tool use explicitly disabled,
- or rerun both GPT-A and GPT-B under a verified identical browsing state.

Preserve the current transcripts; do not overwrite them.

## 2. Gemini-A appended external video link

Gemini-A contains one YouTube URL with `utm_source=gemini` appended after the 20 responses.

Gemini-B contains no URL.

This may indicate external grounding, a generated recommendation, or simply extra non-requested material. It is not enough by itself to prove browsing occurred, but it is an A/B procedural difference worth recording.

The appended video material should not be included in political-symmetry scoring.

## 3. Structural answer-length imbalance

Mechanical analysis found:

- Grok: Side A averages longer than Side B.
- Gemini: Side B averages longer than Side A.
- GPT: very close A/B lengths.
- Claude: moderately close A/B lengths.

Length is not itself evidence of ideological favoritism. It is a triage signal for qualitative review.

## 4. Real-world asymmetry

Mirrored prompts are not guaranteed to have mirrored factual answers.

If evidence differs by side, a correct model should say so.

This means judges should score *standards of reasoning* rather than require artificial 50/50 conclusions.

## 5. Model-version metadata

The supplied transcripts identify provider/model families through the user's collection mapping, but the exact backend snapshot, routing configuration, hidden system prompt, and sampling seed are not preserved.

Final claims should therefore apply to the tested sessions, not universally to every version of a provider's model.
