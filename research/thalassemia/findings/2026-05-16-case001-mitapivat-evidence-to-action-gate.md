# Case-001 Mitapivat Evidence-To-Action Gate

Date checked: 2026-05-16
Evidence label: current evidence-to-action gate, not medical advice

## Direct Answer

The next blocker after response capture is evidence-to-action separation. The
May 16 refresh supports adult mitapivat as a disease-modifying benchmark, but
it still does not justify pediatric, local-access, or case-specific claims.

Case-001 should use this label:

`mitapivat_evidence_to_action_ready`

## What Changed In The Current Refresh

The current ClinicalTrials.gov API snapshot for `NCT04770779` now has posted
results and remains `ACTIVE_NOT_RECRUITING`. This makes adult TDT mitapivat a
stronger benchmark than it was in the earlier compact notes.

The two pediatric mitapivat records remain separate:

- `NCT07506863`: pediatric TDT, `NOT_YET_RECRUITING`, no posted results,
  primary outcome is transfusion-reduction response through week 48.
- `NCT07517133`: pediatric NTDT, `NOT_YET_RECRUITING`, no posted results,
  primary outcome is hemoglobin response.

The FDA label and official AQVESME site remain adult-only for the indication.
The official site states that safety and effectiveness in children are not
known.

## Allowed Actions

| Evidence state | Allowed public action |
| --- | --- |
| `adult_us_label_current` | Use as an adult-label benchmark. |
| `adult_tdt_results_posted` | Use as an adult TDT transfusion-reduction benchmark. |
| `pediatric_tdt_not_yet_recruiting` | Track as a pediatric TDT registry watchlist. |
| `pediatric_ntdt_not_yet_recruiting` | Track as a pediatric NTDT watchlist only. |
| `safety_and_rems_review_required` | Route safety and monitoring questions to qualified owners. |
| `case_relevance_still_blocked` | Ask hematology only after the minimum packet is complete enough. |

## Blocked Claims

- No claim that adult FDA approval establishes pediatric relevance.
- No claim that adult ENERGIZE-T results establish individual response.
- No claim that a not-yet-recruiting pediatric record establishes access,
  eligibility, safety, or effectiveness.
- No claim that a pediatric NTDT record answers a TDT question.
- No dosing, monitoring, start, stop, transfusion, chelation, travel, import,
  or legal instruction.
- No public raw records, owner replies, identifiers, screenshots, doctor
  messages, exact private dates, or patient-specific advice.

## Operational Rule

Use adult mitapivat evidence as a benchmark only. Use pediatric mitapivat
records as watchlist evidence only. Do not move from benchmark to case action
unless a qualified clinician reviews the minimum packet and names the next
proper owner.

## Biomedical Boundary

This gate does not diagnose thalassemia subtype, recommend mitapivat, change
standard care, decide trial eligibility, report an adverse event, or decide
local access. It only separates current evidence states from allowed public
actions.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran 55:7-9
supports measured claims and anti-exaggeration. Quran 16:43 supports qualified
expert consultation. These are method anchors, not biomedical evidence.

## Sources

- [Mitapivat evidence-to-action map](../../../data/regulatory/mitapivat/2026-05-16-mitapivat-evidence-to-action-map.json)
- [May 16 active mitapivat thalassemia registry refresh](../../../data/registries/clinicaltrials/2026-05-16-active-mitapivat-thalassemia-refresh.json)
- [May 16 NCT04770779 ENERGIZE-T detail](../../../data/registries/clinicaltrials/2026-05-16-nct04770779-energize-t-detail.json)
- [May 16 NCT07506863 pediatric TDT detail](../../../data/registries/clinicaltrials/2026-05-16-nct07506863-mitapivat-pediatric-tdt-detail.json)
- [May 16 NCT07517133 pediatric NTDT detail](../../../data/registries/clinicaltrials/2026-05-16-nct07517133-mitapivat-pediatric-ntdt-detail.json)
- [May 16 PubMed mitapivat ENERGIZE-T refresh](../../../data/literature/pubmed/2026-05-16-mitapivat-energize-t-refresh.json)
- [AQVESME official site](https://www.aqvesme.com/thalassemia/)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
