# Case-001 Branch Review Response Capture Gate

Date checked: 2026-06-28
Status: synthetic response-capture readiness, not treatment advice

## Direct Answer

June 28 adds a branch-review response-capture gate. If a qualified clinician
answers the branch-scope question, the public repo can record only allowed
labels, not the raw message.

Current operational label:

`case001_branch_review_response_capture_ready_synthetic_only`

## What This Gate Captures

Allowed public response labels are:

- `missing_packet_domain`
- `branch_in_scope_for_private_review`
- `branch_out_of_scope_for_private_review`
- `stabilization_first_private_review`
- `benchmark_only_private_review`
- `cannot_answer_from_packet`
- `release_blocked_private_material`

Branch labels are still private-review labels. They are not therapy selection,
eligibility, referral, trial screening, travel, import, purchase, dosing,
transfusion change, chelation change, lab contact, or sample-routing
permission.

## Public Output Contract

Public output may include:

- `current_label`
- `captured_labels`
- `missing_domains`
- `branch_scope_labels`
- `blocked_outputs`

Private-only fields such as `private_response_ref` and `notes_private` must
stay out of public output and out of Git when real clinician replies are used.

## Boundary

Quran 49:6 and 4:58 are process-ethics anchors only. They support verification
and qualified owner routing, not biomedical claims.

This gate does not provide diagnosis, treatment selection, eligibility,
trial-screening instruction, referral, travel guidance, import guidance,
purchase guidance, dosing, transfusion change, chelation change, lab contact,
private-message routing, or sample-routing permission.

## Sources

- [June 28 source JSON](../../../data/literature/pubmed/2026-06-28-branch-review-response-capture-refresh.json)
- [June 28 workflow JSON](../../../data/workflows/case-001/2026-06-28-branch-review-response-capture-gate.json)
- [Response-capture script](../../../scripts/capture_branch_review_response.py)
- [Response-capture template](../../../templates/branch-review-response-capture-template.csv)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- PubMed records: [PMID 42252696](https://pubmed.ncbi.nlm.nih.gov/42252696/),
  [PMID 41955126](https://pubmed.ncbi.nlm.nih.gov/41955126/),
  [PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/),
  [PMID 40058646](https://pubmed.ncbi.nlm.nih.gov/40058646/),
  [PMID 41919270](https://pubmed.ncbi.nlm.nih.gov/41919270/),
  [PMID 40862696](https://pubmed.ncbi.nlm.nih.gov/40862696/)
