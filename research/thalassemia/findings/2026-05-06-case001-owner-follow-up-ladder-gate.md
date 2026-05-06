# Case-001 Owner Follow-Up Ladder Gate

Date checked: 2026-05-06
Evidence label: operational follow-up gate, not medical advice

## Direct Answer

After owner-specific outreach and response capture, the next blocker is a
follow-up ladder. Without it, unanswered outreach can drift into repeated broad
messages or unsafely public notes.

Case-001 should use this public-safe operational label:

`owner_follow_up_ladder_ready`

The goal is to keep follow-up narrow: ask whether the owner can answer the
specific domain, needs records, should redirect the domain, or cannot review.

## Follow-Up States

Use only these labels in public artifacts:

- `follow_up_not_due`;
- `follow_up_ready`;
- `follow_up_sent`;
- `records_pending`;
- `owner_redirected`;
- `alternate_owner_needed`;
- `response_captured_private`;
- `route_closed_label_only`;
- `release_blocked`.

## Follow-Up Ladder

| Current state | Next narrow action | Public-safe output |
| --- | --- | --- |
| No outreach sent | Send one owner row, not the full paper. | `follow_up_not_due` |
| Outreach sent, no response yet | Send one short follow-up asking whether this is the right owner. | `follow_up_sent` |
| Owner asks for records | Return to the private source index and record request matrix. | `records_pending` |
| Owner redirects | Route to the named owner role, not a person or facility name. | `owner_redirected` |
| Owner cannot review | Pick an alternate owner route or leave unresolved. | `alternate_owner_needed` |
| Owner replies with content | Use the owner response capture gate. | `response_captured_private` |
| Response is label-only and release-checked | Update only the public-safe label. | `route_closed_label_only` |
| Response includes identifiers or treatment instructions | Keep private and block release. | `release_blocked` |

## Why This Matters

TIF 2025 separates TDT review across transfusion, blood-bank safety, iron
overload, monitoring, HCT, and gene manipulation domains. GeneReviews separates
phenotype-level thalassemia labels from molecular confirmation and genetic
counseling. Active advanced-therapy registry records continue to require formal
specialist screening and follow-up rather than public-repo eligibility claims.

Therefore, follow-up should not ask, "What is the cure?" It should ask whether
this owner can answer one domain or name the missing record or owner.

## Stop Conditions

This gate is complete for one owner route when:

1. the outreach state is recorded privately;
2. no raw message or contact details enter the public repo;
3. the next action is one of: wait, follow up, request records, redirect,
   capture response, close label-only, or block release;
4. patient-specific treatment instructions stay private and clinician-owned.

## Biomedical Boundary

This gate does not diagnose, dose, change transfusion, change chelation, change
immune medicine, recommend supplements, choose a referral, or decide trial
eligibility. It only defines how to follow up on owner outreach safely.

## Islamic Motivation Boundary

Quran 16:43 is used as an expert-consultation anchor. Quran 55:7-9 is used as a
measurement and anti-exaggeration anchor. These are method boundaries, not
biomedical evidence.

## Sources

- [Case-001 owner outreach packet](../case-context/case-001-owner-outreach-packet.md)
- [Case-001 owner response capture](../case-context/case-001-owner-response-capture.md)
- [Case-001 specialist owner routing](../case-context/case-001-specialist-owner-routing.md)
- [Case-001 record request matrix](../case-context/case-001-record-request-matrix.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [ClinicalTrials.gov thalassemia search](https://clinicaltrials.gov/search?cond=Thalassemia)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
