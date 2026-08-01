# First Quote Panel Assay Readiness Audit

Date checked: 2026-08-01
Status: lab-readiness audit, not treatment advice and not contact permission

## Purpose

This audit applies the May 31 minimum assay readiness gate to the first quote
panel. It separates quote-ready comparators or seeds from identity, model, and
endpoint holds.

Use the
[June 2 first quote request table](2026-06-02-first-quote-request-table.md)
for the compact lab-readable quote draft after this audit.

Current operational label:

`case001_first_quote_panel_assay_readiness_audit_ready`

## Current Panel Readiness

| Item | Role | Readiness | Next action |
| --- | --- | --- | --- |
| Hydroxyurea | Positive HbF comparator | `benchmark_only` | Use only as positive control if the lab can run HbF/HBG and safety readouts. |
| Purified resveratrol | NTDT iron-overload comparator | `deprioritized_from_first_hbf_quote` | Do not spend first-quote capacity. Reassess only after the complete randomized result reports registered iron, HbF, hemoglobin, transfusion, safety, and cost outcomes. |
| Sirolimus | mTOR/autophagy comparator | `assay_ready_for_quote` | Require autophagy, HbF/HBG, viability, maturation, and hemolysis boundaries. |
| Standardized 6-shogaol-rich ginger extract | Red-cell support comparator | `hold_for_model_or_endpoint_gap` | Resolve extract standardization, marker assay, batch controls, and support-only endpoint wording. |
| Melittin | Hemolysis hazard control | `benchmark_only` | Use only if the lab accepts hazard calibration and keeps it out of therapy framing. |
| PF-06409577 | `PRKAB1` expansion probe | `assay_ready_for_quote` | Keep expansion-only and require exact material plus HbF/HBG, autophagy, viability, and hemolysis readouts. |
| `T-BDMC`-like curcuminoid analog | Curcuminoid expansion seed | `hold_for_model_or_endpoint_gap` | Do not quote until exact structure, procurement identity, and batch control are resolved. |

## Identity Refresh

Current PubChem checks resolved exact compound identity for hydroxyurea,
resveratrol, sirolimus, 6-shogaol, melittin, and PF-06409577. This does not
solve extract standardization for ginger, nor the exact procurement identity
for `T-BDMC`-like chemistry.

## August 1 Evidence Correction

A 54-person randomized NTDT study and its Cochrane synthesis do not provide a
decision-useful HbF or transfusion-burden result for resveratrol. A 2026
30-person randomized conference abstract reports a six-month serum-ferritin
signal in 10 resveratrol recipients, but not HbF, hemoglobin, transfusion
burden, organ iron, or delivered cost. Resveratrol is therefore no longer ready
for the active first HbF quote. The other panel labels are unchanged.

## Boundary

This audit supports lab quote design only. It does not recommend patient use,
dosing, transfusion changes, chelation changes, supplements, trial screening,
travel, import, or treatment selection.

## Sources

- [June 1 workflow map](../../../data/workflows/case-001/2026-06-01-first-quote-panel-assay-readiness-audit.json)
- [Minimum assay readiness gate](2026-05-31-minimum-assay-readiness-gate.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [First wet-lab panel optimizer result](../findings/2026-04-27-first-wet-lab-panel-optimizer-result.md)
- [Resveratrol HbF and iron-overload evidence](../findings/2026-04-27-resveratrol-hbf-beta-thalassemia-seed.md)
- [EHA-3064 conference abstract](https://library.ehaweb.org/eha/2026/eha-2026/4208939/)
- [ISRCTN73258526 registry record](https://doi.org/10.1186/ISRCTN73258526)
- [Cochrane HbF-inducer review, PMID 36637054](https://pubmed.ncbi.nlm.nih.gov/36637054/)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
