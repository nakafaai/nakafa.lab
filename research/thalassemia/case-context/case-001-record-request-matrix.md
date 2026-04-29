# Case-001 Record Request Matrix

Date: 2026-04-29
Status: de-identified record-request matrix, not treatment advice
Privacy: no raw records, identifiers, local paths, contact details, exact dates,
or patient-specific treatment instructions

## Purpose

This matrix turns the no-lab completion tracker into concrete record requests.
It is designed for private use with a clinician, hospital record desk, blood
bank, or laboratory desk.

The matrix does not diagnose thalassemia subtype, judge treatment suitability,
change therapy, or decide trial eligibility. It only states which record groups
are needed before case-001 can be interpreted safely.

## Current Matrix Label

`case001_record_request_matrix_active`

## Request Matrix

| Request group | Ask for | Why it matters | Private storage | Public release rule | Current label |
| --- | --- | --- | --- | --- | --- |
| Diagnosis and genotype | Current diagnosis note; HPLC or electrophoresis fractions; whether the historical hemoglobin analysis was pre-transfusion; `HBB` sequencing or targeted mutation result; deletion/duplication follow-up if needed; `HBA1/HBA2` deletion, duplication, sequence, and copy-number context if available; HPFH, delta-beta-thalassemia, `HBG1/HBG2`, XmnI-HBG2, `BCL11A`, or `HBS1L-MYB` modifier results if available. | Subtype uncertainty can misroute nearly every downstream claim: TDT versus NTDT, HbE/beta-thalassemia, alpha-thalassemia coinheritance, and HbF modifier biology change the interpretation of candidates and referrals. | Store raw reports only in ignored private storage. Public repo may keep only de-identified labels and missing-record status. | Do not publish specific variants, dates, facility names, accession numbers, or report text until the release checklist passes. | `phenotype_only` |
| Transfusion burden | Transfusion dates, body weight, transfused volume, product type, red-cell fraction or unit hematocrit, pre-transfusion Hb, post-transfusion Hb if available, reactions, interval, and whether weekly visits reflect high total requirement or small per-visit volume. | Annual `ml/kg/year`, pure red-cell volume, Hb increment, and estimated iron input are needed before transfusion burden or disease-modifying endpoints can be compared. | Use `templates/transfusion-log-template.csv` privately, then run `scripts/calc_transfusion_burden.py` on de-identified rows. | Public repo may show only calculated labels or ranges after privacy review, not raw dates or visit-level records. | `transfusion_burden_unknown` |
| Immune and blood-bank | ABO/Rh/Kell; extended matching policy; antibody screen; named alloantibodies; DAT/direct Coombs with IgG/C3 specificity if available; red-cell phenotype or genotype; crossmatch difficulty; delayed reaction history; post-transfusion hemolysis workups. | Alloimmunization, autoimmunity, shortened donor-RBC survival, and crossmatch difficulty can explain high transfusion needs and can block or change referral questions. | Index record aliases privately with `templates/clinical-record-index-template.csv`; do not copy full blood-bank reports into Git. | Public repo may only record whether the packet is missing, partial, or clinician-reviewed. | `immune_transfusion_packet_missing` |
| Iron, chelation, and organ risk | Ferritin trend; liver iron concentration MRI; cardiac `T2*` MRI; chelator identity; dose schedule as written in the record; adherence notes; side effects; kidney, liver, blood-count, hearing, eye, GI, endocrine, bone, cardiac, liver, and infection monitoring as applicable. | Transfusion intensity and chelation context cannot be interpreted without iron distribution and organ-risk monitoring. Advanced options also depend on organ status. | Store raw labs and imaging reports only in ignored private storage. Public repo should keep only packet status and source aliases. | Do not publish exact values, image text, dates, or medication details unless a clinician and release checklist approve a de-identified summary. | `iron_packet_missing` |
| Advanced-therapy and referral readiness | Prior discussion, referral, trial screening, rejection, or access barrier for HSCT, gene therapy, CRISPR therapy, luspatercept, mitapivat, hydroxyurea, or other advanced options; exact reason if blocked. | These options are real benchmark lanes, but suitability cannot be inferred without subtype, transfusion, immune, iron, organ, infection, fertility, cost, and center-access context. | Use the advanced-therapy referral readiness template privately or as de-identified labels only. | Public repo may record only readiness labels such as missing, partial, ready for specialist screening, medically unsuitable, access-blocked, or under review. | `advanced_therapy_referral_packet_missing` |
| Private source index | Source alias, record type, owner, private storage alias, extraction status, and whether the source is safe to summarize. | The repo needs traceability without exposing raw medical records or local file paths. | Keep the raw index under ignored `private/` storage. Use aliases in public artifacts. | No public case update until the public case data release checklist passes. | `private_intake_index_needed` |
| Public release review | De-identified extraction worksheet, identifier review, date review, clinical-claim boundary review, and repo checks. | Public research notes must not leak protected health information or turn private records into treatment advice. | Keep extraction notes private until reviewed. | Public updates require `scripts/check_public_repo.py`, `scripts/check_repo_language.py`, and manual review. | `release_check_required` |

## Request Order

1. Diagnosis and genotype.
2. Transfusion burden and response.
3. Immune and blood-bank.
4. Iron, chelation, and organ risk.
5. Advanced-therapy and referral readiness.
6. Private source index.
7. Public release review.

## Do Not Ask This Matrix To Decide

- Whether to change transfusion frequency or volume.
- Whether to change chelation, immune medicines, supplements, diet, or any
  other treatment.
- Whether a specific drug, transplant, gene therapy, CRISPR therapy, or trial is
  suitable for case-001.
- Whether a private lab result proves or disproves a candidate hypothesis.

Those are clinician-review questions. This matrix only organizes missing
records.

## Evidence Boundaries

Biomedical basis: subtype, transfusion burden, alloimmunization and DAT context,
iron overload monitoring, and organ-risk data are prerequisite facts for
interpreting severity, care burden, and referral readiness. This is not a cure
claim.

Islamic motivation: Quran anchors are used only as research-method guardrails
for expert consultation, balance, and honest measurement, not as biomedical
evidence.

## Source-Backed Gates

- [Case-001 no-lab completion tracker](case-001-no-lab-completion-tracker.md) and [minimum hematologist packet](case-001-minimum-hematologist-packet.md)
- [No-lab execution ladder](../findings/2026-04-29-no-lab-execution-ladder.md)
- [Case-001 record request matrix gate](../findings/2026-04-29-case001-record-request-matrix-gate.md)
- [Private case intake workspace gate](../findings/2026-04-28-private-case-intake-workspace-gate.md)
- [Public case data release gate](../findings/2026-04-28-public-case-data-release-gate.md)
- TIF 2025 chapters: [blood transfusion](https://www.ncbi.nlm.nih.gov/books/NBK614240/), [iron overload](https://www.ncbi.nlm.nih.gov/books/NBK614244/), and [monitoring](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [HHS HIPAA de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/privacy/special-topics/de-identification/index.html)
- Quran anchors: [16:43](../../islamic/quran/016-an-nahl/043.md) and [55:7-9](../../islamic/quran/055-ar-rahman/007-009.md)
