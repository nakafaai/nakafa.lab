# Case-001 Record Request Matrix Gate

Date checked: 2026-04-29
Evidence label: operational case-record gate, not medical advice

## Direct Answer

The next highest-value blocker is no longer another candidate claim. It is a
record request matrix that turns the case-001 tracker into concrete, private
record requests.

The output is a diagnosis/genotype request, transfusion-burden request,
immune/blood-bank request, iron/chelation/organ-risk request,
advanced-therapy-readiness request, private source index request, and public
release gate. It does not interpret the patient's records and does not
recommend treatment.

## Why This Matters

Current thalassemia interpretation depends on facts that are still blocked for
case-001: subtype and genotype context; actual transfusion burden rather than
reported visit frequency alone; immune and blood-bank context; iron,
chelation, and organ-risk monitoring; and specialist readiness for HSCT, gene
therapy, CRISPR therapy, luspatercept, mitapivat, hydroxyurea, or trial review.

Without those records, any patient-specific candidate claim remains
`patient_relevance_blocked`.

## Practical Output

Use the
[case-001 record request matrix](../case-context/case-001-record-request-matrix.md)
as the public-safe request layer between the no-lab tracker and private record
collection.

The matrix should be used to ask for records privately. Raw reports, identifiers,
local paths, exact dates, and full lab text must stay out of the public repo.

## Privacy Gate

The matrix follows the existing private-intake threat model and HHS
de-identification boundary: public artifacts can track labels, missing domains,
and source aliases, but not raw medical records or identifiers.

Before any new case fact enters Git, run the public release checklist and the
public-repo checks.

## Biomedical Boundary

This gate is not a new cure hypothesis. It is a prerequisite gate for
interpreting cure-oriented research responsibly.

It does not provide diagnosis, dosing, transfusion changes, chelation changes,
immune-medicine changes, supplement advice, referral decisions, or trial
eligibility.

## Islamic Motivation Boundary

Quran 16:43 supports asking qualified people when the team does not know. Quran
55:7-9 supports balance and honest measurement. These anchors motivate research
discipline only; they are not biomedical evidence.

## Decision

`case001_record_request_matrix_active`

Do not promote any candidate to patient relevance until the matrix-backed packet
is completed privately and reviewed by a qualified hematologist.

## Sources

- [Case-001 no-lab completion tracker](../case-context/case-001-no-lab-completion-tracker.md)
- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)
- [No-lab execution ladder](2026-04-29-no-lab-execution-ladder.md)
- [Private case intake workspace gate](2026-04-28-private-case-intake-workspace-gate.md)
- [Public case data release gate](2026-04-28-public-case-data-release-gate.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [HHS HIPAA de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
