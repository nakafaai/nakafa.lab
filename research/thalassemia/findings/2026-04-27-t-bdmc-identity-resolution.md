# Finding: T-BDMC Identity Resolution

Date checked: 2026-04-27
Evidence label: chemistry identity resolution and assay-seed upgrade, not treatment advice

## Working Conclusion

`T-BDMC` can now be tracked as a chemistry-resolved curcuminoid trienone HbF
seed.

The exact publication name,
`(1E,4E,6E)-1,7-bis(4-hydroxyphenyl)-1,4,6-heptatrien-3-one`, resolved through
ChEMBL as `CHEMBL469419`. The ChEMBL InChIKey then resolved in PubChem as
`CID 10447050`.

This does not make `T-BDMC` a treatment lead. It means the next research blocker
is no longer "what is the molecule?" The blocker is now practical translation:
source or synthesis route, batch purity, red-cell hemolysis, endogenous HbF
replication, disease-cell replication, and safety.

## Identity Trail

| Check | Result | Interpretation |
| --- | --- | --- |
| PubChem name query for `T-BDMC` | no CID found | abbreviation alone is not enough for identity lookup |
| PubChem exact-name query | no CID found | PubChem name resolver did not match the long publication name directly |
| ChEMBL exact-name search | `CHEMBL469419`, score `104` | cleanest retrieved database identity for the publication name |
| PubChem InChIKey lookup | `CID 10447050` | confirms the same structure through `PALMCMYYFAHUGA-BPTNNVFMSA-N` |
| ChEMBL `HHBDMC` search | zero molecules | reduced analog lane remains unresolved |

## Resolved Compound Record

| Field | Value |
| --- | --- |
| PubChem | `CID 10447050` |
| ChEMBL | `CHEMBL469419` |
| Formula | `C19H16O3` |
| Molecular weight | `292.3` / `292.33` |
| InChIKey | `PALMCMYYFAHUGA-BPTNNVFMSA-N` |
| SMILES | `O=C(/C=C/C=C/c1ccc(O)cc1)/C=C/c1ccc(O)cc1` |
| PubChem XLogP | `4` |
| PubChem TPSA | `57.5` |
| H-bond donors / acceptors | `2` / `3` |
| ChEMBL max phase | none |
| ChEMBL natural-product flag | `1` |

ChEMBL activity records for `CHEMBL469419` are not HbF records. The first
retrieved activity page contains antioxidant, COX, PC12 protection, lipid
peroxidation, and cytotoxicity records. Therefore, the HbF evidence must remain
attributed to the Nuamsee 2021 beta-thalassemia/HbE study, not to ChEMBL
activity annotations.

The same ChEMBL activity snapshot now also creates a safety boundary:
`CHEMBL469419` has low-micromolar KB and Vero cytotoxicity records from the
trienone synthesis paper. That does not replace erythroid or red-cell testing,
but it makes dose-window and hemolysis gates mandatory.

## Biology Boundary

Nuamsee 2021 remains the relevant biology source:

- `T-BDMC` was the strongest reported K562 HbF inducer in that study, around
  `2.4 +/- 0.2` fold endogenous HbF;
- it also entered beta-thalassemia/HbE erythroid progenitor testing;
- the study reported reduced DNA methylation at the `G gamma` promoter CpG
  `+6` site in beta-thalassemia/HbE progenitors;
- purity in the publication was reported as greater than `95%` by TLC and NMR;
- pharmacokinetics, bioavailability, hemolysis, and in vivo translation were
  not established.

## Research Decision

Promote `T-BDMC` from "publication-defined but database-unresolved" to
"chemistry-resolved high-priority assay seed".

The next gates are:

- obtain a supplier record or synthesis partner for `CID 10447050` /
  `CHEMBL469419`;
- confirm batch identity and purity before any biology run;
- run mature red-cell hemolysis before disease-cell escalation;
- repeat endogenous HbF protein, F-cell, `HBG1/HBG2`, globin balance, and
  erythroid maturation endpoints;
- compare against hydroxyurea, decitabine, `isocoronarin D`,
  `3,4'-Di-O-methylquercetin`, and vehicle controls;
- keep the reduced analog `HHBDMC` as a separate unresolved chemistry lane.

## Sources

- [T-BDMC PubChem InChIKey snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-t-bdmc-inchikey-properties.json)
- [T-BDMC PubChem abbreviation negative snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-t-bdmc-name-properties.json)
- [T-BDMC PubChem long-name negative snapshot](../../../data/chemistry/pubchem/curcuminoid-analogs/2026-04-27-t-bdmc-iupac-properties.json)
- [T-BDMC ChEMBL exact-name search snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-t-bdmc-iupac-search.json)
- [T-BDMC ChEMBL molecule snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-t-bdmc-chembl469419.json)
- [T-BDMC ChEMBL activity snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-t-bdmc-chembl-activities.json)
- [HHBDMC ChEMBL negative search snapshot](../../../data/chemistry/chembl/curcuminoid-analogs/2026-04-27-hhbdmc-search.json)
- [Nuamsee 2021 PMC snapshot](../../../data/literature/fulltext/nature/2026-04-27-nuamsee-2021-curcuminoid-trienone-pmc.html)
- [Curcuminoid analog assay map](2026-04-27-curcuminoid-analog-assay-map.md)
- [T-BDMC cytotoxicity boundary](2026-04-27-t-bdmc-cytotoxicity-boundary.md)
