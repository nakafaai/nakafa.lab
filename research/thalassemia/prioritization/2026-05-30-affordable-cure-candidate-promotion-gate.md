# Affordable-Cure Candidate Promotion Gate

Date checked: 2026-05-30
Last evidence update: 2026-07-14
Scope: research prioritization, not treatment advice

## Purpose

This gate connects the May 29 affordability gap matrix to candidate scoring.
It prevents the project from promoting a candidate just because it feels
hopeful or novel.

Current operational label:

`case001_affordable_cure_candidate_promotion_gate_ready`

## Promotion Test

A candidate can move upward only if all four questions have source-backed
answers:

| Question | Required answer |
| --- | --- |
| Which gap? | Cost, infrastructure, conditioning, monitoring, access, safety, fertility, or assay feasibility. |
| Which benchmark? | Closest curative benchmark and closest non-curative benchmark. |
| Which endpoint? | HbF, F-cells, hemoglobin, transfusion burden, chain balance, hemolysis, viability, iron burden, or safety. |
| What would falsify it? | A clear stop rule such as identity failure, no endpoint movement, hemolysis, toxicity, access failure, or benchmark-only status. |

## Current Lane Labels

| Lane | Current label | Why |
| --- | --- | --- |
| Approved or late gene-cell therapy | `benchmark_only` | Defines curative biology and endpoint standards but does not solve access, center, conditioning, or cost gaps. |
| Hydroxyurea | `affordable_clinical_comparator` | Useful low-cost HbF comparator; not a cure claim and not case-specific. |
| Sirolimus, `PRKAB1`/autophagy, `T-BDMC`, resveratrol | `hold_for_endpoint_or_identity_gap` | Assay-only until identity, HbF, chain balance, hemolysis, viability, and safety endpoints are present. |
| Thalidomide class or melittin hazard lanes | `reject_hazard_or_unmeasured_claim` | Safety boundary blocks therapeutic promotion without a new safety-resolution package. |
| AND017, luspatercept, mitapivat | `benchmark_only` | Useful for transfusion-burden or red-cell-metabolism comparison, not cure. |

## Current Research Read

The 2026 source refresh sharpens the gate rather than changing the cure claim.
PubMed now includes a 2026 exa-cel cost-effectiveness model projecting favorable
US value, but the author affiliations require sponsor-affiliation caution.
CDA-AMC's TDT pharmacoeconomic review keeps uncertainty, acquisition cost, and
price-reduction dependency visible. ClinicalTrials.gov still shows close China
editing and non-editing benchmarks, including CS-101 phase 2, VGB-Ex01,
luspatercept plus thalidomide, and AND017.

Therefore, Nakafa Lab should not promote another weak candidate. It should
promote only a candidate that names the benchmark gap it can realistically
improve and the test that could reject it.

## July 14 Genome-Editing Safety And Affordability Delta

**Question:** Does current FDA genome-editing guidance make an ex vivo editing
route credible enough to promote as affordable?

**Decision:** `hold_for_regulatory_safety_and_cost_evidence`. The gene-editing
lanes remain `benchmark_only`; no candidate score changes.

- **Fact:** The April 2026 FDA draft is nonbinding and not for implementation.
  It recommends NGS and bioinformatics studies for on-target outcomes,
  off-target editing, and genomic integrity. For ex vivo products, the sample
  should match the edited drug-product cell type, use biological replicates,
  and achieve on-target editing comparable to the final product. It also
  recommends analysis of human genetic variation and, where relevant,
  chromosomal translocations before an original IND submission, while noting
  that variation analysis may not be necessary at that stage in some
  ultra-rare or single-patient programs.
- **Fact:** The June 2026 FDA draft allows prior public or platform knowledge to
  reduce duplicated methods, pipelines, and some validation work. It also says
  off-target results are generally not transferable across different guide
  RNAs or sequence-recognition components, and on-target or genomic-integrity
  results are generally not transferable across different genomic targets.
- **Interpretation:** A credible lower-cost editing route still needs
  product-specific safety evidence, reproducible sequencing and bioinformatics,
  representative human-cell evidence, and manufacturing-change control.
  Platform reuse may reduce this burden, but it does not erase it.
- **Contradiction:** FDA's flexibility pathway means the April draft cannot be
  used to claim that every safety assay must be built from scratch or that NGS
  alone makes editing unaffordable. Neither document provides a delivered-cost
  estimate.
- **Confidence:** High for the current FDA draft recommendations; low for their
  cost effect in Indonesia or any specific product because no owner-validated
  assay scope, regulator-accepted plan, or quote is available.
- **Affordability implication:** Do not promote an editing route on reagent or
  product price alone. Require a public-safe, costed scope for representative
  cells, on-target and off-target assays, genomic integrity, population-aware
  analysis, raw-data and software traceability, and repeat work after relevant
  manufacturing changes.
- **Falsification criterion:** Replace this hold only if a qualified regulatory
  and manufacturing owner documents which safety elements can be reused, which
  remain product-specific, the regulator-accepted evidence plan, and the total
  delivered cost. A final guidance that materially removes these product-
  specific elements would also require reassessment.
- **Next decisive action:** Obtain one owner-validated safety-package scope and
  cost breakdown for the closest Asia editing benchmark; do not start an NGS
  analysis without real inputs and essential metadata.

After a candidate passes this promotion test, use the
[minimum assay readiness gate](../assays/2026-05-31-minimum-assay-readiness-gate.md)
before lab quote or partner outreach.

## Islamic Motivation Boundary

Quran 13:17 supports disciplined attrition: benefit remains and foam is
discarded. Quran 55:7-9 supports measured claims. These are research-method
anchors, not biomedical evidence for any candidate.

## Sources

- [May 30 workflow map](../../../data/workflows/case-001/2026-05-30-affordable-cure-candidate-promotion-gate.json)
- [May 29 curative affordability gap matrix](../case-context/case-001-curative-affordability-gap-matrix.md)
- [Candidate scoring V0](2026-04-27-candidate-scoring-v0.md)
- [Proximity novelty gate V0](2026-04-28-proximity-novelty-gate-v0.md)
- [PubMed PMID 41955126](https://pubmed.ncbi.nlm.nih.gov/41955126/)
- [CDA-AMC exa-cel TDT pharmacoeconomic review](https://www.ncbi.nlm.nih.gov/books/NBK616627/)
- ClinicalTrials.gov benchmark records:
  [NCT06024876](https://clinicaltrials.gov/study/NCT06024876),
  [NCT07489196](https://clinicaltrials.gov/study/NCT07489196),
  [NCT06041620](https://clinicaltrials.gov/study/NCT06041620),
  [NCT07338344](https://clinicaltrials.gov/study/NCT07338344),
  [NCT06302491](https://clinicaltrials.gov/study/NCT06302491)
- [FDA April 2026 genome-editing NGS safety draft](https://www.fda.gov/media/191966/download)
- [FDA June 2026 prior-knowledge draft](https://www.fda.gov/media/192810/download)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
