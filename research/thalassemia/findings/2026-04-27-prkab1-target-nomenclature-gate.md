# Finding: PRKAB1 Target Nomenclature Gate

Date checked: 2026-04-27
Evidence label: target-naming gate for assay design, not treatment advice

## Working Conclusion

For lab-facing documents, the `AMPKB1` shorthand should be translated to:

`PRKAB1` / AMPK beta1 / 5'-AMP-activated protein kinase subunit beta-1.

The repo can still refer to the pathway as `AMPK beta1` biology, but qPCR,
antibody, omics, reagent, and assay requests should use `PRKAB1` for the human
gene and AMPK beta1 for the protein complex subunit.

## Why This Matters

`AMPKB1` is easy to read as "AMPK beta1," but it is not the official human gene
symbol. A lab quote that asks for `AMPKB1` without clarification can create
avoidable ambiguity.

Use this gate before any `AMPKB1` expansion-lane work order:

- gene-level readouts: `PRKAB1`;
- protein-level readouts: AMPK beta1 or AMPK subunit beta-1;
- compound lane: PF-06409577 as an AMPK beta1-biased research probe;
- pathway context: noncanonical `NRF2`, `ULK1`, and p62 / `SQSTM1`;
- disease endpoint: HbF/F-cell plus alpha-globin/autophagy and red-cell safety.

## Source-Backed Naming

NCBI Gene ID `5564` lists the official human symbol as `PRKAB1`, provided by
HGNC, with the official full name protein kinase AMP-activated non-catalytic
subunit beta 1. The same source describes the encoded protein as a regulatory
subunit of heterotrimeric AMPK.

The NCBI source also lists preferred protein names and related names including
5'-AMP-activated protein kinase subunit beta-1, AMPK beta 1, AMPK subunit
beta-1, and AMPKb.

## Assay Instruction

When the lab quote or assay template references this lane, write:

```text
Target lane:
PRKAB1 / AMPK beta1 / PF-06409577 research probe

Readouts:
PRKAB1 or AMPK beta1 context if available, HBG1/HBG2, HbF, F-cells,
NRF2 target context, ULK1 or phospho-ULK1, p62/SQSTM1, alpha/non-alpha
globin balance, free or insoluble alpha-globin, maturation, viability,
apoptosis, and mature red-cell hemolysis.
```

## Reject Or Hold Conditions

Hold this lane if:

- a lab cannot map `PRKAB1` to AMPK beta1;
- the quote only says generic AMPK activation;
- antibody, qPCR, or omics panels cannot specify whether they measure AMPK
  beta1, AMPK alpha phosphorylation, or generic downstream AMPK activity;
- PF-06409577 identity is detached from the target readouts;
- beta-thalassemia endpoint readouts are replaced by generic metabolic stress
  markers.

## Research Decision

Use `PRKAB1 / AMPK beta1` in lab-facing documents. Treat `AMPKB1` as a
readability shorthand only when the surrounding text makes the official target
clear.

This is a precision improvement, not a new cure claim.

## Sources

- [NCBI Gene: PRKAB1, Gene ID 5564](https://www.ncbi.nlm.nih.gov/gene/5564)
- [PF-06409577 probe material gate](2026-04-27-pf-06409577-probe-material-gate.md)
- [PF-06409577 ChEMBL activities snapshot](../../../data/chemistry/chembl/ampk-probes/2026-04-27-pf-06409577-chembl-activities.json)
- [Selective AMPKB1 HbF article, PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
