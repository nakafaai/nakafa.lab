# Case-001 Branch Review Packet Checker Gate

Date checked: 2026-06-27
Status: synthetic checker readiness, not treatment advice

## Direct Answer

June 27 adds a small checker that can read a private owner-maintained CSV and
emit only public-safe branch-review packet labels.

Current operational label:

`case001_branch_review_packet_checker_ready_synthetic_only`

## What The Checker Answers

The checker answers only this:

> Are the six private branch-review packet domains marked ready for private
> clinician review, or which public missing-domain labels should remain?

It does not answer whether any therapy branch is suitable.

## Public Output Contract

Public output may include:

- `current_label`
- `ready_domains`
- `missing_domains`
- `public_labels`
- `blocked_outputs`

Private-only fields such as `private_record_ref` and `notes_private` must stay
out of public output and out of Git when real records are used.

## Boundary

This gate does not provide diagnosis, dosing, treatment selection, eligibility,
trial-screening instruction, referral, travel guidance, import guidance,
purchase guidance, transfusion change, chelation change, lab contact,
private-message routing, or sample-routing permission.

Quran 49:6 and 4:58 are process-ethics anchors only. They support verification
and qualified owner routing, not biomedical claims.

## Sources

- [June 27 source JSON](../../../data/literature/pubmed/2026-06-27-branch-review-packet-checker-refresh.json)
- [June 27 workflow JSON](../../../data/workflows/case-001/2026-06-27-branch-review-packet-checker-gate.json)
- [Checker script](../../../scripts/check_branch_review_packet.py)
- [Template CSV](../../../templates/branch-review-minimum-packet-template.csv)
- [TIF 2025 diagnosis chapter](https://www.ncbi.nlm.nih.gov/books/NBK614253/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- PubMed records: [PMID 40058646](https://pubmed.ncbi.nlm.nih.gov/40058646/),
  [PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/),
  [PMID 42091200](https://pubmed.ncbi.nlm.nih.gov/42091200/),
  [PMID 42252696](https://pubmed.ncbi.nlm.nih.gov/42252696/),
  [PMID 41947014](https://pubmed.ncbi.nlm.nih.gov/41947014/),
  [PMID 41955126](https://pubmed.ncbi.nlm.nih.gov/41955126/)
