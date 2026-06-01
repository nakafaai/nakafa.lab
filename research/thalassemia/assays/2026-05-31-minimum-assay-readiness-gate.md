# Minimum Assay Readiness Gate

Date checked: 2026-05-31
Status: lab-readiness gate, not treatment advice and not contact permission

## Purpose

This gate turns the May 30 candidate promotion rule into a lab-readable minimum
package. A candidate can be interesting and still not be assay-ready.

Use the
[first quote panel assay readiness audit](2026-06-01-first-quote-panel-assay-readiness-audit.md)
for the first applied panel-level result.

Current operational label:

`case001_minimum_assay_readiness_gate_ready`

## Minimum Fields

| Field | Required content |
| --- | --- |
| Candidate identity | Exact material, batch, purity, standardization, or reason identity is not yet resolved. |
| Category | Comparator, drug, purified molecule, standardized extract, probe, hazard control, or benchmark. |
| Target gap | Cost, infrastructure, conditioning, monitoring, access, safety, fertility, or assay feasibility. |
| Model context | HUDEP2, endogenous HbF reporter, CD34+ erythroid model, disease-relevant cells, or explicit reason the model is only a screen. |
| Controls | Positive HbF comparator, vehicle or negative control, and hazard or hemolysis control when relevant. |
| Endpoints | HbF/HBG, erythroid maturation, viability, hemolysis, chain balance or free alpha-globin, and claimed autophagy readouts. |
| Stop rule | Identity failure, no endpoint movement, hemolysis, toxicity, model mismatch, access failure, or benchmark-only result. |
| Privacy | No identifiable records or patient samples without ethics, consent, biosafety, and clinician oversight. |

## Assay Decisions

- `assay_ready_for_quote`: complete model, controls, endpoints, stop rules,
  raw-data plan, and privacy boundary.
- `hold_for_model_or_endpoint_gap`: plausible but missing model, endpoint,
  replicate, comparator, or raw-data plan.
- `reject_for_identity_or_safety_failure`: material identity, safety, or
  endpoint failure is clear.
- `benchmark_only`: useful standard, not an affordable discovery candidate.
- `ethics_or_privacy_blocked`: requires private records, patient samples, or
  clinical action without review.

## Current Read

The current literature supports better assay discipline, not a direct cure
claim. A 2024 endogenous HbF reporter source supports HbF screening context.
A 2024 small-molecule HbF screening paper supports screen design but is not
thalassemia treatment evidence. A 2023 hemolysis-assay source supports mature
red-cell safety screening. 2026 reporter and Southeast Asia alpha-thalassemia
model papers show the model landscape is improving, while also proving that
model context must be explicit.

## Islamic Motivation Boundary

Quran 16:43 supports asking qualified experts. Quran 13:17 supports discarding
weak signals. Quran 55:7-9 supports measured claims. These are research-method
anchors, not biomedical evidence for any assay candidate.

## Sources

- [May 31 workflow map](../../../data/workflows/case-001/2026-05-31-minimum-assay-readiness-gate.json)
- [May 30 promotion gate](../prioritization/2026-05-30-affordable-cure-candidate-promotion-gate.md)
- [First lab quote brief V0](2026-04-27-first-lab-quote-brief-v0.md)
- [PubMed PMID 39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/)
- [PubMed PMID 39504332](https://pubmed.ncbi.nlm.nih.gov/39504332/)
- [PubMed PMID 36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
- [PubMed PMID 41736887](https://pubmed.ncbi.nlm.nih.gov/41736887/)
- [PubMed PMID 42162272](https://pubmed.ncbi.nlm.nih.gov/42162272/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
