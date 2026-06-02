# First Quote Request Table

Date checked: 2026-06-02
Status: public-safe preclinical quote draft, not treatment advice and not
contact permission

## Purpose

This table converts the June 1 assay readiness audit into a compact lab quote
request. It asks for model availability, readout feasibility, material
requirements, cost, timeline, and raw-data format.

It does not authorize outreach, patient samples, treatment validation, dosing,
trial screening, travel, import, or patient-specific action.

Current operational label:

`case001_first_quote_request_table_ready`

## Quote Request Table

| Item | Quote role | Material ask | Readout ask | Stop condition | Boundary |
| --- | --- | --- | --- | --- | --- |
| Hydroxyurea | Positive HbF comparator | Lab-standard comparator with identity and vehicle documented. | HbF/HBG response, maturation, viability. | Do not frame as a new cure candidate. | Comparator only. |
| Purified resveratrol | HbF and erythroid-maturation seed | Purified compound with supplier, batch, purity, certificate of analysis if available, and vehicle documented. | HbF/HBG, HbF protein or F-cell percentage if available, maturation, viability, hemolysis, alpha/non-alpha or free alpha-globin context if available. | Hold or reject if identity, viability, hemolysis, or maturation boundaries fail. | Preclinical seed only. |
| Sirolimus | mTOR/autophagy comparator | Exact compound identity, supplier, batch, purity, and vehicle documented. | HbF/HBG, ULK1, p62/SQSTM1 or lab equivalent, maturation, viability, hemolysis. | Hold or reject if immune-active comparator status is blurred into patient-facing therapy language. | Preclinical comparator only. |
| Melittin | Hemolysis hazard control | Use only if the lab accepts it as a hazard-calibration control and documents biosafety handling. | Mature red-cell hemolysis or membrane damage; rejection threshold calibration. | Exclude if safe handling is unavailable or if therapy framing appears. | Hazard control only. |
| PF-06409577 | `PRKAB1` / AMPK beta1 expansion probe | Exact identity, supplier, batch, purity, and vehicle documented. | HbF/HBG, AMPK beta1 or downstream target engagement if available, ULK1, p62/SQSTM1 or lab equivalent, maturation, viability, hemolysis. | Keep expansion-only unless the lab can support AMPK beta1 and autophagy context without patient-facing claims. | Expansion probe only. |

## Held Out Of This Quote

| Item | Reason |
| --- | --- |
| Standardized 6-shogaol-rich ginger extract | Extract standardization, marker assay, batch controls, and support-only endpoint wording are not ready enough for first quote. |
| `T-BDMC`-like curcuminoid analog | Exact structure, procurement identity, and batch control remain unresolved for this quote. |

## Lab Questions

Ask the lab to answer:

- Which erythroid model can be run: HUDEP2, endogenous HbF reporter, CD34+
  erythroid differentiation, beta-thalassemia/HbE cells, or another validated
  model?
- Can the lab measure endogenous HbF or `HBG1` / `HBG2`?
- Can the lab measure HbF protein or F-cell percentage?
- Can the lab measure erythroid maturation markers such as `CD71` and
  `CD235a`?
- Can the lab measure viability or apoptosis?
- Can the lab run mature red-cell hemolysis or membrane-damage assays?
- Can the lab measure alpha/non-alpha globin balance or free alpha-globin
  burden?
- Can the lab measure autophagy readouts for sirolimus and PF-06409577?
- What are the per-item cost, per-readout cost, replicate plan, timeline,
  material requirements, raw-data format, known limitations, and ethics or
  biosafety constraints?

## Boundary

Send only public research context and de-identified summaries. Do not send raw
records, patient samples, doctor messages, owner replies, names, exact birth
dates, hospital numbers, contact details, screenshots, prescriptions, lab
reports, private family notes, treatment-selection requests, dosing requests,
trial-screening requests, travel requests, or import requests.

## Islamic Motivation Boundary

Quran 13:17 supports discarding weak signals. Quran 55:7-9 supports measured
claims. These are research-method anchors, not biomedical evidence for any quote
item.

## Sources

- [June 2 workflow map](../../../data/workflows/case-001/2026-06-02-first-quote-request-table.json)
- [June 1 assay readiness audit](2026-06-01-first-quote-panel-assay-readiness-audit.md)
- [May 31 minimum assay readiness gate](2026-05-31-minimum-assay-readiness-gate.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [PubMed PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
- [PubMed PMID 36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubChem hydroxyurea CID 3657](https://pubchem.ncbi.nlm.nih.gov/compound/3657)
- [PubChem resveratrol CID 445154](https://pubchem.ncbi.nlm.nih.gov/compound/445154)
- [PubChem sirolimus CID 5284616](https://pubchem.ncbi.nlm.nih.gov/compound/5284616)
- [PubChem melittin CID 16133648](https://pubchem.ncbi.nlm.nih.gov/compound/16133648)
- [PubChem PF-06409577 CID 71748255](https://pubchem.ncbi.nlm.nih.gov/compound/71748255)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
