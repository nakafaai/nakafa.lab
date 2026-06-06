# Finding: Case-001 T-BDMC Catalog Feasibility Gate

Date checked: 2026-06-06
Evidence label: catalog feasibility, stereochemistry boundary, and safety
gate; not medical advice

## Direct Answer

`T-BDMC` now has a catalog lead: MedChemExpress `HY-N11902`, also visible via
Namiki. This changes the blocker from "find any material lead" to "verify exact
batch identity before quote."

The quote state stays held because supplier names, CAS, and formula are not
enough. A current PubChem check showed a same-formula, name-adjacent
stereoisomer with a different InChIKey, so the intended batch must be checked
against PubChem `CID 10447050` / ChEMBL `CHEMBL469419` or matching InChIKey.
MCE and Namiki also display different purity values, so batch-specific COA and
HPLC documents must control.

## Result

| Question | Current answer | Decision |
| --- | --- | --- |
| Is there a catalog lead? | Yes: MCE `HY-N11902`, CAS `149732-52-5`. | Promote to material-lead-found. |
| Is it quote-ready? | No. COA, HPLC, NMR/MS, storage, vehicle, and exact structure match still need review. | Keep held. |
| Is there an isomer risk? | Yes. PubChem `CID 131752971` has the same formula but different InChIKey. | Require exact InChIKey or structure proof. |
| Is purity settled? | No. MCE and Namiki display different purity values. | Use batch COA/HPLC only. |
| Does this add clinical evidence? | No. MCE/Namiki are reagent sources, not thalassemia evidence. | No treatment claim. |
| What remains the biology source? | Nuamsee 2021, PMID `33879818`. | Preclinical HbF seed only. |

## Decision Rule

Move `T-BDMC` toward quote only after the material packet names:

- exact supplier or distributor;
- catalog number, CAS, and batch;
- certificate of analysis;
- `HPLC` purity;
- `NMR` or `MS` identity;
- exact InChIKey or structure match to `PALMCMYYFAHUGA-BPTNNVFMSA-N`;
- storage, solvent, and vehicle;
- hemolysis, erythroid viability, and maturation safety-window readouts.

## Boundary

Do not use this as a patient procurement, import, supplement, dosing, trial, or
treatment instruction. This is a preclinical material feasibility note only.

## Sources

- [June 6 assay gate](../assays/2026-06-06-t-bdmc-catalog-feasibility-gate.md)
- [June 6 workflow map](../../../data/workflows/case-001/2026-06-06-t-bdmc-catalog-feasibility-gate.json)
- [June 4 material identity gate](../assays/2026-06-04-t-bdmc-material-identity-gate.md)
- [PubChem CID 10447050](https://pubchem.ncbi.nlm.nih.gov/compound/10447050)
- [PubChem CID 131752971](https://pubchem.ncbi.nlm.nih.gov/compound/131752971)
- [MCE HY-N11902](https://www.medchemexpress.com/1-7-bis-4-hydroxyphenyl-1-4-6-heptatrien-3-one.html)
- [Namiki HY-N11902](https://www.namiki-s.co.jp/compound/compound_detail.php?code=HY-N11902)
- [PubMed PMID 33879818](https://pubmed.ncbi.nlm.nih.gov/33879818/)
- [PubMed PMID 24857542](https://pubmed.ncbi.nlm.nih.gov/24857542/)
