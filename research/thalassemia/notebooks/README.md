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

- `2026-04-27-ahsp-buffer-gate.ipynb` - computational evidence gate that keeps
  `AHSP` as an optional alpha-globin-buffer readout, not a standalone therapy
  lead.
- `2026-04-27-alpha-globin-rebalancing-gate.ipynb` - computational evidence
  gate that promotes direct alpha-globin reduction as a chain-balance benchmark
  and assay gate, not a first affordable treatment lead.
- `2026-04-27-ampk-nrf2-expansion-gate.ipynb` - computational evidence gate
  for the `AMPKB1` / `NRF2` expansion lane, including metformin as a
  translational warning comparator.
- `2026-04-27-candidate-score-sensitivity.ipynb` - stress test for the first
  candidate scoring table.
- `2026-04-27-dual-readout-panel-prioritizer.ipynb` - computational experiment
  that re-checks the first lab-quote panel against dual HbF plus
  alpha-globin/autophagy readouts.
- `2026-04-27-delta-globin-hba2-gate.ipynb` - computational evidence gate that
  keeps `HBD` / delta-globin / HbA2 induction as an advanced compensation
  benchmark and assay expansion gate, not a first treatment lead.
- `2026-04-27-first-wet-lab-panel-optimizer.ipynb` - computational experiment
  that chooses a small first lab-panel candidate set by required assay coverage.
- `2026-04-27-mechanism-gap-matrix.ipynb` - computational literature-mapping
  experiment comparing broad component evidence with the fully integrated
  Nakafa Lab research gap.
