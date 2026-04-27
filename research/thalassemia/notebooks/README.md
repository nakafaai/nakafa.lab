# Research Notebooks

This folder stores small reproducible experiments that are easier to inspect as
notebooks than as prose-only notes.

Rules:

- keep notebooks source-backed and small;
- do not commit private patient data or raw clinical records;
- clear large outputs before commit;
- move durable conclusions into `findings/`, `prioritization/`, or the paper;
- run the notebook top-to-bottom when the environment allows.

Current notebooks:

- `2026-04-27-candidate-score-sensitivity.ipynb` - stress test for the first
  candidate scoring table.
- `2026-04-27-first-wet-lab-panel-optimizer.ipynb` - computational experiment
  that chooses a small first lab-panel candidate set by required assay coverage.
