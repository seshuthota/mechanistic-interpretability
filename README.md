# Mechanistic Interpretability Learning Project

Structured 12-18 month journey to expert-level mechanistic interpretability following the roadmap in `deep-research-report.md`.

## Project Structure

- `notebooks/` - Jupyter notebooks for experiments and replication
- `src/` - Utility functions and helper code
- `experiments/` - Organized by month, containing code and results for each milestone
- `logs/` - Experiment logs and outputs
- `papers/` - Key reference papers (already populated)
- `docs/` - Additional documentation and write-ups

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Note: On Python 3.12+, `ecco` is skipped automatically due to upstream dependency constraints.

2. Start with Month 1 notebook:
   ```bash
   jupyter notebook notebooks/01_activation_inspection.ipynb
   ```

## Roadmap

See `deep-research-report.md` for detailed monthly milestones and exit criteria.

For immediate execution, use:
- `docs/roadmap-12-weeks.md` - Concrete week-by-week curriculum and deliverables
- `docs/notebook-checklist.md` - Quality gate for notebook completion
- `templates/experiment-template.md` - Standard experiment notes template

For pre-paper foundations, start with:
- `docs/foundations/00_required-concepts.md` - Quick walkthrough of must-know MI concepts
- `docs/foundations/01_concept-mastery-checklist.md` - Readiness checklist before paper deep-dives
- `notebooks/00_concepts_quickstart.ipynb` - Lightweight practical concept notebook

## Citation

If you use this work, please cite the original sources referenced in the roadmap.
