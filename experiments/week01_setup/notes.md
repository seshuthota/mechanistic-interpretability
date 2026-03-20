# Week 01 Setup - Notes

## Metadata

- Experiment name: week01_setup
- Date:
- Owner:
- Model: gpt2
- Seed(s): 42

## Hypothesis

Caching and inspecting a fixed residual-stream hook (`blocks.5.hook_resid_post`) is stable across repeated runs with fixed seed and prompt.

## Task and Data

- Task/behavior: activation inspection
- Prompt source: fixed manual prompt in config
- Clean/corrupt construction: not applicable

## Method

- Run model once with cache capture.
- Extract target hook tensor shape and summary statistics.
- Save results as JSON artifact.

## Metrics

- `resid_mean`
- `resid_std`
- `resid_l2`
- tensor shape

## Results

Fill after running `run.py`.

## Robustness and Sanity Checks

- Repeat run with same seed and confirm identical summary stats.

## Interpretation

- If stable, environment + basic hook pipeline are ready for Week 2.

## Next Actions

1. Add metrics notebook (`notebooks/02_metrics_and_readouts.ipynb`).
2. Add clean/corrupt prompt generator.
3. Define `logit_diff` baseline tables.
