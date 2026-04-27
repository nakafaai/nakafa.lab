# Finding: Dual-Readout Panel Prioritizer Result

Date checked: 2026-04-27
Evidence label: computational experiment, not wet-lab evidence and not treatment advice

## Working Conclusion

The dual-readout prioritizer keeps the first lab-quote panel unchanged:

1. hydroxyurea;
2. purified resveratrol;
3. sirolimus;
4. standardized 6-shogaol-rich ginger extract;
5. melittin hazard control.

This result does not mean any item is a cure. It means the smallest first panel
still covers the required lab-design roles after the newer dual HbF plus
alpha-globin/autophagy assay spec was added.

## What The Prioritizer Tested

The notebook scored each candidate against:

- HbF or F-cell fit;
- alpha-globin cleanup fit;
- autophagy fit;
- erythroid maturation safety;
- mature red-cell hemolysis gate;
- identity and access;
- patient-boundary risk.

It then forced coverage of five roles that should not be blurred:

- positive HbF comparator;
- HbF seed for HPFH-like readouts;
- autophagy and alpha-globin cleanup comparator;
- red-cell metabolism or support comparator;
- hemolysis hazard boundary.

## Core Panel Decision

| Item | Why it remains in the core panel | Boundary |
| --- | --- | --- |
| Hydroxyurea | positive HbF comparator | comparator only, not a new cure claim |
| Purified resveratrol | low-friction natural-product HbF seed | screen seed only until endogenous HbF and safety replication |
| Sirolimus | autophagy and alpha-globin cleanup comparator | immune-active monitor-only comparator |
| Standardized 6-shogaol-rich ginger extract | red-cell support comparator | support endpoint only unless HbF and alpha-globin endpoints improve |
| Melittin hazard control | hemolysis rejection threshold | hazard calibration only, blocked from therapy framing |

## Expansion Logic

The highest-value expansion items are:

1. `AMPKB1` / `NRF2` pathway probe;
2. pyruvate kinase activator reference;
3. `T-BDMC`-like curcuminoid analog.

These are expansion lanes, not patient candidates. They should be added only if
a qualified lab can support the identity, procurement, alpha-globin, autophagy,
maturation, viability, and hemolysis gates.

## Research Decision

Use the five-item panel for first lab feasibility and pricing. Ask the lab
whether expansion items are practical, but keep the first quote small unless the
lab already has the required models, assays, and material controls.

Promotion remains blocked until wet-lab data show a useful HbF or F-cell signal
without worsening alpha-globin burden, maturation, viability, apoptosis, or
mature red-cell hemolysis.

## Sources

- [Dual-readout panel prioritizer notebook](../notebooks/2026-04-27-dual-readout-panel-prioritizer.ipynb)
- [Dual HbF and alpha-globin autophagy assay spec V0](../assays/2026-04-27-dual-hbf-alpha-autophagy-assay-spec-v0.md)
- [First wet-lab panel optimizer result](2026-04-27-first-wet-lab-panel-optimizer-result.md)
- [Candidate scoring V0](../prioritization/2026-04-27-candidate-scoring-v0.md)
- [AMPKB1 autophagy HbF bridge](2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [Pyruvate kinase red-cell metabolism benchmark](2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [T-BDMC identity resolution](2026-04-27-t-bdmc-identity-resolution.md)
- [Sirolimus ULK1 alpha-globin article, PMID 37894732](https://pubmed.ncbi.nlm.nih.gov/37894732/)
- [AMPKB1 HbF NRF2 article, PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
