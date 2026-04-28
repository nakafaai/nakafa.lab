# Case-001 Minimum Hematologist Packet

Date: 2026-04-28
Status: de-identified clinician-preparation packet, not treatment advice
Privacy: no name, address, hospital ID, phone, photo, exact birth date, or raw
medical-record text

## Purpose

This packet compresses the case-001 research gates into one doctor-readable
checklist. The goal is to help a hematologist decide which records are present,
missing, not applicable, or impossible to retrieve.

This packet must not be used to change transfusion, chelation, immune medicine,
supplements, diet, or any treatment plan.

## Current Working Labels

| Area | Current label | Meaning |
| --- | --- | --- |
| Diagnosis | `phenotype_only` | Historical records support a beta-thalassemia phenotype, but molecular subtype is not yet documented. |
| Transfusion burden | `transfusion_burden_unknown` | Weekly transfusion is reported, but annual `ml/kg/year`, pure red-cell volume, Hb increment, and iron input are not yet documented. |
| Immune/transfusion | `immune_transfusion_packet_missing` | Weekly transfusion plus reported autoimmune history cannot be interpreted without blood-bank and DAT records. |
| Iron/chelation | `iron_packet_missing` | Weekly transfusion plus reported daily chelation cannot be interpreted without ferritin trend, LIC, cardiac `T2*`, chelator identity, and toxicity monitoring. |
| Trial/referral | `trial_referral_not_ready` | Referral or trial screening cannot be judged until subtype, transfusion, immune, iron, organ, and access records are known. |

## Bring Or Request First

1. Diagnosis and genotype packet:
   - current diagnosis note and phenotype: `TDT`, `NTDT`, HbE/beta-thalassemia,
     alpha-thalassemia, or mixed disease;
   - current HPLC or electrophoresis fractions: HbA, HbA2, HbF, HbE if present;
   - whether the historical hemoglobin analysis was before any transfusion;
   - `HBB` sequence or targeted mutation result, with deletion/duplication
     follow-up if sequencing is incomplete;
   - `HBA1/HBA2` deletion, duplication, sequence, and alpha-globin copy-number
     context if available;
   - any HPFH, delta-beta-thalassemia, `HBG1/HBG2`, XmnI-HBG2, `BCL11A`, or
     `HBS1L-MYB` modifier result if available.
2. Transfusion burden and response packet:
   - dates, pre-transfusion hemoglobin, units, volume, body weight, product
     type, reactions, and interval;
   - annual `ml/kg/year`, pure red-cell volume, unit hematocrit or red-cell
     fraction, and estimated transfusional iron input if the clinic can
     calculate it;
   - post-transfusion hemoglobin or Hb increment if available;
   - whether weekly visits reflect high total requirement, low volume per visit,
     poor Hb increment, shortened donor RBC survival, or scheduling.
3. Immune and blood-bank packet:
   - ABO/Rh/Kell and extended matching policy;
   - antibody screen, named alloantibodies, DAT/direct Coombs with IgG/C3
     specificity if available;
   - red-cell phenotype or genotype, crossmatch difficulty, delayed reaction
     history, and post-transfusion hemolysis workups.
4. Iron, chelation, and organ-risk packet:
   - serial ferritin values with dates and inflammation/infection/hepatitis
     context;
   - liver iron concentration MRI and cardiac `T2*` MRI with date and method;
   - chelator name, dose, schedule, adherence, side effects, and monitoring;
   - kidney, liver, blood-count, hearing, eye, GI, and interaction checks as
     relevant to the exact chelator;
   - endocrine and bone screen: glucose, thyroid, parathyroid, gonadal axis,
     vitamin D, growth/puberty history if relevant, and bone health.
5. Autoimmune, spleen, and infection context:
   - exact autoimmune diagnosis, tests, symptoms, medicines, and specialist
     notes;
   - spleen size/status, hypersplenism clues, platelet/WBC trend, and hemolysis
     markers;
   - infection, vaccination, hepatitis, liver-virus, and inflammation context.
6. Advanced-therapy and referral history:
   - whether luspatercept, mitapivat, hydroxyurea, HSCT, gene therapy, CRISPR
     therapy, or trial referral has been considered, tried, rejected, or blocked;
   - if rejected or blocked, the exact reason: genotype, organ status, immune
     risk, antibodies, infection, fertility, cost, center access, or another
     reason.

## Doctor Visit Script

Use this wording to keep the visit focused:

> We are not asking to change treatment today. We want to understand why weekly
> transfusion is needed and which records are missing before advanced options or
> research ideas can be judged safely.

Then ask:

1. Which current labels are correct, and which are wrong?
2. Which missing records should we request first from the hospital or blood bank?
3. Are any records unnecessary for this case, and why?
4. Is this case screenable for referral or trial review, or still
   `trial_referral_not_ready`?

## Research Routing Rule

Until a hematologist reviews this packet, keep all patient-specific candidate
claims blocked. Nakafa Lab can continue computational ranking and assay design,
but every candidate remains `patient_relevance_blocked` for case-001.

## Public Release Rule

Before adding new case-001 facts to the public repo, use the
[public case data release checklist](../../../templates/public-case-data-release-checklist.md).
Raw records, scans, photos, identifiers, and local file paths stay outside Git.

## Notebook

- [Case-001 minimum hematologist packet gate notebook](../notebooks/2026-04-28-case001-minimum-hematologist-packet-gate.ipynb)

## Source-Backed Gates

- [Case-001 high-HbF genotype evidence gate](../findings/2026-04-28-case001-high-hbf-genotype-evidence-gate.md)
- [Case-001 molecular test escalation gate](../findings/2026-04-28-case001-molecular-test-escalation-gate.md)
- [Case-001 transfusion burden quantification gate](../findings/2026-04-28-case001-transfusion-burden-quantification-gate.md)
- [Case-001 immune transfusion record gate](../findings/2026-04-28-case001-immune-transfusion-record-gate.md)
- [Case-001 iron chelation organ-risk record gate](../findings/2026-04-28-case001-iron-chelation-organ-risk-record-gate.md)
- [Public case data release gate](../findings/2026-04-28-public-case-data-release-gate.md)
- [Case-001 research routing matrix](case-001-research-routing-v0.md)
- [Trial referral no-lab gate](../findings/2026-04-27-trial-referral-no-lab-gate.md)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [GeneReviews alpha-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1435/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
