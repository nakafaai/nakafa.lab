# Case-001 Doctor Handoff Sprint Gate

Date checked: 2026-04-30
Evidence label: operational clinician-handoff gate, not medical advice

## Direct Answer

The current blocker is not passive waiting for a doctor. The doctor should be
used as a label validator while record collection, de-identified data entry,
and research outreach continue in parallel.

The updated operational label is:

`case001_doctor_handoff_sprint_active`

## Why This Matters

Caregiver context already supports a public-safe working label of reported
transfusion dependence, but the actionable problem is still unquantified:

- diagnosis is phenotype-level, not molecularly resolved in the public packet;
- transfusion dependence is reported, but annual burden and Hb response are not
  quantified;
- immune and blood-bank risk is not packeted;
- iron, chelation, and organ-risk context is not packeted;
- advanced-therapy or trial readiness remains a specialist-screening question.

## Two-Week Sprint

| Track | Owner | Output | Stop condition |
| --- | --- | --- | --- |
| Clinician validation | Hematologist or thalassemia clinician | Corrected labels and missing-record list | Doctor states labels are validated or cannot be validated without named records. |
| Record collection | Family/private workspace | Private source index and record aliases | Diagnosis, transfusion, blood-bank, iron, and chelation records are indexed or marked unavailable. |
| Data engineering | Nakafa Lab/private workspace | De-identified transfusion-burden table | Dates, weight, volume, red-cell fraction, pre-Hb, post-Hb if available, and reactions are entered. |
| Research outreach | Founder | Specialist, blood-bank, genetics, trial/access, and wet-lab contacts | At least one qualified reviewer or lab partner gives a concrete next step. |

## Doctor-Facing Ask

Use the
[case-001 doctor handoff brief](../case-context/case-001-doctor-handoff-brief.md)
instead of the main paper as the first clinical document. The main paper is for
research collaborators, reviewers, donors, and lab partners.

## Biomedical Boundary

This gate does not diagnose, dose, select therapy, change transfusion, change
chelation, change immune medicines, recommend supplements, or decide trial
eligibility. It only defines the next structured workflow.

## Islamic Motivation Boundary

Quran 16:43 motivates expert consultation. Quran 55:7-9 motivates balanced
measurement and anti-exaggeration. These are research-discipline anchors, not
biomedical evidence.

## Decision

Keep all patient-specific candidate claims as `patient_relevance_blocked` until
a qualified clinician reviews the packet. Continue computational and outreach
work only as research context.

## Sources

- [Case-001 doctor handoff brief](../case-context/case-001-doctor-handoff-brief.md)
- [Case-001 record request matrix](../case-context/case-001-record-request-matrix.md)
- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
