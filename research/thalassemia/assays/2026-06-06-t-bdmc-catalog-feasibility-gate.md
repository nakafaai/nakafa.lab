# T-BDMC Catalog Feasibility Gate

Date checked: 2026-06-06
Status: catalog lead found, still held from quote and not treatment advice

## Purpose

This gate upgrades `T-BDMC` from "no material lead" to "catalog lead found but
not quote-safe." It prevents a name-only supplier hit from bypassing exact
identity, stereochemistry, batch, purity, and safety-window requirements.

Current operational label:

`case001_t_bdmc_catalog_feasibility_gate_hold`

## Current Read

| Layer | Result | Quote meaning |
| --- | --- | --- |
| Exact target | PubChem `CID 10447050`, ChEMBL `CHEMBL469419`, InChIKey `PALMCMYYFAHUGA-BPTNNVFMSA-N` | Intended assay seed remains exact. |
| Stereochemistry trap | PubChem `CID 131752971` has the same formula but InChIKey `PALMCMYYFAHUGA-ZRFKDBLFSA-N` | Name/formula alone is unsafe. |
| Catalog lead | MCE lists `HY-N11902`, CAS `149732-52-5`, purity `95.51%`, and COA/CNMR/HPLC/MS links | Material lead exists, but batch documents must be reviewed. |
| Distributor lead | Namiki lists `HY-N11902`, supplier MedChemExpress, purity `>98%`, formula `C19H16O3`, and research-reagent-only language | A Japan distributor path exists, but not a clinical product. |
| Purity conflict | MCE and Namiki display different purity values | Batch-specific COA and HPLC documents must control. |
| Biology | PubMed focused check still points to Nuamsee 2021, PMID `33879818` | HbF evidence remains preclinical. |
| Synthesis/safety | PMID `24857542` remains the trienone synthesis and KB/Vero cytotoxicity source | Safety-window readouts remain mandatory. |

## Minimum Material Packet Before Quote

Do not move `T-BDMC` into a lab quote unless the packet includes:

- supplier or distributor URL;
- catalog number and CAS;
- batch number;
- certificate of analysis;
- `HPLC` purity report;
- `NMR` or `MS` identity report;
- exact InChIKey or structure match to PubChem `CID 10447050` or
  ChEMBL `CHEMBL469419`;
- storage and handling conditions;
- solvent or vehicle recommendation;
- lab acceptance of hemolysis, erythroid viability, and maturation
  safety-window readouts.

## Decision

Keep `T-BDMC` out of the first quote. A catalog lead now exists, but exact batch
identity and safety-window readiness are not complete.

## Boundary

This gate does not authorize patient purchase, patient import, dosing,
supplements, treatment selection, trial screening, travel, or clinical use.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak or noisy signals. Quran 55:7-9 supports
measured claims. These are research-method anchors, not biomedical evidence for
`T-BDMC`.

## Sources

- [June 6 workflow map](../../../data/workflows/case-001/2026-06-06-t-bdmc-catalog-feasibility-gate.json)
- [June 4 material identity gate](2026-06-04-t-bdmc-material-identity-gate.md)
- [PubChem CID 10447050](https://pubchem.ncbi.nlm.nih.gov/compound/10447050)
- [PubChem CID 131752971](https://pubchem.ncbi.nlm.nih.gov/compound/131752971)
- [ChEMBL CHEMBL469419](https://www.ebi.ac.uk/chembl/compound_report_card/CHEMBL469419/)
- [MCE HY-N11902](https://www.medchemexpress.com/1-7-bis-4-hydroxyphenyl-1-4-6-heptatrien-3-one.html)
- [Namiki HY-N11902](https://www.namiki-s.co.jp/compound/compound_detail.php?code=HY-N11902)
- [PubMed PMID 33879818](https://pubmed.ncbi.nlm.nih.gov/33879818/)
- [PubMed PMID 24857542](https://pubmed.ncbi.nlm.nih.gov/24857542/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
