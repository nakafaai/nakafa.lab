# Case-001 Mitapivat Clinician Review Readiness Gate

Date checked: 2026-05-17
Evidence label: clinician-review readiness gate, not medical advice

## Direct Answer

The next blocker after evidence-to-action separation is clinician-review
readiness. The useful question is no longer whether mitapivat is interesting.
The useful question is whether a hematologist can safely review the lane at all
from the current record packet.

Case-001 should use this label:

`mitapivat_clinician_review_readiness_ready`

## One Question For The Hematologist

Ask this exact narrow question:

> Given the diagnosis, age and weight band, transfusion burden, iron and organ
> status, liver tests, medication list, and local access constraints, is
> mitapivat clinically worth reviewing at all, or should this lane stay paused?

This is a review-readiness question. It is not a request to change treatment.

## Why This Is The Current Blocker

The May 17 source refresh did not create a new case-specific therapy claim.
Instead, it clarified the handoff boundary:

- TIF 2025 keeps TDT interpretation tied to diagnosis, transfusion burden, iron,
  organ, and monitoring context.
- FDA sources keep AQVESME as adult-label evidence with liver-injury and
  interaction constraints.
- ClinicalTrials.gov still separates adult TDT results from pediatric
  no-result watchlist records.

## Required Record Domains

- `diagnosis_genotype_context`
- `age_weight_context`
- `transfusion_burden_context`
- `iron_organ_context`
- `liver_safety_context`
- `medication_interaction_context`
- `local_access_context`

## Allowed Clinician Outcomes

- `review_not_ready_missing_records`
- `not_clinically_relevant_now`
- `review_with_hematologist_only`
- `refer_to_trial_or_access_owner_after_clinician_review`
- `safety_review_required_before_any_discussion`
- `lane_paused_until_pediatric_results_or_recruitment`

## Blocked Claims

- No claim that adult approval establishes pediatric relevance.
- No claim that adult ENERGIZE-T results establish individual response.
- No claim that a pediatric not-yet-recruiting record establishes effectiveness
  or access.
- No dosing, start, stop, transfusion, chelation, supplement, travel, import,
  legal, or trial-eligibility instruction.
- No raw records, screenshots, identifiers, exact private dates, hospital
  names, clinician names, owner replies, or doctor messages in the public repo.

## Biomedical Boundary

This gate does not diagnose subtype, recommend mitapivat, change standard care,
decide eligibility, decide access, or answer safety questions. It only turns
the mitapivat lane into one hematologist-review question and a finite set of
allowed public outcomes.

## Islamic Motivation Boundary

Quran 49:6 supports verifying consequential reports before acting. Quran
55:7-9 supports measured claims and anti-exaggeration. Quran 16:43 supports
qualified expert consultation. These are research-method anchors, not
biomedical evidence.

## Sources

- [Mitapivat clinician-review readiness map](../../../data/regulatory/mitapivat/2026-05-17-mitapivat-clinician-review-readiness-map.json)
- [Case-001 mitapivat evidence-to-action gate](2026-05-16-case001-mitapivat-evidence-to-action-gate.md)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Aqvesme FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/216196s003lbl.pdf)
- [FDA AQVESME approval summary](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [ClinicalTrials.gov NCT04770779](https://clinicaltrials.gov/study/NCT04770779)
- [ClinicalTrials.gov NCT07506863](https://clinicaltrials.gov/study/NCT07506863)
- [ClinicalTrials.gov NCT07517133](https://clinicaltrials.gov/study/NCT07517133)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
