# First Quote Panel Assay Readiness Audit

Date checked: 2026-06-01
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
| Purified resveratrol | HbF seed | `assay_ready_for_quote` | Require purity, batch, vehicle, HbF/HBG, maturation, viability, hemolysis, and chain-balance readouts. |
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

## Boundary

This audit supports lab quote design only. It does not recommend patient use,
dosing, transfusion changes, chelation changes, supplements, trial screening,
travel, import, or treatment selection.

## Sources

- [June 1 workflow map](../../../data/workflows/case-001/2026-06-01-first-quote-panel-assay-readiness-audit.json)
- [Minimum assay readiness gate](2026-05-31-minimum-assay-readiness-gate.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [First wet-lab panel optimizer result](../findings/2026-04-27-first-wet-lab-panel-optimizer-result.md)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
