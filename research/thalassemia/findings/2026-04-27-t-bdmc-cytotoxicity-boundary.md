# Finding: T-BDMC Cytotoxicity Boundary

Date checked: 2026-04-27
Evidence label: synthesis and cytotoxicity boundary, not treatment advice

## Working Conclusion

`T-BDMC` remains the cleanest curcuminoid analog assay seed, but it has a
low-micromolar cytotoxicity warning that must shape every next experiment.

The synthesis/cytotoxicity source linked from Nuamsee 2021 is PubMed PMID
`24857542`. Its abstract describes a general synthesis of substituted
`(1E,4E,6E)-1,7-diphenylhepta-1,4,6-trien-3-ones` through aldol condensations.
That supports the idea that a synthesis partner could recreate the trienone
series.

However, ChEMBL activity records for `T-BDMC` / `CHEMBL469419` include
cytotoxicity against KB and Vero cells from the same document. This does not
answer red-cell or erythroid safety directly, but it makes hemolysis,
erythroid maturation, and dose-window testing non-negotiable.

## Extracted Records

| Source | Result | Meaning |
| --- | --- | --- |
| PubMed PMID `24857542` | trienone synthesis and KB/Vero cytotoxicity paper | synthesis route exists at literature level |
| ChEMBL document | `CHEMBL3286273`, DOI `10.1016/j.bmcl.2014.04.105` | ChEMBL-indexed source for trienone analog activities |
| `CHEMBL469419` KB activity | IC50 `5750 nM` | low-micromolar cytotoxicity in human oral cancer KB cells |
| `CHEMBL469419` Vero activity | IC50 `9650 nM` | low-micromolar cytotoxicity in non-cancerous Vero cells |
| `CHEMBL469419` selectivity index | `1.68` | not one of the strongest selectivity-index trienones in the abstract |

The source abstract says compounds `11`, `12`, and `17` had high selectivity
indices, but the current `CHEMBL469419` record has selectivity index `1.68`.
Therefore, do not assume all trienone analogs share the most favorable safety
profile.

## Research Decision

Keep `T-BDMC` as a high-priority assay seed, but set a stricter safety rule:

- identify the exact test concentration used in HbF assays before procurement;
- run red-cell hemolysis before primary erythroid escalation;
- run erythroid viability and maturation at every HbF-active concentration;
- reject or redesign if HbF induction overlaps with cytotoxicity or maturation
  arrest;
- compare `T-BDMC` against less cytotoxic trienone analogs if structure and HbF
  evidence can be recovered.

`T-BDMC` is no longer just an identity question. It is now a dose-window and
safety-window question.

## Sources

- [T-BDMC synthesis/cytotoxicity PubMed ESummary](../../../data/literature/pubmed/2026-04-27-tbdmc-trienone-synthesis-cytotoxicity-esummary.json)
- [T-BDMC synthesis/cytotoxicity PubMed abstract](../../../data/literature/pubmed/2026-04-27-tbdmc-trienone-synthesis-cytotoxicity-abstract.xml)
- [T-BDMC synthesis/cytotoxicity Crossref snapshot](../../../data/literature/pubmed/2026-04-27-tbdmc-trienone-synthesis-cytotoxicity-crossref.json)
- [T-BDMC synthesis ChEMBL document snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-tbdmc-trienone-synthesis-chembl-document.json)
- [T-BDMC ChEMBL molecule snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-t-bdmc-chembl469419.json)
- [T-BDMC ChEMBL activity snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-t-bdmc-chembl-activities.json)
- [T-BDMC identity resolution](2026-04-27-t-bdmc-identity-resolution.md)
