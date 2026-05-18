# Case-001 Mitapivat Clinician Answer Action Ladder

Date: 2026-05-18
Status: public-safe response handling aid, not treatment advice
Privacy: no raw clinician replies, raw records, screenshots, identifiers, exact
dates, contact details, or patient-specific instructions

## Purpose

Use this after a hematologist answers the May 17 mitapivat review-readiness
question. The goal is to convert the answer into a safe next research state.

Current label: `mitapivat_clinician_answer_action_ladder_ready`

## How To Record The Answer

Choose one input label:

- `review_not_ready_missing_records`
- `not_clinically_relevant_now`
- `review_with_hematologist_only`
- `refer_to_trial_or_access_owner_after_clinician_review`
- `safety_review_required_before_any_discussion`
- `lane_paused_until_pediatric_results_or_recruitment`

Then record only:

- the input label;
- missing record-domain labels, if any;
- owner category, if named;
- public source URL, if named;
- private action;
- public repo action.

## What Not To Record Publicly

- raw doctor message;
- doctor, hospital, owner, email, phone, or location details;
- exact private dates or screenshots;
- raw lab values or medical-record text;
- treatment, dosing, transfusion, chelation, import, travel, or access
  instructions.

## Source-Backed Gates

- [Case-001 mitapivat clinician-answer action ladder gate](../findings/2026-05-18-case001-mitapivat-clinician-answer-action-ladder.md)
- [Case-001 mitapivat clinician-review readiness](case-001-mitapivat-clinician-review-readiness.md)
- [Case-001 mitapivat response capture](case-001-mitapivat-response-capture.md)
