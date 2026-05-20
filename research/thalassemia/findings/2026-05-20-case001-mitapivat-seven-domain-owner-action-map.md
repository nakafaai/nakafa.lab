# Case-001 Mitapivat Seven-Domain Owner Action Map

Date checked: 2026-05-20
Evidence label: owner action map, not medical advice

## Direct Answer

The next blocker after the May 19 readiness gate is owner routing for each
required domain. The mitapivat lane should not jump from "packet readiness" to
"drug access." It should first map each missing or ready domain to the correct
clinical owner and a public-safe label.

Case-001 should use this label:

`mitapivat_seven_domain_owner_action_map_ready`

## Source Refresh

The May 20 source check does not create a new cure claim:

- TIF 2025 remains the clinical-context baseline for diagnosis, transfusion,
  iron, organ monitoring, multidisciplinary care, HCT, gene manipulation, and
  disease-modifying agents.
- FDA AQVESME evidence remains adult-label, liver-injury, REMS,
  hepatic-impairment, and interaction context.
- `NCT07506863` remains pediatric TDT watchlist evidence. The API check showed
  not-yet-recruiting, no posted results, last update 2026-04-08, and version
  2026-05-19.
- `NCT07517133` remains pediatric NTDT watchlist evidence. It must not be mixed
  with a TDT question.

## Owner Matrix

| Domain | Primary owner | Public-safe label |
| --- | --- | --- |
| `diagnosis_genotype_context` | hematologist or genetics lab | `diagnosis_genotype_label_ready_or_missing` |
| `age_weight_context` | treating hematologist | `age_weight_band_ready_or_missing` |
| `transfusion_burden_context` | hematologist or transfusion medicine | `transfusion_burden_ready_or_unquantified` |
| `iron_organ_context` | hematologist or iron/organ monitoring owner | `iron_organ_packet_ready_or_missing` |
| `liver_safety_context` | hematologist or hepatology owner | `liver_safety_review_ready_or_missing` |
| `medication_interaction_context` | hematologist or clinical pharmacist | `medication_review_ready_or_missing` |
| `local_access_context` | hematologist, then access owner | `access_owner_context_ready_or_missing` |

## Operational Rule

Each domain should move through one of four states:

- `domain_missing_private_record_request`
- `domain_label_ready_private`
- `domain_release_blocked_public_label_only`
- `all_domains_ready_for_clinician_question`

Do not ask for treatment, dosing, access, import, travel, or trial-screening
instructions. Ask only whether the packet is complete enough for a hematologist
to review the mitapivat lane at all.

## Privacy Boundary

The public repo may record owner categories, labels, source URLs, and public-safe
questions. It must not record raw records, exact dates, screenshots, doctor
messages, owner replies, contact details, or patient-specific instructions.

## Islamic Motivation Boundary

Quran 49:6 supports verification before acting on reports. Quran 16:43 supports
qualified expert consultation when knowledge is missing. Quran 55:7-9 supports
measured claims and anti-exaggeration. These are research-method anchors, not
biomedical evidence.

## Sources

- [Mitapivat seven-domain owner action map](../../../data/regulatory/mitapivat/2026-05-20-mitapivat-seven-domain-owner-action-map.json)
- [Case-001 mitapivat minimum-packet readiness gate](2026-05-19-case001-mitapivat-minimum-packet-readiness-gate.md)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
