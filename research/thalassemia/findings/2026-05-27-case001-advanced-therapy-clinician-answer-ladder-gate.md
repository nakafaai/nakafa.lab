# Case-001 Advanced-Therapy Clinician-Answer Ladder Gate

Date checked: 2026-05-27
Evidence label: guideline, regulator, workflow, and privacy synthesis, not
medical advice

## Direct Answer

The May 26 owner packet says what needs to be labeled. The May 27 blocker is
what to do after a clinician answers.

The safe rule is:

`case001_advanced_therapy_clinician_answer_ladder_ready`

A clinician reply can change the public repo only through allowed labels. It
cannot directly become HSCT advice, gene therapy advice, CRISPR advice, trial
screening, travel guidance, import guidance, dosing, or a cure claim.

## Evidence Boundary

TIF 2025 keeps HCT in the curative category for selected TDT patients, but it
also requires expert review of donor route, iron and organ status,
pre-transplant workup, fertility, conditioning, and follow-up. TIF 2025 gene
manipulation keeps gene addition and gene editing as real curative benchmark
categories while preserving specialist selection and long-term evidence
boundaries.

FDA Casgevy and Zynteglo pages establish product categories. They do not
establish local access, affordability, patient suitability, or what case-001
should do.

## Allowed Answer Ladder

| Clinician answer label | Public output | Next state |
| --- | --- | --- |
| `domain_confirmed_record_present` | `owner_domain_labeled_present` | Continue until all seven domains are label-ready. |
| `domain_missing_record_requested` | `owner_domain_missing_record_requested` | `advanced_therapy_referral_packet_partial` |
| `domain_not_applicable_clinician_confirmed` | `owner_domain_not_applicable` | Continue with the remaining required domains. |
| `specialist_screening_reasonable` | `advanced_therapy_referral_packet_ready_for_specialist_screening` | `under_specialist_review` |
| `screening_not_reasonable_medical` | `medically_unsuitable` | `patient_relevance_blocked` |
| `access_blocked_owner_confirmed` | `access_blocked` | `access_route_research_only` |
| `private_or_patient_specific_instruction` | `release_blocked_private_material` | `public_release_blocked` |

## Advancement Requirements

- All seven owner domains are labeled present, not applicable, or
  owner-confirmed missing.
- Raw records, owner replies, identifiers, HLA details, and exact private dates
  stay outside Git.
- A qualified specialist must explicitly say screening is reasonable before the
  public state can become ready for specialist screening.
- Access blockers are not medical unsuitability.
- Medical unsuitability is not product failure or research failure.

## Islamic Motivation Boundary

Quran 16:43 supports expert consultation. Quran 49:6 supports verification
before acting. Quran 55:7-9 supports measured claims. These are process
anchors, not biomedical evidence for any therapy.

## Sources

- [May 27 clinician-answer ladder map](../../../data/workflows/case-001/2026-05-27-advanced-therapy-clinician-answer-ladder.json)
- [May 26 advanced-therapy screening owner packet](../case-context/case-001-advanced-therapy-screening-owner-packet.md)
- [TIF 2025 HSCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [FDA Casgevy product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 49:6 verification anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
