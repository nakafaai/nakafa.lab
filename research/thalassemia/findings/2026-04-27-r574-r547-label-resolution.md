# Finding: R574 / R547 Label Resolution

Date checked: 2026-04-27
Evidence label: compound-identity correction, not treatment advice

## Working Conclusion

The HUDEP2 HbF screen names `R574` as a novel HbF inducer, but the same source
cites a CDK inhibitor paper whose compound is `R547`, not `R574`.

For Nakafa Lab, the safest interpretation is:

- keep the screen label as `R574` when quoting Yang 2024;
- map the probable structure/mechanism benchmark to `R547` / `RG-547`;
- mark this as a label discrepancy until the exact screening library record is
  recovered from the authors, supplier, or unambiguous supplementary metadata.

## Evidence

The Yang 2024 discussion describes `R574` as a potent ATP-competitive inhibitor
of `CDK1/2/4`. Its cited reference is Chu 2006, whose title and abstract identify
`R547` as the potent selective cyclin-dependent kinase inhibitor.

Database resolution supports the `R547` interpretation:

| Source | Resolved identity |
| --- | --- |
| PubChem | `R547`, `CID 6918852`, formula `C18H21F2N5O4S`, InChIKey `JRNJNYBQQYBCLE-UHFFFAOYSA-N` |
| ChEMBL | `RG-547`, `CHEMBL384304`, synonyms include `R 547`, `R-547`, and `Ro-4584820`; max phase `2` |
| ChEMBL activity | `Ki = 1 nM` for CDK4/cyclin D1, `2 nM` for CDK1, `3 nM` for CDK2 |

The downloaded PLOS supporting XLSX files provide useful raw assay data for
lead-hit and primary-cell validation, but the first pass did not expose a clean
`R574` or `R547` label in the workbook text. That means the identity claim should
not be upgraded from "probable" to "confirmed" yet.

## Research Decision

`R574` should no longer be treated as an unresolved unknown. It should be tracked
as `R574 / probable R547`, with `R547` used for chemistry and CDK mechanism
lookup.

It remains a high-caution benchmark. CDK1/2/4 inhibition is close to cell-cycle
and oncology pharmacology, so this lane is useful for assay interpretation and
target discovery, not for access-ready therapy speculation.

## Sources

- [Yang 2024 PLOS snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-yang-2024-hudep2-hbf-agonists-plos.dom.txt)
- [Yang 2024 Fig 4 supporting data](../../../data/literature/supplementary/plos/2026-04-27-yang-2024-fig4-lead-hit-drugs-s003.xlsx)
- [Yang 2024 Fig 5 supporting data](../../../data/literature/supplementary/plos/2026-04-27-yang-2024-fig5-cd34-s004.xlsx)
- [Yang 2024 Fig 6 supporting data](../../../data/literature/supplementary/plos/2026-04-27-yang-2024-fig6-western-s005.xlsx)
- [R574 ChEMBL unresolved search snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-r574-search.json)
- [R547 PubChem snapshot](../../../data/chemistry/pubchem/hudep2-hbf-hits/2026-04-27-r547-properties.json)
- [R547 ChEMBL search snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-r547-search.json)
- [R547 ChEMBL molecule snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-r547-chembl384304.json)
- [R547 ChEMBL activity snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-r547-chembl-activities.json)
- [Chu 2006 PubMed summary](../../../data/literature/pubmed/2026-04-27-r547-cdk-inhibitor-esummary.json)
- [Chu 2006 PubMed abstract XML](../../../data/literature/pubmed/2026-04-27-r547-cdk-inhibitor-abstract.xml)
