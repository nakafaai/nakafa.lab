# Finding: First Wet-Lab Panel Optimizer Result

Date checked: 2026-04-27
Evidence label: computational experiment, not wet-lab evidence

## Working Conclusion

The first computational lab-panel optimizer selected a five-item pilot panel
that covers the required first-pass assay questions:

1. hydroxyurea;
2. purified resveratrol;
3. sirolimus;
4. standardized 6-shogaol-rich ginger extract;
5. melittin hazard control.

This is not a biological result. It is a lab-quote design result: the smallest
panel that still covers positive HbF control, HbF seed testing against
HPFH-like readouts, autophagy/alpha-globin cleanup, red-cell support or
metabolism, and hemolysis hazard calibration.

## Why These Five

| Candidate | Role in first quote panel | Boundary |
| --- | --- | --- |
| Hydroxyurea | positive HbF comparator | comparator only; not a new Nakafa Lab cure |
| Purified resveratrol | HbF seed tested against HPFH-like readouts | seed only; requires endogenous HbF and safety replication |
| Sirolimus | mTOR/autophagy/alpha-globin cleanup comparator | immune-active, access-limited, monitor-only comparator |
| Standardized 6-shogaol-rich ginger extract | red-cell support comparator | support endpoint only, not an HbF or cure claim |
| Melittin hazard control | hemolysis rejection threshold | hazard calibration only, not a therapy candidate |

## What Was Deferred

- `T-BDMC`-like curcuminoid analog remains interesting but was deferred from the
  smallest panel because exact procurement identity and batch-control work can
  add friction.
- Mitapivat or a pyruvate-kinase activator reference remains scientifically
  strong, but should be added only if the lab can legally and practically obtain
  it.

## Decision

Use this five-item set as the first lab-outreach quote package. If a lab can
handle a larger panel, add `T-BDMC`-like curcuminoid analog and a pyruvate
kinase activator reference as expansion items.

## Required Readouts

- `HBG1` / `HBG2` messenger RNA;
- HbF protein;
- F-cell percentage;
- alpha/non-alpha globin balance;
- `ULK1`, p62 / `SQSTM1`, and autophagy readouts for sirolimus;
- erythroid maturation;
- viability and apoptosis;
- mature red-cell hemolysis.

## Sources

- [First wet-lab panel optimizer notebook](../notebooks/2026-04-27-first-wet-lab-panel-optimizer.ipynb)
- [First HbF and red-cell safety assay work order V0](../assays/2026-04-27-first-assay-work-order-v0.md)
- [Candidate scoring V0](../prioritization/2026-04-27-candidate-scoring-v0.md)
- [Experiment status boundary](2026-04-27-experiment-status-boundary.md)
