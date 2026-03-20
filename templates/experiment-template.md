# Experiment Template

Use this template for each experiment in `experiments/weekXX_<name>/notes.md`.

## Metadata

- Experiment name:
- Date:
- Owner:
- Model:
- Tokenizer:
- Code commit/ref:
- Environment (Python + key libs):
- Seed(s):

## Hypothesis

State one testable claim.

Example:
"Head L5H3 contributes causally to IOI logit difference under templated prompts."

## Task and Data

- Task/behavior:
- Prompt/data source:
- Clean/corrupt construction:
- Inclusion/exclusion criteria:

## Method

- Primary method (e.g., activation patching):
- Secondary checks (e.g., ablation, seed sweep):
- Hook points:
- Intervention details:

## Metrics

- Primary metric:
- Secondary metrics:
- Success threshold (predefined):

Example:
- Primary: `recovery_score`
- Success threshold: mean recovery >= 0.4 over 3 seeds

## Results

Record numeric results first.

| Condition | Metric | Value |
|---|---|---:|
| clean | logit_diff | |
| corrupt | logit_diff | |
| patched | recovery_score | |
| ablated | ablation_drop | |

## Robustness and Sanity Checks

- Seed sweep results:
- Prompt distribution shift:
- Alternative corruption scheme:
- Negative control:

## Interpretation

- What supports the hypothesis?
- What weakens it?
- Most plausible alternative explanation:

## Decision

- [ ] Hypothesis supported
- [ ] Hypothesis partially supported
- [ ] Hypothesis not supported

## Next Actions

1.
2.
3.
