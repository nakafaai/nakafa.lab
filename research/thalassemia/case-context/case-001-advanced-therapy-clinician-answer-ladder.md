# Case-001 Advanced-Therapy Clinician-Answer Ladder

Date checked: 2026-05-27
Status: public-safe response-capture note, not treatment advice

## Purpose

Use this after a doctor or specialist responds to the May 26 owner packet. It
keeps the response from jumping directly to therapy, trial, travel, import, or
access instructions.

## Response Labels

| If the clinician says... | Public label |
| --- | --- |
| A domain record is present. | `owner_domain_labeled_present` |
| A domain record is missing and should be requested. | `owner_domain_missing_record_requested` |
| A domain is not applicable for this case. | `owner_domain_not_applicable` |
| Specialist screening is reasonable after packet review. | `advanced_therapy_referral_packet_ready_for_specialist_screening` |
| Screening is not reasonable for a medical reason. | `medically_unsuitable` |
| Biology may be relevant, but access, center, payer, or geography blocks it. | `access_blocked` |
| The reply includes private or patient-specific instructions. | `release_blocked_private_material` |

## Doctor-Facing Script

> To keep our notes safe, can we reduce your answer to one label: present,
> missing, not applicable, ready for specialist screening, medically unsuitable,
> access blocked, or private-only?

## Public Release Rule

Only the label and broad domain category can enter the public repo. Raw records,
screenshots, doctor messages, names, hospitals, contacts, exact private dates,
HLA or donor details, and patient-specific instructions stay private.

Use the [advanced-therapy route triage](case-001-advanced-therapy-route-triage.md)
if a reply is about which advanced-therapy branch belongs in scope.

## Sources

- [May 27 clinician-answer ladder gate](../findings/2026-05-27-case001-advanced-therapy-clinician-answer-ladder-gate.md)
- [May 28 route triage](case-001-advanced-therapy-route-triage.md)
- [May 27 workflow map](../../../data/workflows/case-001/2026-05-27-advanced-therapy-clinician-answer-ladder.json)
- [May 26 owner packet](case-001-advanced-therapy-screening-owner-packet.md)
