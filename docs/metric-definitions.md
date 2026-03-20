# Metric Definitions

Use these exact definitions across experiments unless explicitly justified.

## `logit_diff`

Definition:
- `logit_diff = logit(correct_token) - logit(foil_token)`

Interpretation:
- Higher is better for the target behavior.

Notes:
- Keep `correct_token` and `foil_token` fixed per prompt template.
- Report mean and std across examples and seeds.

## `recovery_score`

Definition:
- `recovery_score = (metric_patched - metric_corrupt) / (metric_clean - metric_corrupt)`

Interpretation:
- `1.0`: full recovery to clean behavior
- `0.0`: no improvement over corrupt baseline
- `<0`: intervention hurt performance
- `>1`: over-recovery (can happen; inspect carefully)

Notes:
- Avoid divide-by-zero by excluding or flagging examples where clean equals corrupt.

## `ablation_drop`

Definition:
- `ablation_drop = metric_clean - metric_ablated`

Interpretation:
- Larger positive values indicate higher component necessity.

Notes:
- Report effect size and confidence interval when possible.
- Pair with negative-control ablations.

## `stability`

Definition:
- Aggregate variability across seeds:
- `stability = mean(metric) ± std(metric)` over >=3 seeds

Interpretation:
- Low variance supports robustness.

Notes:
- Keep seed list fixed for comparability.

## Reporting Standard

For every main result table include:
- sample size (`n_prompts`)
- seed count (`n_seeds`)
- metric mean
- metric std (or CI)
- brief caveat if any denominator/edge-case filtering is applied
