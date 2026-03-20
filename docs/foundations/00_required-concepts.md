# Required Concepts Before Reading Mechanistic Interpretability Papers

This is the minimum concept set you should be comfortable with before diving into papers.

## 1) Residual Stream (Core Object)

What it is:
- The shared vector "workspace" that almost all components read from and write to.

Why it matters:
- Most mechanistic explanations are about which components write what information into the residual stream, and where that information is later read.

You should know:
- Shape intuition: `[batch, position, d_model]`
- Additive updates from attention and MLP blocks

## 2) Attention Heads as Read-Write Programs

What it is:
- A head computes attention weights (QK) and writes transformed values (OV) back to the residual stream.

Why it matters:
- Many canonical circuits are head-level mechanisms (e.g., induction-like behavior).

You should know:
- Q, K, V roles
- Attention pattern vs causal importance are different things

## 3) MLP Layers as Feature Computers

What it is:
- MLPs apply nonlinear transformations that often create or sharpen useful features.

Why it matters:
- Circuits are not only attention; many behaviors need MLP-computed features.

You should know:
- MLP outputs are also residual-stream writes
- Neurons are often polysemantic, so neuron-level stories can be incomplete

## 4) Unembedding and Logits

What it is:
- The unembedding maps final residual states to token logits.

Why it matters:
- Mech interp often measures impact via logits (e.g., logit difference).

You should know:
- `logit_diff = logit(correct) - logit(foil)`
- Why logit-space metrics are preferred over only visual intuition

## 5) Superposition and Polysemanticity

What it is:
- Models can represent multiple concepts in overlapping directions/subspaces.

Why it matters:
- Explains why single-neuron interpretations often fail and why feature methods (SAEs) became important.

You should know:
- "one neuron = one concept" is usually too simplistic

## 6) Correlation vs Causation

What it is:
- Correlational evidence: patterns/probes/heatmaps
- Causal evidence: interventions that change behavior predictably

Why it matters:
- Mechanistic claims should primarily rely on causal tests.

You should know:
- Why attention maps and saliency can mislead
- Why ablation/patching are central

## 7) Core Intervention Methods

- Ablation: remove or zero component output to test necessity
- Activation patching: replace activations from corrupted run with clean run at specific sites
- Attribution patching: gradient/attribution-based approximations to prioritize sites
- Path patching: test causal contribution of specific computational paths

You should know:
- What each method can and cannot prove

## 8) Evaluation Quality Bar

For a strong claim, ask:
- Faithfulness: does proposed mechanism actually track behavior?
- Completeness/sufficiency: can mechanism alone recover behavior?
- Necessity: removing it harms behavior?
- Robustness: does it hold under prompt/template changes and seeds?

## 9) Practical Tooling Hygiene

You should be able to:
- Hook named internal activations
- Cache and inspect tensors by shape and location
- Keep reproducible runs (seed, model/version, prompts, metric definitions)

## 10) How to Use This Before Papers

For each paper you read:
1. Map it to these concepts (which ones are central?)
2. Write claim/evidence/method in your own words
3. Do one small practical check in notebook
4. Log one caveat and one open question

---

## Minimal Readiness Checklist

You are ready to start papers when you can explain, from memory:
- residual stream as central communication channel
- attention/MLP as additive writes
- logit-diff style measurement
- superposition/polysemanticity motivation
- why intervention evidence beats visualization-only evidence
