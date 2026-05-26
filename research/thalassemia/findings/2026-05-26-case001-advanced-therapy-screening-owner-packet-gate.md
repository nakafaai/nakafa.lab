# Case-001 Advanced-Therapy Screening Owner Packet Gate

Date checked: 2026-05-26
Evidence label: guideline, regulator, registry, and workflow synthesis, not
medical advice

## Direct Answer

The next blocker is not more trial hunting. The blocker is owner-labeled
packet readiness.

Case-001 remains:

`advanced_therapy_referral_packet_missing`

The May 26 gate adds one practical layer: before asking any hematologist,
transplant center, gene-cell therapy team, or trial owner whether screening is
reasonable, each required domain needs a clear owner and a public-safe label.

## Why This Matters

The TIF 2025 HSCT chapter frames hematopoietic cell transplantation as a
curative option for selected TDT patients, but it also ties the decision to
donor route, iron and organ workup, conditioning, fertility, follow-up, and
expert centers. The TIF 2025 gene-manipulation chapter confirms that gene
addition and gene editing are reshaping curative options, while still requiring
specialist selection and long-term evidence discipline.

FDA pages for Casgevy and Zynteglo establish regulator-recognized product
categories for TDT or regularly transfused beta-thalassemia. They do not prove
Indonesia access, affordability, medical suitability, or individual eligibility.

## Ordered Owner Packet

| Order | Domain | Likely owner | Public-safe output |
| --- | --- | --- | --- |
| 1 | Diagnosis and genotype | Hematologist or genetics owner | `diagnosis_genotype_owner_labeled` |
| 2 | Transfusion burden | Hematologist or transfusion service | `transfusion_burden_owner_labeled` |
| 3 | Immune and blood bank | Blood bank or transfusion medicine | `immune_blood_bank_owner_labeled` |
| 4 | Iron, organ risk, and chelation | Hematology with organ specialists as needed | `iron_organ_chelation_owner_labeled` |
| 5 | Infection, fertility, and transplant readiness | Transplant or advanced-therapy referral team | `infection_fertility_transplant_readiness_owner_labeled` |
| 6 | Donor or HLA context | Hematologist or transplant center | `donor_hla_context_owner_labeled` |
| 7 | Access, center, and payer context | Referral coordinator, center, or payer owner | `access_center_payer_owner_labeled` |

## Allowed Public Labels

- `advanced_therapy_referral_packet_missing`
- `advanced_therapy_referral_packet_partial`
- `advanced_therapy_referral_packet_ready_for_specialist_screening`
- `under_specialist_review`
- `medically_unsuitable`
- `access_blocked`
- `release_blocked_private_material`

## Blocked Jumps

Do not publish trial screening, travel, import, product access, treatment
selection, dose, raw record, doctor-message, owner-reply, hospital-name, or
identifier content.

## Decision Rule

Curative biology is real. Case-specific relevance is still blocked until the
seven owner domains are label-ready and a qualified specialist decides whether
screening is reasonable.

## Islamic Motivation Boundary

Quran 16:43 supports asking qualified experts. Quran 49:6 supports verifying
reports before acting. Quran 55:7-9 supports measured claims. These are
research-method anchors, not biomedical evidence for HSCT, gene therapy,
CRISPR therapy, or any drug.

## Sources

- [May 26 owner-packet workflow map](../../../data/workflows/case-001/2026-05-26-advanced-therapy-screening-owner-packet.json)
- [Case-001 advanced therapy referral readiness gate](2026-04-28-case001-advanced-therapy-referral-readiness-gate.md)
- [May 25 Asia curative gene-cell therapy registry refresh](2026-05-25-asia-curative-gene-cell-therapy-refresh.md)
- [TIF 2025 HSCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [FDA Casgevy product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
