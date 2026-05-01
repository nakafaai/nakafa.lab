# Case-001 Doctor Handoff Brief

Date: 2026-04-30
Status: de-identified doctor-facing brief, not treatment advice
Privacy: no raw records, identifiers, local paths, contact details, exact dates,
or patient-specific treatment instructions

## Purpose

This brief is for a hematologist or thalassemia clinician. It turns Nakafa Lab's
case-001 work into a short clinical validation request.

The goal is not to ask the doctor to approve Nakafa Lab as a research program.
The goal is to ask the doctor to validate labels, identify missing records, and
state whether the case is ready for specialist or advanced-therapy review.

## Current Public-Safe Working Labels

| Area | Current label | What needs validation |
| --- | --- | --- |
| Clinical dependence | `transfusion_dependent_reported` | Confirm whether the current clinical label should be TDT, NTDT with regular transfusion, HbE/beta-thalassemia, or another label. |
| Diagnosis | `phenotype_only` | Historical hemoglobin analysis supports beta-thalassemia phenotype, but molecular subtype is not documented in the public packet. |
| Transfusion burden | `transfusion_dependent_burden_unquantified` | Weekly transfusion is reported, but annual `ml/kg/year`, pure red-cell volume, Hb increment, and iron input are not quantified. |
| Immune and blood-bank | `immune_transfusion_packet_missing` | Antibody screen, DAT/direct Coombs specificity, red-cell phenotype/genotype, matching policy, and hemolysis workup are not yet packeted. |
| Iron, chelation, and organ risk | `iron_packet_missing` | Daily chelation is reported, but ferritin trend, LIC MRI, cardiac `T2*`, chelator monitoring, and organ-risk screen are not yet packeted. |
| Referral readiness | `advanced_therapy_referral_packet_missing` | HSCT, gene therapy, CRISPR therapy, luspatercept, mitapivat, hydroxyurea, or trial review cannot be judged from the public packet. |

## Doctor Validation Request

Please help answer these labels, not treatment changes:

1. What is the current best diagnosis label and subtype?
2. Is the current state best described as TDT, NTDT with regular transfusion, or
   another category?
3. Why is the current transfusion interval so short: high total requirement,
   small per-visit volume, poor Hb increment, hemolysis, spleen/hypersplenism,
   antibody/crossmatch issue, scheduling, or another cause?
4. Which missing records should be requested first from the hospital, blood
   bank, or laboratory?
5. Is the case ready for advanced-therapy or trial specialist screening, or is
   it still data-missing?

## Records To Bring Or Request

- Historical thalassemia screen and early hematology labs.
- Current diagnosis note and current HPLC/electrophoresis if available.
- `HBB` molecular result; `HBA1/HBA2` result if available or clinically needed.
- Transfusion dates, body weight, volume, product type, pre-transfusion Hb,
  post-transfusion Hb if available, interval, and reactions.
- ABO/Rh/Kell, extended matching policy, antibody screen, named antibodies,
  DAT/direct Coombs with IgG/C3 specificity if available, crossmatch problems,
  and hemolysis workup.
- Ferritin trend, LIC MRI, cardiac `T2*`, chelator name, prescribed schedule,
  adherence notes, side effects, and kidney/liver/blood-count/hearing/eye/GI,
  endocrine, bone, cardiac, liver, and infection monitoring as applicable.
- Any prior discussion, referral, rejection, or access barrier for HSCT, gene
  therapy, CRISPR therapy, luspatercept, mitapivat, hydroxyurea, or trials.

## What We Are Not Asking

- Do not change transfusion, chelation, immune medicines, supplements, diet, or
  referral plan based on this brief.
- Do not treat this brief as diagnosis, dosing, eligibility, or treatment
  advice.
- Do not put raw medical records in the public repository.

## Parallel Work While Waiting

Nakafa Lab can continue non-clinical work in parallel:

1. privately index records by source alias;
2. build a de-identified transfusion-burden table;
3. calculate annual transfusion burden once enough fields are available;
4. prepare blood-bank and iron-risk packets;
5. keep all candidate claims blocked from patient relevance until clinician
   review.

## Source-Backed Gates

- [Case-001 record request matrix](case-001-record-request-matrix.md)
- [Case-001 no-lab completion tracker](case-001-no-lab-completion-tracker.md)
- [Case-001 minimum hematologist packet](case-001-minimum-hematologist-packet.md)
- [Doctor handoff sprint gate](../findings/2026-04-30-case001-doctor-handoff-sprint-gate.md)
- [Transfusion burden readiness gate](../findings/2026-05-01-case001-transfusion-burden-readiness-gate.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
