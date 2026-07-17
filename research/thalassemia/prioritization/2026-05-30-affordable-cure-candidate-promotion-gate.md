# Affordable-Cure Candidate Promotion Gate

Date checked: 2026-05-30
Last evidence update: 2026-07-17
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
| Approved or late gene-cell therapy | `benchmark_only` | Pediatric exa-cel confirms transfusion-independence potential, but full myeloablation and a reported fatal busulfan-related event leave conditioning, access, center, and cost gaps open. |
| Hydroxyurea | `affordable_clinical_comparator` | Useful low-cost HbF comparator; not a cure claim and not case-specific. |
| Epigenetic HbF / `DNMT1` | Decitabine `blocked`; DMT207 `partial_hbf_reproduction_only` | DMT207 adds disease-cell and short mouse evidence but lacks a qualified material route, diverse-genotype replication, long-term safety, practical delivery, cost, total-hemoglobin, or transfusion evidence. |
| Sirolimus, `PRKAB1`/autophagy, `T-BDMC`, resveratrol | `hold_for_endpoint_or_identity_gap` | Assay-only until identity, HbF, chain balance, hemolysis, viability, and safety endpoints are present. |
| Thalidomide class or melittin hazard lanes | `reject_hazard_or_unmeasured_claim` | Safety boundary blocks therapeutic promotion without a new safety-resolution package. |
| AND017, luspatercept, mitapivat | `benchmark_only` | Useful for transfusion-burden or red-cell-metabolism comparison, not cure. |
| Hepcidin-ferroportin-`TMPRSS6` axis | `comparator_only`; sapablursen `deprioritized` | The 2026 sapablursen phase 2a `NTDT` study missed hemoglobin and liver-iron endpoints and did not consistently raise hepcidin. |

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

The July 2026 sapablursen result applies that rule to the iron axis. Endpoint
failure falsifies sapablursen monotherapy as an active affordable-cure
candidate; it does not falsify every `TMPRSS6`, ferroportin, or hepcidin
modality. Any successor must show target engagement and hemoglobin or
transfusion benefit in human thalassemia before promotion.

The posted results resolve an apparent contradiction: endpoint failure did not
mean zero individual liver-iron threshold responses, but no evaluable
participant met the week-53 hemoglobin threshold and the study had no untreated
comparator.
`NCT06421636` is now the named successor evidence trigger. It is active, not
recruiting, placebo-controlled, and has no posted results; its liver-iron,
hemoglobin, and transfusion endpoints cannot support promotion until reported.

The July 2026 DMT207 review splits the epigenetic lane without promoting a cure
claim. Decitabine remains a cytotoxic `DNMT1` proof-of-biology comparator.
DMT207 moves to `partial_hbf_reproduction_only` because it has HbF protein,
F-cell, beta-thalassemia donor-cell, and short mouse evidence. It remains
outside the first quote panel until a qualified material-identity and cost
packet exists, and it cannot move beyond preclinical reproduction without
long-term safety plus total-hemoglobin or transfusion evidence.

## July 17 Pediatric Exa-Cel Conditioning Boundary

**Question:** Does pediatric exa-cel efficacy make ex vivo editing an
affordable-cure candidate rather than a benchmark?

**Decision:** `hold_exa_cel_benchmark_only_conditioning_not_separable`.

The primary report found 12-month transfusion independence in all 8 children
with TDT evaluable at its cutoff. Across the parallel TDT and SCD cohorts, all
26 children had a grade 3 or 4 adverse event. Two children with TDT developed
severe hepatic veno-occlusive disease attributed to busulfan conditioning, and
one died. FDA's later analysis reported 8 of 9 evaluable children meeting the
same endpoint. These denominators reflect different analysis sets or cutoffs
and must stay separate.

This result strengthens the curative benchmark while tightening the affordable
route rule: editing efficacy cannot compensate for unpriced full myeloablation,
individualized manufacturing, and specialist-center risk. Exact July 17 BPOM
searches found no public `CASGEVY` or `exagamglogene` record; that bounded
negative does not establish legal status, availability, or patient fit.

**Kill criterion:** keep any ex vivo editing proposal `benchmark_only` if it
retains full myeloablation and individualized external manufacturing without
independent evidence of materially lower serious toxicity and a total delivered
cost below a recorded program threshold.

**Next action:** make removal or material reduction of full myeloablation an
explicit affordable-route discriminator before investing in product-specific
editing optimization.

## July 14 Genome-Editing Safety And Affordability Delta

**Question:** Does current FDA genome-editing guidance make an ex vivo editing
route credible enough to promote as affordable?

**Decision:** `hold_for_regulatory_safety_and_cost_evidence`. The gene-editing
lanes remain `benchmark_only`; no candidate score changes.

**Mechanism and scope:** The closest Asia benchmark is CS-101: ex vivo base
editing of autologous `CD34+` hematopoietic stem and progenitor cells at the
`HBG` promoter BCL11A-binding site to reactivate gamma-globin. The current
registry scope covers beta-thalassemia, including beta-thalassemia major; this
does not establish genotype-specific eligibility or Case-001 relevance.

**Evidence tier:** Official draft regulatory guidance plus official clinical-
trial registry records. No newly posted trial result changes the clinical-
outcome tier.

**Registry design and limitation:** `NCT06024876` is a completed, open-label,
single-arm early phase 1 study with five participants aged 6-35 and beta-
thalassemia genotype examples including beta+/beta0, betaE/beta0, and
beta0/beta0. `NCT07489196` is a not-yet-recruiting, open-label, single-arm phase
2 study planning 20 participants aged 12-35 with beta-thalassemia major. Their
registered endpoints cover adverse events, engraftment, transplant-related
mortality, transfusion independence, hemoglobin, and HbF, but neither record has
posted results. Registry design is not outcome evidence and does not resolve
safety, durability, access, or cost.

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
- **Resolved contradiction:** Reuse and product specificity apply at different
  layers. FDA allows reuse of suitable analytical methods, NGS strategies,
  bioinformatics tools and pipelines, and some platform CMC knowledge. It
  generally does not support transferring off-target results across different
  guide RNAs, on-target outcomes across different genomic targets, or genomic-
  integrity results across different edited loci. Therefore, the evidence does
  not support either extreme: every assay is new, or platform reuse removes the
  product-specific safety burden.
- **Interpretation:** The hold is caused by missing owner-validated evidence,
  not by an assumption that NGS itself makes editing unaffordable. A credible
  lower-cost route needs a regulator-accepted split between reusable methods
  and product-specific results, plus representative-cell evidence,
  manufacturing-change control, and total delivered cost.
- **Safety risk:** Off-target editing, unintended on-target outcomes, and loss
  of genomic integrity remain material product-specific risks. Conditioning,
  collection, manufacturing, and long-term follow-up remain separate delivered-
  route risks outside the two draft-guidance documents.
- **Confidence:** High for the current FDA draft recommendations; low for their
  cost effect in Indonesia or any specific product because no owner-validated
  assay scope, regulator-accepted plan, or quote is available.
- **Affordability implication:** Do not promote an editing route on reagent or
  product price alone. Require a public-safe, costed scope for representative
  cells, on-target and off-target assays, genomic integrity, population-aware
  analysis, raw-data and software traceability, and repeat work after relevant
  manufacturing changes.
- **Access impact:** No public source establishes regulator-accepted reuse,
  manufacturing capacity, total delivered cost, or a payer path for Indonesia.
  The existing CS-101 access score remains `0`; the route stays a benchmark.
- **Falsification criterion:** Replace this hold only if a qualified regulatory
  and manufacturing owner documents which safety elements can be reused, which
  remain product-specific, the regulator-accepted evidence plan, and the total
  delivered cost, and that cost meets a recorded program affordability
  threshold. A final guidance that materially removes these product-specific
  elements would also require reassessment.
- **Next decisive owner action:** The cure-program owner should use CS-101 as
  the named reference and obtain one public-safe matrix, validated jointly by a
  qualified regulatory owner and manufacturing/analytics owner, that separates
  reusable methods and platform knowledge from product-specific results,
  identifies required bridging data, and prices total delivered capacity. The
  same request must state the program's affordability threshold. Do not start
  an NGS analysis without real inputs and essential metadata.

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
- [Sapablursen phase 2a result, PMID 42241700](https://pubmed.ncbi.nlm.nih.gov/42241700/)
- [`Tmprss6` resistance study, PMID 41954608](https://pubmed.ncbi.nlm.nih.gov/41954608/)
- [REGN7999 trial `NCT06421636`](https://clinicaltrials.gov/study/NCT06421636)
- [DMT207 primary study, PMID 41347631](https://pubmed.ncbi.nlm.nih.gov/41347631/)
- [DMT207 evidence decision](../findings/2026-04-27-epigenetic-hbf-target-drilldown.md#dmt207-decision)
- [Pediatric exa-cel primary result, PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/)
- [Pediatric exa-cel trial `NCT05356195`](https://clinicaltrials.gov/study/NCT05356195)
- [FDA July 1 pediatric supplemental approval](https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-young-children-sickle-cell-disease)
- [July 17 BPOM exact-term snapshot](../../../data/regulatory/bpom/2026-07-17-casgevy-product-search-refresh.json)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
