# Finding: Expansion Lane Decision Gate

Date checked: 2026-04-27
Evidence label: computational triage gate, not wet-lab evidence and not treatment advice

## Working Conclusion

The first expansion lane after the fixed quote panel should be an
`AMPKB1` / `NRF2` / `ULK1` / autophagy pathway probe, if a qualified lab can
source a defined research-grade probe and measure dual HbF plus
alpha-globin/autophagy readouts.

This is not a patient treatment claim. It is a research-planning decision:
prioritize the expansion lane that best connects fetal hemoglobin induction,
alpha-globin cleanup, erythroid maturation, viability, and hemolysis gates.

## Ranked Gate Result

| Rank | Lane | Gate | Boundary |
| --- | --- | --- | --- |
| 1 | `AMPKB1` / `NRF2` / `ULK1` autophagy probe | first expansion assay probe | Assay biology only; not a patient candidate. |
| 2 | Pyruvate kinase activator reference | conditional or benchmark only | Strong clinical benchmark, but access and legal procurement block first use. |
| 3 | `T-BDMC`-like curcuminoid analog | conditional or benchmark only | Exact identity, supplier, purity, dose window, and hemolysis gate must come first. |
| 4 | `CRBN` / `WIZ` / `IKZF` degrader class | benchmark only, high caution | Mechanistic HbF comparator only; safety and regulatory barriers block affordable-treatment framing. |
| 5 | `HBD` / HbA2 delta-globin compensation | conditional expansion | Advanced globin-balance benchmark, not first expansion material. |
| 6 | Hepcidin / ferroportin iron-axis modulation | conditional or benchmark only | Important disease-modifier biology, but not the first HbF/globin-balance assay material. |

## Why This Matters

The repo already has a first lab quote panel:

- hydroxyurea;
- purified resveratrol;
- sirolimus;
- standardized 6-shogaol-rich ginger extract;
- melittin hazard control.

The decision here is about what to add only if a lab can support more than that
first panel. The gate keeps the project from drifting into a long candidate list
without assay logic.

## Evidence Notes

- The AMPK refresh snapshot retrieved the selective `AMPKB1` fetal-hemoglobin
  paper, PMID `41259521`; this supports assay-probe prioritization, not
  beta-thalassemia treatment use.
- The `T-BDMC` refresh snapshot retrieved the trienone-curcuminoid fetal
  hemoglobin paper, PMID `33879818`; this keeps the lane alive but still
  blocked by exact compound procurement and red-cell safety.
- The CRBN refresh snapshot retrieved a molecular-glue HbF paper, PMID
  `38963839`; the pomalidomide thalassemia query also recovered beta-thal/HbE
  and CD34+ HbF papers, including PMIDs `18064299` and `32358840`.
- The CRBN / IMiD class remains comparator-only because drug-class risk,
  cytopenia, teratogenicity, oncology-regulatory context, and procurement make
  it a poor affordable-treatment lead.

## Operational Decision

If a lab can add exactly one expansion lane, ask for a defined
`AMPKB1` / `NRF2` / `ULK1` / autophagy assay probe with the dual HbF plus
alpha-globin/autophagy readout panel.

If the lab cannot source that probe, do not replace it with an unsafe or vague
natural-product claim. Keep the core quote panel unchanged and use the expansion
lanes as benchmark context only.

## Required Readouts

- `HBG1` / `HBG2` messenger RNA;
- HbF protein;
- F-cell percentage;
- alpha/non-alpha globin balance;
- free or insoluble alpha-globin burden;
- `ULK1` and p62 / `SQSTM1` autophagy context;
- erythroid maturation;
- viability and apoptosis;
- mature red-cell hemolysis.

## Sources

- [Expansion lane decision gate notebook](../notebooks/2026-04-27-expansion-lane-decision-gate.ipynb)
- [AMPKB1/NRF2/ULK1 PubMed refresh](../../../data/literature/pubmed/2026-04-27-expansion-ampkb1-nrf2-ulk1-hbf.json)
- [CRBN HbF PubMed refresh](../../../data/literature/pubmed/2026-04-27-expansion-crbn-ikzf-bcl11a-hbf.json)
- [Pomalidomide HbF thalassemia PubMed refresh](../../../data/literature/pubmed/2026-04-27-expansion-pomalidomide-hbf-thalassemia.json)
- [T-BDMC HbF thalassemia PubMed refresh](../../../data/literature/pubmed/2026-04-27-expansion-t-bdmc-hbf-thalassemia.json)
- [AMPK/NRF2 expansion gate](2026-04-27-ampk-nrf2-expansion-gate.md)
- [AMPKB1 autophagy HbF bridge](2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [T-BDMC identity resolution](2026-04-27-t-bdmc-identity-resolution.md)
- [Avadomide/CRBN HbF evidence boundary](2026-04-27-avadomide-crbn-hbf-evidence-boundary.md)
- [Pyruvate kinase red-cell metabolism benchmark](2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
