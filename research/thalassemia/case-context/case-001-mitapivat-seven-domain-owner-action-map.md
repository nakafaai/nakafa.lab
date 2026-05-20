# Case-001 Mitapivat Seven-Domain Owner Action Map

Date: 2026-05-20
Status: public-safe owner-routing aid, not treatment advice
Privacy: no raw records, exact dates, screenshots, doctor messages, owner
replies, contact details, or patient-specific instructions

## Purpose

Use this after the May 19 minimum-packet readiness gate. The goal is to turn the
seven required domains into owner-specific private record questions before the
May 17 clinician-review question is asked.

Current label: `mitapivat_seven_domain_owner_action_map_ready`

## Domain Owners

| Domain | Primary owner |
| --- | --- |
| diagnosis and genotype context | hematologist or genetics lab |
| age and weight band | treating hematologist |
| transfusion burden context | hematologist or transfusion medicine |
| iron and organ context | hematologist or iron/organ monitoring owner |
| liver safety context | hematologist or hepatology owner |
| medication interaction context | hematologist or clinical pharmacist |
| local access owner context | hematologist, then regulatory, pharmacy, trial, or payer owner |

## Use Rule

For each domain, record only one public state:

- `domain_missing_private_record_request`
- `domain_label_ready_private`
- `domain_release_blocked_public_label_only`
- `all_domains_ready_for_clinician_question`

If any domain is missing or release-blocked, do not ask the mitapivat clinician
question yet. Return to private record retrieval or private owner review.

## Source-Backed Gates

- [Case-001 mitapivat seven-domain owner action map](../findings/2026-05-20-case001-mitapivat-seven-domain-owner-action-map.md)
- [Case-001 mitapivat minimum-packet readiness](case-001-mitapivat-minimum-packet-readiness.md)
- [Case-001 mitapivat clinician-review readiness](case-001-mitapivat-clinician-review-readiness.md)
