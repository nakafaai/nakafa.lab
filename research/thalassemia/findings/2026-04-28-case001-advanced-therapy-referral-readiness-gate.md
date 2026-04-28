# Finding: Case-001 Advanced Therapy Referral Readiness Gate

Date checked: 2026-04-28
Status: de-identified referral-readiness gate, not treatment advice
Evidence label: guideline, regulator, registry, and case-packet synthesis

## Bottom Line

Case-001 should carry the label
`advanced_therapy_referral_packet_missing`.

That means Nakafa Lab can discuss HSCT, gene therapy, CRISPR therapy,
luspatercept, mitapivat, hydroxyurea, and trials as evidence-backed categories,
but cannot call case-001 eligible, ineligible, suitable, unsuitable,
screenable, or access-blocked. The next no-lab action is a specialist-readable
record packet, not a therapy decision.

## Why This Gate Exists

Advanced options already exist, but they are gated by subtype, transfusion
burden, organ risk, immune risk, center capacity, and access. Asking a center
"can this patient get advanced therapy?" before those records are organized can
create false hope or false rejection.

The stronger question is:

> Which records must be complete before a hematologist or referral center can
> screen case-001 for existing advanced options?

## Current Evidence Map

| Lane | Source-backed signal | Case-001 implication |
| --- | --- | --- |
| HSCT | TIF 2025 frames HCT as curative for selected TDT patients, but dependent on donor route, iron/organ workup, conditioning, follow-up, and expert centers. | Ask whether evaluation is appropriate only after subtype, donor, organ-risk, infection, fertility, and access records are organized. |
| Gene addition | FDA lists Zynteglo for beta-thalassemia patients requiring regular RBC transfusions; TIF gene-manipulation guidance frames it as autologous HSPC collection, manufacturing, myeloablation, infusion, and follow-up. | Product indication does not equal local availability or patient eligibility. |
| Gene editing / CRISPR | FDA lists Casgevy for TDT in patients 12 years and older; NICE keeps exa-cel under managed-access and uncertainty boundaries. | Treat as a referral-center question, not a repo decision. |
| Disease-modifying drugs | FDA luspatercept approval and phase 3 evidence support adult beta-thalassemia transfusion-burden reduction; mitapivat remains a benchmark with monitoring constraints. | Requires confirmed subtype, baseline burden, spleen/immune context, response definition, monitoring, and access review. |
| Asia signals | A 2026 China multicenter HSCT trial plus China gene-therapy registry records show strong regional activity. | Continue Asia-aware scouting, but do not infer case-specific eligibility. |

## Minimum Packet

Before advanced-option screening, mark these areas as present, unavailable, or
not clinically needed:

1. diagnosis, TDT/NTDT category, HbE/beta or mixed-disease context, `HBB`,
   `HBA1/HBA2`, alpha-globin copy number, and HbF modifiers;
2. transfusion dates, product type, units or volume, body weight, pre/post Hb,
   reactions, annual `ml/kg/year`, pure red-cell volume, and iron input;
3. ABO/Rh/Kell, extended matching, antibody screen, named alloantibodies,
   DAT/direct Coombs, red-cell phenotype/genotype, and reaction history;
4. ferritin trend, LIC MRI, cardiac `T2*`, chelator identity, toxicity
   monitoring, organ screening, and inflammation or hepatitis context;
5. infection, vaccination, spleen, fertility, prior advanced-therapy review,
   HLA or donor discussion when clinician-led, and access constraints.

## Decision Labels

| Label | Meaning |
| --- | --- |
| `advanced_therapy_referral_packet_missing` | Core records are not organized enough for high-quality screening. |
| `advanced_therapy_referral_packet_partial` | Some records exist, but blockers remain. |
| `advanced_therapy_referral_packet_ready_for_specialist_screening` | Records are organized enough to ask a specialist whether screening is reasonable. |
| `under_specialist_review` | Specialist review is active; the repo should not speculate. |
| `medically_unsuitable` | A clinician documents a medical reason an option is not appropriate. |
| `access_blocked` | A clinician or center considers the option plausible, but cost, center access, payer, geography, or registry access blocks it. |

Current case-001 label: `advanced_therapy_referral_packet_missing`.

## Boundary

This finding does not recommend HSCT, gene therapy, CRISPR therapy,
luspatercept, mitapivat, hydroxyurea, or any trial. Quran 16:43 and Quran
55:7-9 are ethical-method anchors for expert consultation and measurement; they
are not biomedical evidence for any therapy.

## Sources

- [Case-001 advanced therapy referral readiness notebook](../notebooks/2026-04-28-case001-advanced-therapy-referral-readiness-gate.ipynb)
- [Advanced therapy referral readiness template](../../../templates/advanced-therapy-referral-readiness-template.md)
- [TIF 2025 HSCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [FDA Casgevy](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [FDA luspatercept beta-thalassemia approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-luspatercept-aamt-anemia-patients-beta-thalassemia)
- [NICE exagamglogene autotemcel appraisal](https://www.ncbi.nlm.nih.gov/books/NBK610907/)
- [Exagamglogene autotemcel in TDT, PMID 38657265](https://pubmed.ncbi.nlm.nih.gov/38657265/)
- [Betibeglogene autotemcel in beta-thalassemia, PMID 34891223](https://pubmed.ncbi.nlm.nih.gov/34891223/)
- [China multicenter allo-HSCT TDT trial](https://www.nature.com/articles/s41467-026-69756-8)
- [China KL003 gene-therapy registry record, NCT06219239](https://clinicaltrials.gov/study/NCT06219239)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
