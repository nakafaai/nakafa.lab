# Case-001 Mitapivat Clinician Conversation Sequence Gate

Date checked: 2026-05-21
Evidence label: clinician conversation sequence gate, not medical advice

## Direct Answer

The next blocker is sequencing. The doctor conversation should not begin with
mitapivat access or dosing. It should start with label validation, missing-record
routing, and seven-domain readiness. The mitapivat review-readiness question is
step five, not step one.

Case-001 should use this label:

`mitapivat_clinician_conversation_sequence_ready`

## Source Refresh

The May 21 check does not create a new cure claim:

- TIF 2025 supports beginning with clinical category, transfusion decision
  context, patient blood management, transfusion burden, iron overload, organ
  risk, and chelation context before disease-modifying drug review.
- FDA AQVESME evidence remains adult-label, hepatocellular-injury, REMS,
  hepatic-impairment, and interaction context.
- `NCT07506863` pediatric TDT and `NCT07517133` pediatric NTDT remain
  not-yet-recruiting watchlist records with no posted results in the current
  API check.
- `NCT04770779` remains adult TDT benchmark evidence with posted results, not
  pediatric case-specific evidence.

## Conversation Sequence

| Step | Ask for | Public-safe output |
| --- | --- | --- |
| `open_scope` | Confirm that the visit is for label validation and missing-record routing. | `scope_confirmed_or_corrected` |
| `validate_core_case_labels` | Confirm, correct, or mark unconfirmable the public-safe case labels. | `core_labels_confirmed_corrected_or_unconfirmable` |
| `close_missing_records` | Identify missing records and owner categories. | `missing_record_owner_labels_only` |
| `confirm_seven_domain_readiness` | Check whether the seven domains are privately label-ready and release-checked. | `seven_domain_readiness_label` |
| `ask_mitapivat_review_readiness` | Ask whether the lane is worth clinical review or should stay paused. | one allowed clinician response label |
| `route_after_answer` | Reduce the answer through the May 18 action ladder. | `next_research_state_label_only` |

## Stop Conditions

Stop before the mitapivat question if:

- the core diagnosis or transfusion category is unclear;
- any required domain is missing;
- any domain is release-blocked;
- the clinician redirects to a broader case packet first;
- the answer contains raw private material or patient-specific instructions.

## Biomedical Boundary

This gate does not diagnose subtype, recommend mitapivat, request dosing, change
care, decide access, decide trial screening, or interpret private records. It
only gives a safe order for asking a hematologist what should be confirmed.

## Islamic Motivation Boundary

Quran 49:6 supports verification before acting on reports. Quran 16:43 supports
qualified expert consultation when knowledge is missing. Quran 55:7-9 supports
measured claims and anti-exaggeration. These are research-method anchors, not
biomedical evidence.

## Sources

- [Mitapivat clinician conversation sequence gate map](../../../data/regulatory/mitapivat/2026-05-21-mitapivat-clinician-conversation-sequence-gate.json)
- [Case-001 mitapivat seven-domain owner action map](2026-05-20-case001-mitapivat-seven-domain-owner-action-map.md)
- [Case-001 mitapivat minimum-packet readiness gate](2026-05-19-case001-mitapivat-minimum-packet-readiness-gate.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
