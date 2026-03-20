# 12-Week Mechanistic Interpretability Roadmap

Start date: 2026-03-20  
Cadence: 8-12 hrs/week  
Weekly rhythm:
- Day 1-2: reading + hypothesis design
- Day 3-4: implementation
- Day 5: runs + debugging
- Day 6: write-up + robustness checks
- Day 7: backlog grooming and next-week prep

## Working Rules (Non-Negotiable)

- Every claim needs at least one intervention-based check.
- Every experiment run logs seed, model, data/prompt generator, and metric definition.
- Every week ends with a short written conclusion: what changed in your beliefs and why.
- No "pretty plot only" weeks. At least one measurable causal test each week from Week 3 onward.

## Milestones

- Milestone 1 (end Week 2): You can explain residual stream, heads, MLPs, superposition, circuits, and causal vs correlational evidence.
- Milestone 2 (end Week 4): You can inspect activations and attention, and run ablations + activation patching on a small model.
- Milestone 3 (end Week 8): You have reproduced at least one canonical result with your own metrics and caveats.
- Milestone 4 (end Week 10): You have completed one feature-level (SAE) investigation with causal probes.
- Milestone 5 (end Week 12): You have one original mini-project with robustness checks and a defensible conclusion.

## Standard Metrics Pack (Use Throughout)

- `logit_diff`: logit(correct_token) - logit(foil_token)
- `recovery_score`: (patched - corrupt) / (clean - corrupt)
- `ablation_drop`: metric(clean) - metric(ablated)
- `stability`: mean ± std across >=3 seeds

Use this same pack across most experiments so comparisons stay meaningful.

## Week-by-Week Plan

## Week 1 - Foundations and Environment

Focus:
- Set up environment and repo workflow.
- Build conceptual map.

Read:
- Transformer Circuits framework (core sections).

Build:
- One notebook: activation cache smoke test on GPT-2 small.

Deliverables:
- Concept notes for residual stream, attention read/write, MLP features.
- `notebooks/01_activation_inspection.ipynb` (or equivalent).
- First run log in `logs/`.

Exit criteria:
- You can run cache capture twice and get consistent summary stats.

## Week 2 - Causal Thinking + Basic Readouts

Focus:
- Define metrics before interventions.

Read:
- Induction heads (selected sections).
- One short piece on saliency/attention caveats.

Build:
- Metrics notebook with `logit_diff` and task accuracy on templated prompts.
- Optional baseline logit lens view.

Deliverables:
- `notebooks/02_metrics_and_readouts.ipynb`
- `docs/metric-definitions.md`

Exit criteria:
- Metrics are stable across reruns and you can justify why each metric is used.

## Week 3 - Ablations and Activation Patching

Focus:
- First serious interventions.

Read:
- Activation patching best-practices paper/post.

Build:
- Clean/corrupt prompt pairs.
- Single-site patching heatmap across layers/heads.
- Head ablation sweep.

Deliverables:
- `notebooks/03_ablation_and_patching.ipynb`
- Heatmap figures + run artifacts.

Exit criteria:
- You can show at least one behavior where interventions produce expected directional effects.

## Week 4 - Attribution Patching and Failure Modes

Focus:
- Compare intervention methods and inspect disagreements.

Read:
- Attribution patching reference material.

Build:
- Attribution patching run on same behavior from Week 3.
- Side-by-side comparison with activation patching.

Deliverables:
- `notebooks/04_attribution_vs_activation_patching.ipynb`
- Short memo: where methods disagree and likely reasons.

Exit criteria:
- You have one documented failure mode and one mitigation idea.

## Week 5 - Reproduction Target 1 (Induction/Copy)

Focus:
- Full mini-replication with your own pipeline.

Read:
- Induction/copy mechanism write-ups.

Build:
- Reproduce a basic induction/copy localization result.
- Validate with at least one ablation + one patching confirmation.

Deliverables:
- `experiments/week05_induction_replication/`
- Reproduction report draft.

Exit criteria:
- Claim + evidence + caveats are written clearly and backed by artifacts.

## Week 6 - Robustness Pass on Target 1

Focus:
- Stress-test your own conclusion.

Build:
- Prompt distribution shift tests.
- Noise/corruption scheme sensitivity checks.
- Seed sweep.

Deliverables:
- Robustness table with pass/fail per check.

Exit criteria:
- You can state exactly where the explanation generalizes and where it breaks.

## Week 7 - Reproduction Target 2 (IOI-Style Localization)

Focus:
- Larger, structured replication.

Read:
- IOI circuit paper sections on evaluation.

Build:
- IOI-style prompt set.
- Circuit localization using patching/ablation.

Deliverables:
- `experiments/week07_ioi_replication/`
- Metrics table (`faithfulness/completeness` proxies).

Exit criteria:
- Reproduction obtains qualitatively similar pattern to reference, with your own limitations documented.

## Week 8 - Path-Level Reasoning

Focus:
- Move from components to paths.

Read:
- Path patching paper.

Build:
- Minimal path patching analysis on known behavior.

Deliverables:
- Ranked causal path list and effect-size chart.

Exit criteria:
- Compact path subset explains meaningful share of behavioral effect.

## Week 9 - Feature-Based Interpretability (SAE Intro)

Focus:
- Shift from neurons/heads to sparse features.

Read:
- Monosemanticity + one SAE implementation resource.

Build:
- Load a pretrained SAE or train a small one on cached activations.
- Inspect top-activating tokens/contexts for selected features.

Deliverables:
- `notebooks/09_sae_feature_exploration.ipynb`
- Feature cards (at least 10).

Exit criteria:
- You can identify at least 3 features with coherent interpretations.

## Week 10 - Causal Tests on Features

Focus:
- Test whether feature interpretations matter behaviorally.

Build:
- Feature interventions (activate/suppress/edit).
- Measure `logit_diff` and task deltas under interventions.

Deliverables:
- `experiments/week10_sae_causal_tests/`
- Feature-level causal effect table.

Exit criteria:
- At least one feature has measurable, repeatable causal impact.

## Week 11 - Original Mini-Project (Design + Run)

Focus:
- Form and test your own hypothesis.

Examples:
- Compare mechanism differences across two model sizes.
- Test whether a claimed circuit survives quantization or light fine-tuning.

Build:
- Register hypothesis, protocol, and evaluation criteria before running.

Deliverables:
- `experiments/week11_original_project/`
- Pre-registered-style plan doc + initial results.

Exit criteria:
- Hypothesis is testable and experiment execution is reproducible.

## Week 12 - Consolidation and Write-Up

Focus:
- Defensible report, not just notebooks.

Build:
- Final report with claim/evidence/limitations.
- Re-run key figure from clean environment once.

Deliverables:
- `docs/12-week-report.md`
- Repro checklist completed.
- Prioritized backlog for next 12 weeks.

Exit criteria:
- Third party could rerun your main result from docs + scripts.

## Quality Bar for "Completed"

A week is complete only if all are true:
- Notebook runs top-to-bottom.
- Metrics table saved as artifact.
- At least one caveat/failure mode documented.
- Next action logged.

## Suggested Folder Convention

- `experiments/weekXX_<name>/config.yaml`
- `experiments/weekXX_<name>/run.py`
- `experiments/weekXX_<name>/results.json`
- `experiments/weekXX_<name>/notes.md`

Keep exploratory notebooks in `notebooks/`, but move stable experiment logic into `experiments/` scripts.
