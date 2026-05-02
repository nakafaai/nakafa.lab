# Case-001 No-Lab Completion Tracker

Date: 2026-04-29
Status: de-identified tracker, not treatment advice
Privacy: no raw records, identifiers, local paths, contact details, exact dates,
or patient-specific treatment instructions

## Purpose

This tracker turns the no-lab execution ladder into a small public-safe work
queue. It shows which record domains remain blocked before a hematologist can
review the case packet.

This file must not be used to change transfusion, chelation, immune medicine,
diet, supplements, referral, or any therapy plan.

## Current Tracker Label

`case001_no_lab_completion_tracker_active`

## Completion Domains

| Domain | Current label | Public-safe next action | Public update allowed? |
| --- | --- | --- | --- |
| Diagnosis and genotype | `phenotype_only` | Privately index current diagnosis note, HPLC/electrophoresis, `HBB`, `HBA1/HBA2`, and HbF-modifier records if available. | No |
| Transfusion burden | `transfusion_dependent_burden_unquantified` | Use de-identified private logs to calculate dates, weight, volume, red-cell fraction, pre/post Hb, `ml/kg/year`, and estimated iron input. | No |
| Immune and blood-bank | `immune_transfusion_packet_missing` | Privately request or index antibody screen, named antibodies, DAT/direct Coombs specificity, matching policy, red-cell phenotype/genotype, reactions, and hemolysis workup. | No |
| Iron, chelation, and organ risk | `iron_packet_missing` | Privately index ferritin trend, LIC MRI, cardiac `T2*`, chelator identity, adherence, toxicity monitoring, and organ-risk screen. | No |
| Advanced-therapy referral | `advanced_therapy_referral_packet_missing` | Ask only whether the packet is not ready, partial, ready for specialist screening, medically unsuitable, access-blocked, or under review. | No |
| Private intake | `private_intake_index_needed` | Complete an ignored private source index using source aliases, not local file paths. | No |
| Public release | `release_check_required` | Use the release checklist and extraction template before any public case update. | No |

## Record Request Order

1. Current diagnosis and molecular context.
2. Transfusion-burden and response data.
3. Immune and blood-bank records.
4. Iron, chelation, and organ-risk records.
5. Advanced-therapy or trial referral-readiness labels.
6. Public-release review for any de-identified summary.

Use the [case-001 record request matrix](case-001-record-request-matrix.md) as
the exact public-safe request layer for these domains. It should remain a list
of asks and labels, not a repository for raw medical facts.

Use the [case-001 doctor handoff brief](case-001-doctor-handoff-brief.md) for
the clinician conversation. The main paper remains a research appendix, not the
first doctor-facing document.

## Public Release Rule

No new case fact should enter the public repo until it passes:

1. private source indexing;
2. private-to-public extraction;
3. identifier and date review;
4. clinical-claim boundary review;
5. public case data release checklist;
6. `scripts/check_public_repo.py`;
7. `scripts/check_repo_language.py`.

## Clinician-Review Boundary

Until a hematologist reviews the packet, keep all patient-specific candidate
claims as `patient_relevance_blocked`.

The tracker can support better questions. It cannot diagnose, dose, select
therapy, change transfusion, change chelation, change immune medicines,
recommend supplements, or decide trial eligibility.

## Source-Backed Gates

- [No-lab execution ladder](../findings/2026-04-29-no-lab-execution-ladder.md)
- [Case-001 minimum hematologist packet](case-001-minimum-hematologist-packet.md)
- [Case-001 record request matrix](case-001-record-request-matrix.md)
- [Case-001 record request matrix gate](../findings/2026-04-29-case001-record-request-matrix-gate.md)
- [Case-001 doctor handoff brief](case-001-doctor-handoff-brief.md)
- [Case-001 doctor response triage](case-001-doctor-response-triage.md)
- [Case-001 doctor handoff sprint gate](../findings/2026-04-30-case001-doctor-handoff-sprint-gate.md)
- [Private case intake workspace gate](../findings/2026-04-28-private-case-intake-workspace-gate.md)
- [Public case data release gate](../findings/2026-04-28-public-case-data-release-gate.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [Private case intake index template](../../../templates/private-case-intake-index-template.md)
- [Private-to-public extraction template](../../../templates/private-to-public-case-extraction-template.md)
- [Public case data release checklist](../../../templates/public-case-data-release-checklist.md)
- [No-lab completion tracker notebook](../notebooks/2026-04-29-case001-no-lab-completion-tracker.ipynb)
- [Record request matrix notebook](../notebooks/2026-04-29-case001-record-request-matrix.ipynb)
