# Case-001 Curative Branch Doctor Question Gate

Date checked: 2026-06-24
Status: doctor-facing question frame, not treatment advice

## Direct Answer

The next useful output is not a treatment recommendation. It is one branch
question for a qualified hematologist or advanced-therapy specialist after
private packet review:

> Which branch is in scope to discuss for Case-001: allogeneic HCT, autologous
> gene-cell therapy, non-curative disease modification, standard-care
> stabilization first, or benchmark-only tracking?

Current operational label:

`case001_curative_branch_doctor_question_ready_general_only`

## Why This Is The Next Gate

The June 22 radar showed that curative evidence is no longer one bucket. TIF
2025 separates allogeneic HCT and gene manipulation. FDA sources identify
CASGEVY and ZYNTEGLO as approved benchmarks. ClinicalTrials.gov adds active
registry-watch records, especially China gene-cell records. None of those
sources decide patient fit.

## Question Sequence

| Step | Ask | Public output label |
| --- | --- | --- |
| Packet readiness | Is the private packet sufficient for any branch discussion? | `packet_not_ready` or `branch_question_ready_general_only` |
| Stabilization first | Are iron, immune, organ, infection, transfusion, or safety blockers urgent first? | `standard_care_stabilization_first` |
| Branch scope | Which branch is in scope to discuss? | `allogeneic_hct_branch_owner_question`, `autologous_gene_cell_branch_owner_question`, `disease_modifying_noncurative_branch_owner_question`, or `benchmark_only_tracking` |
| Route owner | Which owner should answer next? | `route_owner_question_only` |

## Required Private Context Before Interpretation

- Clinician-confirmed diagnosis, genotype, and phenotype label.
- Transfusion burden, pre-transfusion hemoglobin, hemoglobin response, body
  weight, and annualized burden.
- Antibody screen, DAT/direct Coombs context, matching policy, reactions, and
  spleen context.
- Ferritin trend, liver iron, cardiac `T2*`, organ-risk notes, and chelator
  identity.
- HLA/donor context, center access, payer path, fertility counseling status,
  consent boundaries, and travel constraints.

## Boundary

This gate does not provide diagnosis, dosing, treatment selection, eligibility,
trial-screening instruction, referral, travel guidance, import guidance,
purchase guidance, transfusion change, chelation change, lab contact, private
message routing, or sample-routing permission.

Quran 49:6 and 4:58 are process-ethics anchors only. They support verification
and qualified owner routing, not biomedical claims.

## Sources

- [June 24 source JSON](../../../data/literature/pubmed/2026-06-24-curative-branch-question-refresh.json)
- [June 24 workflow JSON](../../../data/workflows/case-001/2026-06-24-curative-branch-doctor-question-gate.json)
- [TIF 2025 gene manipulation chapter](https://www.ncbi.nlm.nih.gov/books/NBK614241/)
- [TIF 2025 HCT chapter](https://www.ncbi.nlm.nih.gov/books/NBK614242/)
- [FDA CASGEVY](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA ZYNTEGLO](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [ClinicalTrials.gov NCT05991336](https://clinicaltrials.gov/study/NCT05991336)
- [ClinicalTrials.gov NCT06280378](https://clinicaltrials.gov/study/NCT06280378)
- [ClinicalTrials.gov NCT05577312](https://clinicaltrials.gov/study/NCT05577312)
- [ClinicalTrials.gov NCT05762510](https://clinicaltrials.gov/study/NCT05762510)
- [PubMed PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/)
- [PubMed PMID 40058646](https://pubmed.ncbi.nlm.nih.gov/40058646/)
- [PubMed PMID 41947014](https://pubmed.ncbi.nlm.nih.gov/41947014/)
- [Quran 49:6 anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 anchor](../../islamic/quran/004-an-nisa/058.md)
