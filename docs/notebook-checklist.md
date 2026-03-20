# Notebook Checklist (Mechanistic Interpretability)

Use this checklist before marking a notebook complete.

## Setup

- [ ] Notebook title includes task and date.
- [ ] Model name/version is declared.
- [ ] Random seed(s) are fixed and shown.
- [ ] Required packages and versions are recorded.

## Data/Prompts

- [ ] Prompt/task generator is explicit and reproducible.
- [ ] Clean/corrupt split is clearly defined (if used).
- [ ] Example inputs are saved.

## Method

- [ ] Hook points/intervention sites are explicitly named.
- [ ] Metric definitions are written before results.
- [ ] Baselines are present (`clean`, `corrupt`, and/or `ablated`).

## Results

- [ ] Main table includes `logit_diff`, `recovery_score`, and/or `ablation_drop`.
- [ ] At least one visualization is paired with numeric evidence.
- [ ] Results include at least 3 seeds or a reason for single-seed.

## Validity Checks

- [ ] At least one robustness check is included.
- [ ] At least one failure case is documented.
- [ ] Alternative explanation is considered.

## Conclusion

- [ ] Claim is stated in one sentence.
- [ ] Evidence supporting claim is listed.
- [ ] Limitations are listed.
- [ ] Next experiment is specified.

## Artifact Output

- [ ] Notebook runs top-to-bottom from clean kernel.
- [ ] Result artifacts saved to `experiments/...` or `logs/...`.
- [ ] Short summary added to experiment `notes.md`.
