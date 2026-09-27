# Judge Handoff

Repository: `caosos/SANDBOX`

Branch: `model-bias-benchmark-2026-09-27`

Research root:

`research/model-bias-benchmark/`

## Give an independent judge these files only

1. `prompts/CONTROL.md`
2. `prompts/A.md`
3. `prompts/B.md`
4. `judging/RUBRIC.md`
5. `judging/JUDGE_PROMPT.md`
6. all eight files under `blind/`

Do **not** give the judge:
- `admin/BLIND_MAP.md`
- named files under `raw/`
- `analysis/INITIAL_COMPARISON.md`

until the judge has submitted its scores.

## Requested judge output

Save each judge's work as:

`analysis/judges/<judge-name>/scores.csv`

and

`analysis/judges/<judge-name>/report.md`

The scoring file should preserve all 20 pairs and all six rubric dimensions.

## After all judges finish

Aggregate:
- median score by pair and dimension,
- spread/disagreement by pair,
- policy-pair score,
- loaded-premise score,
- overall score,
- factual-verification flags.

Only then reveal candidate identities using `admin/BLIND_MAP.md`.

## Important

Do not ask a judge which political side it prefers.

The question is whether the tested responses use comparable reasoning standards across mirrored prompts.
