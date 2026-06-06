# T-BDMC Material Identity Gate

Date checked: 2026-06-04
Status: held-item material gate, not treatment advice and not contact
permission

## Purpose

This gate prevents `T-BDMC` from entering a lab quote as vague
`T-BDMC`-like chemistry. The structure is database-resolved, but material
procurement and batch controls are not quote-ready.

Current operational label:

`case001_t_bdmc_material_identity_gate_hold`

## Current Read

| Layer | Result | Quote meaning |
| --- | --- | --- |
| PubChem | `CID 10447050`, formula `C19H16O3`, InChIKey `PALMCMYYFAHUGA-BPTNNVFMSA-N` | Exact structure can be named. |
| ChEMBL | `CHEMBL469419`, same formula and InChIKey, no approved therapeutic status | Identity support only, not clinical evidence. |
| Literature | PubMed focused search still points to Nuamsee 2021 as the direct HbF-thalassemia source | Biology remains preclinical. |
| Safety | ChEMBL activity page includes KB IC50 `5750 nM`, Vero IC50 `9650 nM`, and selectivity index `1.68` | Hemolysis, erythroid viability, and maturation gates are mandatory. |

## Material Requirements Before Quote

`T-BDMC` can move from held to quote-candidate only if the material record has:

- exact `T-BDMC`, PubChem `CID 10447050`, ChEMBL `CHEMBL469419`, or matching
  InChIKey;
- certificate of analysis or equivalent batch record with identity, purity,
  lot, method, vehicle or solvent, and storage conditions;
- no substitution with turmeric, curcumin, `BDMC`, generic curcuminoids,
  `HHBDMC`, `T-Cur`, `T-DMC`, or unnamed `T-BDMC`-like material;
- lab acceptance of mature red-cell hemolysis, erythroid viability, and
  maturation as mandatory safety-window readouts.

## Decision

Keep `T-BDMC` out of the first quote. The exact database identity is resolved,
but procurement identity, batch purity, vehicle, storage, and safety-window
requirements are not ready.

The June 6 catalog feasibility gate found a material lead but keeps `T-BDMC`
held until exact batch identity, stereochemistry, purity, and safety-window
requirements pass.

## Boundary

This gate does not recommend patient use, dosing, supplements, transfusion
changes, chelation changes, trial screening, travel, import, or treatment
selection.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak or noisy signals. Quran 55:7-9 supports
measured claims. These are research-method anchors, not biomedical evidence for
`T-BDMC`.

## Sources

- [June 4 workflow map](../../../data/workflows/case-001/2026-06-04-t-bdmc-material-identity-gate.json)
- [June 6 catalog feasibility gate](2026-06-06-t-bdmc-catalog-feasibility-gate.md)
- [T-BDMC identity resolution](../findings/2026-04-27-t-bdmc-identity-resolution.md)
- [T-BDMC cytotoxicity boundary](../findings/2026-04-27-t-bdmc-cytotoxicity-boundary.md)
- [Curcuminoid analog assay map](../findings/2026-04-27-curcuminoid-analog-assay-map.md)
- [PubChem CID 10447050](https://pubchem.ncbi.nlm.nih.gov/compound/10447050)
- [ChEMBL CHEMBL469419](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL469419/)
- [PubMed PMID 33879818](https://pubmed.ncbi.nlm.nih.gov/33879818/)
- [PubMed PMID 24857542](https://pubmed.ncbi.nlm.nih.gov/24857542/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
