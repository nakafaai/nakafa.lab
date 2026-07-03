# Case-001 Doctor Handoff Brief

Date updated: 2026-07-02
Status: de-identified doctor-facing branch-review brief, not treatment advice
Privacy: no raw records, identifiers, local paths, contact details, exact dates,
or patient-specific treatment instructions

## Purpose

This brief is for a hematologist or thalassemia clinician. It turns Nakafa Lab's
case-001 work into one ordered clinical validation request.

The goal is not to ask the doctor to approve Nakafa Lab as a research program
or choose a treatment from the public repo. The goal is to ask the doctor to
validate whether the private packet is complete enough for branch review, name
missing records, and state which clinical owner should review the next packet.

## Send This First

Do not send `paper/build/main.pdf` as the first doctor-facing document. The main
paper is a research evidence map, so it starts with benchmarks, registries, and
research methods. That is useful as an appendix only if the clinician asks for
the broader research rationale.

Use this order for a doctor conversation:

1. this handoff brief or the compiled doctor handoff PDF;
2. the private original lab and screening PDFs;
3. any current transfusion, chelation, blood-bank, iron, organ-risk, and
   autoimmune records;
4. the main paper only as an optional research appendix.

If the clinician asks what exactly should be confirmed, use this order:

1. Are the six private packet domains complete enough to review?
2. If not, which domains are missing and who owns them?
3. If complete, which branch is in scope to discuss privately?
4. If a reply is given, reduce it to public-safe labels before any repo update.

## Current Public Handoff State

Current public-safe handoff label:

`branch_review_handoff_packet_incomplete`

That means the public repo cannot yet ask for a branch decision. The useful
doctor question is whether the private packet is complete enough, and if not,
which exact domains must be completed first.

## Six Packet Domains To Confirm

| Domain | Public label if missing | What needs validation |
| --- | --- | --- |
| Diagnosis, genotype, phenotype | `missing_diagnosis_genotype_phenotype` | Confirm diagnosis category, molecular subtype, and whether HbF/HPFH or alpha-globin context changes interpretation. |
| Transfusion burden and response | `missing_transfusion_burden_response` | Confirm dates, volume, body weight, product type, pre-transfusion Hb, Hb increment, interval, and annualized burden. |
| Blood-bank and immune history | `missing_blood_bank_immune_history` | Confirm antibody screen, DAT/direct Coombs context, red-cell phenotype/genotype, matching policy, reactions, spleen context, and hemolysis workup. |
| Iron, organ-risk, chelation status | `missing_iron_organ_chelation_status` | Confirm ferritin trend, LIC MRI, cardiac `T2*`, chelator identity, toxicity monitoring, and organ-risk notes. |
| HCT/gene-cell access context | `missing_hct_gene_cell_access_context` | Confirm HLA/donor context, transplant or gene-cell center access, payer path, geography, travel constraints, and fertility counseling status. |
| Consent, ethics, owner review | `missing_consent_ethics_private_owner_review` | Confirm family consent boundaries, private-record handling, and which qualified owner can answer each branch question. |

## Doctor Validation Request

Please help answer the packet and branch-review state, not treatment changes:

1. Which of the six packet domains are complete enough for review?
2. Which domains are missing, and where should the family request those
   records?
3. If the packet is complete enough, are any branches in scope for private
   specialist discussion: allogeneic HCT, autologous gene-cell therapy,
   non-curative disease modification, standard-care stabilization first, or
   benchmark-only tracking?
4. If the packet is not complete, should standard-care stabilization or a
   safety issue be reviewed first?
5. Which clinical owner should review the next packet: hematology, transfusion
   medicine, genetics, iron/organ-risk specialist, transplant or gene-cell
   center, or another service?

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
- Any prior discussion, referral, rejection, or access barrier for HSCT,
  gene-cell therapy, CRISPR/base-editing therapy, luspatercept, mitapivat,
  hydroxyurea, or trials.

## Output Needed From The Doctor

Please return a short answer using labels or brief notes:

1. packet complete enough for branch discussion, or packet incomplete;
2. missing domains, if any;
3. branch in scope for private specialist review, branch out of scope,
   stabilization first, benchmark-only, or cannot answer from packet;
4. first missing records the family should request;
5. next clinical owner.

After the doctor replies, use the
[branch review response capture gate](case-001-branch-review-response-capture-gate.md)
and [handoff status gate](case-001-branch-review-handoff-status-gate.md) before
any public update. Do not publish raw chat text, screenshots, clinician names,
hospital names, or patient-specific treatment instructions.

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

- [Case-001 minimum hematologist packet](case-001-minimum-hematologist-packet.md)
- [Case-001 clinician confirmation packet index](case-001-clinician-confirmation-packet-index.md)
- [Case-001 branch review minimum packet gate](case-001-branch-review-minimum-packet-gate.md)
- [Case-001 branch review handoff status gate](case-001-branch-review-handoff-status-gate.md)
- [Case-001 branch review clinician brief gate](case-001-branch-review-clinician-brief-gate.md)
- [Doctor handoff sprint gate](../findings/2026-04-30-case001-doctor-handoff-sprint-gate.md)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [July 2 branch-review clinician brief refresh](../../../data/literature/pubmed/2026-07-02-branch-review-clinician-brief-refresh.json)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 owner-routing anchor](../../islamic/quran/004-an-nisa/058.md)
