# Case-001 Mitapivat Clinician Answer Action Ladder

Date checked: 2026-05-18
Evidence label: clinician-answer action ladder, not medical advice

## Direct Answer

After the May 17 review-readiness question, the next blocker is response
handling. A clinician answer should change the research queue, not the
treatment plan.

Case-001 should use this label:

`mitapivat_clinician_answer_action_ladder_ready`

## Source Refresh

The May 18 check found no loosened evidence boundary:

- `NCT04770779` remains adult TDT benchmark evidence with posted results.
- `NCT07506863` remains pediatric TDT watchlist evidence with no posted
  results.
- `NCT07517133` remains pediatric NTDT watchlist evidence with no posted
  results.
- FDA AQVESME label evidence remains adult-label and safety-context evidence.
- TIF 2025 remains the clinical-context baseline for TDT review.

## Action Ladder

| Clinician label | Public action |
| --- | --- |
| `review_not_ready_missing_records` | Record missing-domain labels only. |
| `not_clinically_relevant_now` | Record `lane_paused_by_clinician_review`. |
| `review_with_hematologist_only` | Record `hematologist_review_only`. |
| `refer_to_trial_or_access_owner_after_clinician_review` | Record owner category and public source only. |
| `safety_review_required_before_any_discussion` | Record `safety_review_needed`. |
| `lane_paused_until_pediatric_results_or_recruitment` | Record `pediatric_watchlist_pause`. |

## Operational Rule

Do not paste the doctor's message into the repo. Reduce it to one allowed label,
one public action, and one private action. If the reply contains a treatment
instruction, raw record request, name, contact detail, exact private date, or
screenshot, keep it private and publish only the blocked state.

## Biomedical Boundary

This ladder does not diagnose, recommend mitapivat, change transfusion or
chelation care, decide trial screening, decide access, or answer safety
questions. It only tells the public repo how to record a clinician answer
without leaking private material or turning the answer into treatment advice.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran
55:7-9 supports measured claims and anti-exaggeration. Quran 16:43 supports
qualified expert consultation. These are research-method anchors, not
biomedical evidence.

## Sources

- [Mitapivat clinician-answer action ladder map](../../../data/regulatory/mitapivat/2026-05-18-mitapivat-clinician-answer-action-ladder.json)
- [Case-001 mitapivat clinician-review readiness gate](2026-05-17-case001-mitapivat-clinician-review-readiness-gate.md)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
