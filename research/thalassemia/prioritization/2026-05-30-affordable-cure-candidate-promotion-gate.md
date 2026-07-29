# Affordable-Cure Candidate Promotion Gate

Date checked: 2026-05-30
Last evidence update: 2026-07-29
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
| Matched-sibling HSCT | `leading_affordable_curative_route_benchmark_only` | A 176-child multicenter LMIC cohort joins high short-term thalassemia-free survival with a USD 8,000-10,000 mean cost range including follow-up. A new long-term synthesis and its 39-year primary cohort add historical survival, recurrence, endocrine, fertility, and secondary-cancer evidence, but contain count and possible cohort-overlap limitations. Matched-sibling restriction, modern five-year outcomes, toxicity, lifetime surveillance cost, and Indonesia delivery remain unresolved. |
| F-BMT haploidentical HSCT | `conditioning_benchmark_only` | A prospective 29-person cohort reports 93.1% two-year thalassemia-free and overall survival with no graft failure. Single-center design, incomplete abstract-level safety attribution, possible overlap with an earlier multicenter cohort, and absent delivered cost block affordable-route promotion. |
| FT007 lentiviral gene addition | `active_registry_benchmark_only` | The nine-person phase 2b record is now recruiting with an actual start, but design and outcomes did not change and no results are posted. Conditioning, product and clonal safety, durability, manufacturing failures, delivered cost, and Indonesia access remain unresolved. |
| Approved or late gene-cell therapy | `benchmark_only` | Pediatric exa-cel confirms transfusion-independence potential, but full myeloablation, a reported fatal busulfan-related event, and required long-term safety surveillance leave conditioning, safety, access, center, and cost gaps open. BRL-101 has no posted outcomes. HGI-001 now has a source-linked five-child pilot, but its small conflicted evidence base, busulfan route, and missing delivered cost keep it at an early clinical benchmark. |
| `CD117` epitope-shielded conditioning | `preclinical_conditioning_benchmark_only` | A primary preprint reports antibody conditioning plus shielded-HSPC enrichment and phenotype improvement in a humanized beta-thalassemia mouse model, but durability after antibody withdrawal, clinical safety, and delivered cost are unresolved. |
| Hydroxyurea | `affordable_clinical_comparator` | Useful low-cost HbF comparator; not a cure claim and not case-specific. |
| Epigenetic HbF / `DNMT1` | Decitabine `blocked`; DMT207 `partial_hbf_reproduction_only` | DMT207 adds disease-cell and short mouse evidence but lacks a qualified material route, diverse-genotype replication, long-term safety, practical delivery, cost, total-hemoglobin, or transfusion evidence. |
| Sirolimus, `PRKAB1`/autophagy, `T-BDMC`, resveratrol | `hold_for_endpoint_or_identity_gap` | Assay-only until identity, HbF, chain balance, hemolysis, viability, and safety endpoints are present. |
| Thalidomide class or melittin hazard lanes | `reject_hazard_or_unmeasured_claim` | Safety boundary blocks therapeutic promotion without a new safety-resolution package. |
| AND017, luspatercept, mitapivat | `benchmark_only` | Useful for transfusion-burden or red-cell-metabolism comparison, not cure. |
| Hepcidin-ferroportin-`TMPRSS6` axis | `iron_overloaded_ntdt_comparator_only`; sapablursen `deprioritized` | Sapablursen missed hemoglobin and liver-iron endpoints. Human `TMPRSS6`-related IRIDA co-inheritance defines a low-iron safety boundary, not therapeutic rescue. |

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

## July 29 Long-Term HSCT Outcome Decision

**Question:** Does a newly indexed long-term HSCT meta-analysis close the
durability and late-safety gaps enough to promote matched-sibling HSCT beyond
the leading affordable-curative route benchmark?

**Decision:** `hold_msd_hsct_at_leading_affordable_curative_route_benchmark_only`.

- **Fact:** PMID `42520329` states that four observational reports with 616
  transplanted participants produced a pooled long-term overall-survival
  estimate of 85% (95% CI 81%-89%; `I2=40%`). The component estimates occur at
  different horizons of 15, 20, 30, and 39 years, and the search ended in July
  2024.
- **Primary evidence:** PMID `36002533` is the most detailed included report.
  It followed 137 consecutive people from one Pescara center; 127 received
  genotypically HLA-identical sibling grafts. At final follow-up, 114 were
  living and 108 were living and cured. Thirty-nine-year overall survival was
  81.4% and disease-free survival was 74.5%.
- **Late-safety evidence:** The primary cohort reports 14
  transplant-related deaths, 12 thalassemia recurrences, 15 secondary solid
  cancers, azoospermia in 22 of 42 evaluated males, and amenorrhea in 32 of 62
  evaluated females. These observations define outcome and surveillance
  requirements without attributing every event to one conditioning component.
- **Evidence and era boundary:** This is historical observational evidence.
  Most of the primary cohort was transplanted in the 1980s or 1990s, so it does
  not estimate a modern EBMT-aligned LMIC protocol or Indonesia delivery.
- **Count contradiction:** The four listed study sizes sum to 618, not 616.
  Narrative donor counts total 618, while the table instead sums to 504
  matched-sibling, 95 unrelated, and 19 other related donors. Preserve these
  differences without choosing a preferred denominator.
- **Independence gap:** The included 115-person 1983-2006 Pescara report
  appears nested in the 137-person 1983-2018 Pescara report by center, authors,
  dates, and scope. The synthesis does not state how participant overlap was
  handled, so its pooled denominator is not a confirmed independent cohort.
- **Interpretation:** The evidence supports a historical long-term comparator
  and makes late recurrence, mortality, gonadal effects, and secondary cancer
  explicit. It does not validate lifetime durability for the short-follow-up
  2026 LMIC cohort or justify affordable-route promotion.
- **Confidence:** High that promotion is unsupported; low that the pooled 85%
  estimate predicts a contemporary LMIC or Indonesia route.
- **Affordability and access:** Neither source prices lifetime surveillance or
  establishes Indonesia capacity, authorization, payer coverage, access, or
  affordability. These components remain outside the reported
  USD 8,000-10,000 LMIC range.
- **Hypothesis:** A contemporary, independently enrolled matched-sibling
  pediatric cohort can preserve five-year thalassemia-free survival while
  reducing historical recurrence, mortality, endocrine, fertility, and
  secondary-cancer burden.
- **Open question:** What complete five-year efficacy and late-safety
  denominators accompany a modern protocol, and what does lifetime monitoring
  add to Indonesia-relevant delivered cost?
- **Falsification criterion:** Remove the leading-route label if independent
  modern follow-up shows material loss of thalassemia-free survival, excess
  death, recurrence, graft failure, infection, GVHD, endocrine or fertility
  harm, or secondary malignancy, or if itemized Indonesia delivery exceeds the
  program's cost threshold.
- **Next decisive action:** Reconcile the Pescara overlap and study counts
  before using the pooled estimate. Require one independent, modern,
  time-specific five-year cohort with complete late-safety denominators and an
  itemized lifetime Indonesia delivery model.

## July 28 HSCT Fertility-Evidence Decision

**Question:** Does a new 119-person pre-HSCT fertility cohort close the
fertility-safety gap enough to promote matched-sibling HSCT beyond the leading
affordable-curative route benchmark?

**Decision:** `hold_msd_hsct_at_leading_affordable_curative_route_benchmark_only`.

- **Mechanism and scope:** Allogeneic matched-sibling HCT replaces ineffective
  recipient hematopoiesis with donor hematopoiesis after conditioning. The
  leading-route outcome evidence remains limited to under-14, fully
  matched-sibling, low- or intermediate-risk TDT. PMID `42515819` instead
  supplies baseline fertility-measurement evidence from 119 pediatric and
  adolescent girls with TDT before HSCT; the indexed abstract does not identify
  genotype, donor type, conditioning regimen, or subsequent transplant outcome.
- **Fact and endpoint:** In the retrospective cohort, preoperative
  anti-Mullerian hormone was not significantly associated with primordial
  follicle density (coefficient -0.04, 95% CI -0.12 to 0.03; `p=0.262`). Each
  1 ng/mL increase was associated with a higher oocyte yield (incidence rate
  ratio 1.14, 95% CI 1.08-1.20) and maturation rate (coefficient 3.50, 95% CI
  1.10-5.90).
- **Evidence tier:** Peer-reviewed human measurement evidence before HSCT, not
  post-HSCT fertility, conditioning-safety, transplant-efficacy, or cost
  evidence. The disease-specific retrospective cohort has no healthy comparator.
- **Resolved measurement contradiction:** Anti-Mullerian hormone may inform
  oocyte yield and maturation in this cohort, but it did not measure the
  primordial follicle pool. It cannot alone close the baseline gap or attribute
  a later change to conditioning.
- **Safety risk:** Conditioning-related ovarian, fertility, and endocrine harm
  remains unresolved. Age was independently associated with follicle density,
  oocyte yield, and maturation in this cohort, so it is an observed baseline
  covariate rather than a post-conditioning outcome.
- **Affordability and access:** Baseline assessment, any fertility-preservation
  component, and longitudinal follow-up remain unpriced in the reported
  USD 8,000-10,000 route. The study does not establish Indonesia capacity,
  payer coverage, access, or affordability.
- **Hypothesis:** A prospective multicenter cohort using a
  fertility-specialist-defined baseline that does not treat anti-Mullerian
  hormone as a proxy for primordial follicle density can separate baseline TDT
  effects from conditioning-related ovarian and endocrine outcomes.
- **Open question:** After baseline adjustment, what three- to five-year
  ovarian, endocrine, and fertility outcomes accompany each matched-sibling and
  alternative-donor conditioning protocol?
- **Falsification criterion:** Remove the leading-route label if independent
  baseline-adjusted follow-up shows unacceptable mortality, graft failure,
  infection, fertility or endocrine harm, loss of thalassemia-free survival, or
  an itemized Indonesia-relevant delivered cost above the program threshold.
- **Next decisive action:** A transplant-program owner and reproductive
  endocrinology research owner should define one prospective baseline and
  longitudinal outcome set that states what anti-Mullerian hormone can and
  cannot measure, records conditioning exposure, and follows ovarian,
  endocrine, and fertility outcomes for three to five years. A
  health-economics owner should price those route components.

## July 27 FT007 Registry Decision

**Question:** Does FT007's move from not yet recruiting to recruiting close
enough evidence gaps for promotion beyond a registry benchmark?

**Decision:**
`hold_ft007_at_active_registry_benchmark_only_pending_treated_outcomes_safety_durability_and_cost`.

- **Fact and scope:** ClinicalTrials.gov version 2026-07-27 changes
  `NCT07680803` to recruiting at two Italian sites and records an actual
  2026-07-06 start. The single-arm phase 2b study still estimates nine people
  aged 3-35 with TDT, including at least two with a beta-zero/beta-zero or
  beta-zero/beta-zero-like genotype.
- **Mechanism and endpoint:** FT007 uses autologous `CD34+` hematopoietic stem
  and progenitor cells transduced ex vivo with a GLOBE lentiviral vector
  encoding human beta-globin. Its primary endpoint remains 12 continuous months
  without transfusion and weighted average hemoglobin of at least 9.0 g/dL
  within 24-month follow-up.
- **Evidence tier:** Active registry design only. Official version history shows
  that design, intervention, enrollment, eligibility, and outcomes are
  unchanged; only status, actual start, and site recruitment changed. No results
  are posted.
- **Safety boundary:** The planned safety endpoints cover harvesting,
  conditioning, product adverse events, engraftment, insertional mutagenesis,
  clonal dominance, immune reconstitution, and multilineage vector integration.
  They are not observed safety results.
- **Affordability and access:** Individualized cell collection, manufacture,
  conditioning, infusion, and surveillance remain unpriced. Recruiting in Rome
  and Milan does not establish Indonesia authorization, manufacturing, center
  capacity, payer coverage, access, affordability, or suitability.
- **Falsification criterion:** Deprioritize FT007 if the complete treated
  denominator fails the registered endpoint, lacks durable polyclonal
  engraftment, shows clonal proliferation or unacceptable serious toxicity, or
  cannot meet the delivered-cost threshold.
- **Next decisive action:** Preserve the registry version change and require a
  complete treated denominator with 24-month outcome, safety, manufacturing, and
  delivered-cost evidence before reconsidering promotion.

## July 27 Haploidentical-HSCT Conditioning Decision

**Question:** Does the new prospective F-BMT haploidentical-HSCT cohort close
the matched-sibling donor gap enough to become an affordable curative route?

**Decision:**
`promote_f_bmt_haplo_hsct_to_conditioning_benchmark_only_pending_independent_comparison_safety_and_cost`.

- **Fact and endpoint:** PMID `42489576` reports 29 participants aged at least
  seven with TDT. Two-year thalassemia-free and overall survival were 93.1%;
  all engrafted, with no reported graft failure or mixed chimerism.
- **Safety boundary:** Grade II-IV acute GVHD was 17.2% and chronic GVHD 6.9%.
  One sinusoidal obstruction syndrome event and three hemorrhagic-cystitis
  events resolved. The abstract does not report causes of death, complete
  infections, severe chronic GVHD, ICU use, fertility or endocrine outcomes.
- **Evidence and independence boundary:** This is prospective peer-reviewed
  evidence, but single-center and non-randomized. The same center participated
  in the earlier 823-person trial, and enrollment windows overlap from June to
  July 2023. Participant independence is unresolved.
- **Registry conflict:** WHO ICTRP's `ChiCTR2300071890` mirror targets 30 people
  aged 3-25 and lists survival endpoints; the paper reports 29 aged at least
  seven and makes two-year thalassemia-free survival primary. The registry
  mirror was last refreshed in June 2023 and posts no results.
- **Interpretation:** The result supports a regimen-specific alternative-donor
  comparison, not a broad low-toxicity, affordable, or Indonesia-access claim.
  Cross-study GVHD percentages are not directly comparable because the
  conditioning, prophylaxis, endpoint definitions, centers, and populations
  differ.
- **Affordability and access:** Four-drug myeloablation, HLA and donor workup,
  post-transplant cyclophosphamide, in vivo T-cell depletion, immunosuppression,
  infection support, and transplant-unit care remain unpriced. No reviewed
  source establishes Indonesia capacity, payer coverage, access, or
  affordability.
- **Falsification criterion:** Deprioritize F-BMT as a conditioning benchmark if
  an independent prospective comparison fails to preserve thalassemia-free
  survival, does not improve GVHD-free survival, increases mortality, graft
  failure, infection or organ toxicity, or exceeds the delivered-cost threshold.
- **Next decisive action:** Obtain the full report, reconcile the registry
  population and endpoints, and exclude participant overlap with PMID
  `41730859`. Compare complete survival, GVHD-free survival, graft failure,
  infection, organ toxicity, hospitalization, and itemized two-year cost across
  protocols before changing the route ranking.

## July 25 HGI-001 Evidence Correction

**Question:** Does the source-linked five-person HGI-001 paper close enough
outcome, delivery, and cost gaps to promote lentiviral gene addition as an
affordable Asian cure route?

**Decision:**
`hold_hgi001_at_early_clinical_benchmark_only_pending_larger_cohort_safety_durability_and_cost`.

- **Fact and endpoint:** PMID `41693207` reports five treated children with TDT,
  including three with beta-zero/beta-zero genotypes. All five remained
  transfusion independent for more than 26 months, with median independence of
  34.3 months and median follow-up of 34.7 months.
- **Evidence tier:** This is a peer-reviewed, single-center, single-arm early
  clinical pilot. It is not a randomized or independent replication, and three
  authors disclose a related patent while one is Hemogen's founder.
- **Resolved provenance gap:** Hemogen identifies paper product hemo-cel as
  HGI-001. The sponsor's publication page links the paper to `NCT04592458`,
  which ClinicalTrials.gov lists as an alias of `NCT05745532`. The earlier
  two-person preprint is a prior data cut, not two extra participants.
- **Unresolved conflict:** The paper calls the study phase 1/2 and reports five
  treated participants. The aliased registry record labels it early phase 1,
  estimates ten participants, remains recruiting, and has no posted results.
  The new phase 2 narrative's no-severe-adverse-event wording is broader than
  the paper abstract's no-unexpected-event statement and must not erase serious
  conditioning events described in the sponsor's publication summary.
- **Mechanism and safety:** Lentiviral beta-globin addition can restore
  beta-like globin production without donor GVHD. The route still requires
  mobilization, apheresis, individualized cell manufacture, busulfan
  myeloablation, inpatient transplant support, and long-term vector
  integration surveillance. Five participants at about three years cannot
  resolve rare, late, or route-level harm.
- **Affordability and access:** Sponsor pages describe localized manufacturing,
  but no reviewed source itemizes technology transfer, product, conditioning,
  inpatient, surveillance, or total delivered cost. The Hong Kong phase 2
  record remains not yet recruiting with no listed site or posted results.
  Neither point establishes Indonesia authorization, payer coverage, access, or
  affordability.
- **Falsification criterion:** Deprioritize HGI-001 if complete-cohort evidence
  shows non-durable transfusion independence, unacceptable conditioning or
  product toxicity, clonal dominance, replication-competent lentivirus,
  manufacturing failure, or delivered cost outside the program threshold.
- **Next decisive action:** Obtain the full paper and supplement through an
  approved route, reconcile treated and evaluable denominators with the aliased
  registry, and extract serious events by conditioning versus product
  attribution. Require a larger prospective cohort plus itemized manufacturing,
  conditioning, inpatient, and surveillance cost before reconsidering the route.

## July 23 EBMT Conditioning Decision

**Question:** Does new EBMT conditioning guidance resolve the regimen and
delivery gaps well enough to move matched-sibling HSCT beyond the leading
affordable-curative route benchmark?

**Decision:** `hold_msd_hsct_at_leading_affordable_curative_route_benchmark_only`.

- **Mechanism and scope:** Allogeneic matched-sibling HCT replaces ineffective
  recipient hematopoiesis with donor hematopoiesis after conditioning. The
  outcome evidence remains the narrow under-14, fully matched-sibling,
  low/intermediate-risk TDT cohort. The EBMT guideline addresses conditioning
  by age and donor type for children and adults with TDT, but does not expand
  the outcome population of that cohort.
- **Evidence tier:** The new EBMT document used a structured literature review,
  consensus sessions, GRADE, panel approval, and external review. It is
  practice guidance, not a new efficacy, safety, or cost cohort.
- **Resolved contradiction:** The LMIC cohort still conflicts on whether its
  busulfan quantity is daily or total, and PubMed/Crossref show no correction.
  The regimen must not be operationalized from that paper. EBMT guidance is the
  correct independent protocol source, but its public preview does not expose
  the recommendation text, so exact regimens are not imported from citations
  or inferred.
- **Safety risk:** Conditioning toxicity, graft failure, transplant mortality,
  veno-occlusive disease or sinusoidal obstruction syndrome, infection, GVHD,
  fertility or endocrine harm, and ICU burden remain route-level risks.
- **Affordability and access:** A stated aim to support resource-limited
  settings is not evidence of Indonesia capacity, authorization, payer
  coverage, or affordability. The reported USD 8,000-10,000 cohort cost remains
  non-itemized and cannot price a guideline-concordant local route.
- **Falsification criterion:** Remove the leading-route label if independent
  three-to-five-year outcomes show unacceptable mortality, graft failure, late
  toxicity, infection, or loss of thalassemia-free survival, or if a
  guideline-concordant Indonesia delivery model exceeds the program threshold.
- **Next decisive action:** A transplant-program owner should obtain the full
  EBMT recommendation text and map its age-, donor-, conditioning-, monitoring-,
  supportive-care-, and iron-management requirements to Indonesia capacity.
  A health-economics owner should then price that mapped route and its
  uncertainties before any promotion beyond `benchmark_only`.

## July 22 TMPRSS6 Human-Genetics Decision

**Question:** Does the new beta-thalassemia and IRIDA family provide human
evidence for promoting `TMPRSS6` inhibition as an affordable disease-modifying
route?

**Decision:** `hold_tmprss6_inhibition_at_iron_overloaded_ntdt_comparator_only`.
The cure-route ranking does not change.

- **Fact:** An ahead-of-print familial case series reports relatives with a
  homozygous `HBB` promoter variant and a novel homozygous `TMPRSS6` missense
  variant that the authors classified as likely pathogenic for IRIDA. The
  reported phenotype included persistent microcytic anemia, low ferritin, and
  only a partial transient response to intravenous iron.
- **Resolved contradiction:** The paper reports that two relatives had
  unnecessary transfusions stopped after molecular confirmation. That is
  diagnostic reclassification, not transfusion independence caused by a
  `TMPRSS6` intervention, and it cannot support a cure or efficacy claim.
- **Scope and safety:** The current REGN7999 trial `NCT06421636` studies the
  opposite iron context: iron-overloaded `NTDT`, with liver iron concentration
  at least 5 mg Fe/g dry weight and ferritin at least 300 ng/mL. It excludes
  screening hemoglobin at or below 8 g/dL. IRIDA-like low-iron states are
  therefore outside the current therapeutic evidence scope.
- **Evidence tier and confidence:** The genetic report is an uncontrolled
  family case series, not an intervention study. Confidence is high that it
  establishes a diagnostic and anemia-safety boundary and low that it predicts
  the efficacy or safety of partial pharmacologic `TMPRSS6` inhibition.
- **Affordability and access:** Genotype and iron-state classification plus MRI
  and anemia monitoring add delivery requirements. No reviewed source provides
  an itemized Indonesia cost or access path, and no efficacy result justifies
  an affordable-route claim.
- **Falsification criterion:** Deprioritize the broader `TMPRSS6` lane if
  placebo-controlled REGN7999 results fail to improve liver iron without
  worsening hemoglobin or transfusion burden, or show unacceptable safety.
  Cure promotion additionally requires durable transfusion independence caused
  by treatment, not diagnostic reclassification.
- **Next decisive action:** At the first `NCT06421636` results posting, extract
  randomized denominators, baseline iron and hemoglobin scope, liver-iron
  effect, hemoglobin, transfusions, and adverse events before reconsidering the
  lane.

## July 21 BRL-101 Registry Decision

**Decision:** `hold_brl101_at_registry_benchmark_until_cohort_outcomes`.

- **Mechanism and scope:** `NCT05577312` is a single-arm phase 1/2 study of
  autologous `CD34+` HSPCs edited by CRISPR-Cas9 at the erythroid `BCL11A`
  enhancer after myeloablative conditioning. Its TDT population is age 3-35 and
  lists beta-zero/beta-zero, beta-plus/beta-plus, beta-plus/beta-zero, and
  beta-E/beta-zero genotypes.
- **Evidence tier:** The July 21 registry version changes 39 participants from
  estimated to actual and the study to active, not recruiting. BRL-101
  follow-up `NCT06298630` is now recruiting, with 45 estimated
  participants and hematologic-malignancy observation up to 15 years. Neither
  record has posted results, and actual enrollment is not a treated or outcome-
  evaluable denominator.
- **Resolved contradiction:** Closed recruitment and active surveillance
  increase operational maturity but do not demonstrate efficacy, safety,
  durability, genomic integrity, or successful transfer of all phase 1/2
  participants into follow-up.
- **Safety risk:** Myeloablation, treatment-related adverse events, graft
  failure, malignancy, and other long-term genomic risks remain unresolved.
- **Affordability and access:** Individualized manufacture and specialist
  follow-up remain necessary. The China-only records contain no total delivered
  cost, Indonesia capacity, authorization, payer, or access evidence.
- **Falsification criterion:** Deprioritize BRL-101 as a curative benchmark if
  complete-cohort results show unacceptable mortality, serious toxicity,
  malignancy, graft failure, or non-durable transfusion independence. Do not
  promote it as affordable without itemized cost below a recorded threshold.
- **Next decisive action:** The evidence owner should capture the first posted
  results or primary phase 1/2 cohort report, reconcile efficacy and safety
  denominators, and only then hand the full route to a health-economics owner.

## July 21 Exa-Cel Regulatory Safety Decision

**Question:** Does FDA's expanded pediatric Casgevy approval resolve exa-cel's
long-term safety gap well enough to promote it beyond `benchmark_only`?

**Decision:** `hold_exa_cel_benchmark_only_pending_conditioning_cost_and_15_year_safety_evidence`.
Matched-sibling HSCT remains the leading affordable-curative route benchmark.

- **Fact:** The July 1 FDA supplement expanded the US TDT indication to ages 2
  years and older and replaced an earlier SCD-only postmarketing requirement.
  Protocol `VX22-290-101` must now include 250 people with SCD and 150 with TDT,
  follow each participant for 15 years, complete by December 31, 2045, and
  report by December 31, 2046.
- **Fact:** FDA says spontaneous reports and routine pharmacovigilance are
  insufficient to assess the unexpected serious risk of secondary malignancies
  and off-target effects after exa-cel genome editing. The protocol must also
  assess long-term safety.
- **Resolved contradiction:** A favorable approval decision does not close the
  long-term safety question, while a required study does not prove the named
  harms occurred. The letter defines a regulator-required uncertainty.
- **Interpretation:** The approval does not change candidate ranking. Confidence
  is high about the evidence requirement and low about eventual risk magnitude
  because no postmarketing outcomes are reported.
- **Safety risk:** Secondary malignancy, off-target effects, and other long-term
  outcomes require systematic 15-year observation. Full myeloablative
  conditioning remains a separate near-term route risk.
- **Affordability and access:** The 150-person TDT postmarketing cohort adds an
  unpriced sponsor-level monitoring and data-infrastructure obligation. The
  letter does not establish which costs apply to every treated person and
  provides no total delivered cost, Indonesia capacity, payer, or access
  evidence.
- **Open question:** What are the TDT cohort's long-term safety results and the
  complete delivered cost of conditioning and individualized manufacture? What
  do the sponsor study and routine long-term follow-up each add?
- **Falsification criterion:** Deprioritize exa-cel as an affordable-curative
  route if the required study shows unacceptable serious long-term risk or the
  complete route cannot meet the program's delivered-cost threshold.
- **Next decisive action:** Track annual `VX22-290-101` status and TDT safety
  reporting. Before reconsidering promotion, require cost comparisons to
  separate the sponsor's postmarketing study from routine long-term follow-up
  and price each included component explicitly.

## July 19 Matched-Sibling HSCT Route Decision

**Question:** Does a new multicenter LMIC matched-sibling transplant cohort move
this route above gene-cell therapy as the leading affordable-curative benchmark?

**Decision:** `promote_msd_hsct_to_leading_affordable_curative_route_benchmark_only`.
The route moves above ex vivo gene-cell therapy on current affordability
evidence, but it is not promoted as broadly accessible or suitable.

- **Fact:** The primary report includes 176 consecutive first matched-sibling
  bone marrow transplants in children under 14 across centers in India,
  Pakistan, Vietnam, Uzbekistan, and Iraq. Entry required a fully matched
  sibling, stable organ function, no active infection, and low- or intermediate-
  risk features after optimization.
- **Fact:** At median follow-up of 11.35 months, 164 of 176 were thalassemia-free
  and 169 were alive. Six transplant-related deaths, five graft failures, 13
  veno-occlusive disease or sinusoidal obstruction syndrome events, 33 CMV
  reactivations, and 18 ICU admissions keep the route-level burden visible.
- **Fact:** The paper reports mean cost per transplant, including follow-up, as
  USD 8,000-10,000. It does not itemize the cost method, time horizon, subsidy,
  currency year, or what would transfer to Indonesia.
- **Resolved contradiction:** The manuscript reports 93.2% thalassemia-free
  survival in its results and table versus 93.4% in its abstract and figure,
  and 3.4% transplant-related mortality in its results and table versus 3.8% in
  its figure. The table reports 169 overall survivors, which does not reconcile
  with 176 participants and six reported deaths. Several other rates differ
  slightly, the methods institution list omits a Pakistan center present in
  Table 4, and
  the methods and discussion conflict on whether the busulfan quantity is daily
  or total. Preserve the reported counts and ranges without forcing
  reconciliation, and do not operationalize the regimen from this paper.
- **Hypothesis:** A standardized matched-sibling route using generally available
  medicines plus remote quality support can preserve high thalassemia-free
  survival while remaining below the program's delivered-cost threshold in an
  independently run LMIC network.
- **Interpretation:** This is the strongest current affordable-curative route
  evidence because it combines clinical cure-oriented outcomes with a direct
  cost range. Confidence is moderate for the short-term result and low for long-
  term durability, broad transferability, or Indonesia affordability. The three
  startup centers contributed only 15 patients, and no Indonesia site or payer
  evidence is present.
- **Open question:** Will independent three- to five-year follow-up preserve
  thalassemia-free survival while resolving late graft failure, fertility,
  endocrine, infection, and cost-transferability gaps?
- **Falsification criterion:** Remove the leading-route label if independent
  long-term results show unacceptable mortality, graft failure, late toxicity,
  infection burden, or if an itemized Indonesia-relevant delivered cost exceeds
  the program threshold.
- **Next decisive action:** A transplant-program and health-economics owner
  should itemize the reported USD 8,000-10,000 route, test the required center
  capacity and payer assumptions against Indonesia, and pair that analysis with
  independent long-term outcome data.

## July 18 Conditioning-Route Decision

**Question:** Does `CD117` epitope shielding resolve the full-myeloablation
blocker well enough to promote gene-cell therapy as an affordable-cure
candidate?

**Decision:** `promote_cd117_shielding_to_preclinical_conditioning_benchmark_only`.
The approved gene-cell lane remains `benchmark_only`.

- **Fact:** A non-peer-reviewed primary preprint combined the `CIM058`
  `CD117`-blocking antibody with healthy-donor `CD34+` HSPCs prime-edited to
  carry the antibody-resistant `CD117 E73K` variant. In NBSGW mice humanized
  with beta-thalassemia HSPCs of the homozygous `IVS1-110/IVS1-110` genotype,
  pre- and post-transplant antibody exposure enriched shielded cells and
  improved globin-chain balance and erythroid maturation, reduced
  reticulocytosis and splenic iron, and reduced spleen size. The methods report
  two same-genotype donor sources; the study did not test patients, transfusion
  independence, or total delivered cost.
- **Interpretation:** This directly addresses the conditioning bottleneck
  exposed by pediatric exa-cel without resolving it clinically. The model is
  immunodeficient, permits human HSPC engraftment without conditioning, and
  partially rescued the phenotype without `CIM058`. The authors also identify
  durability after antibody withdrawal as a critical open question.
- **Safety risk:** The route adds a second genome edit and repeated antibody
  exposure. The reported prime-editing checks were favorable but not a full
  genomic-safety assessment. Long-term multilineage fitness, immune effects,
  graft rejection or graft-versus-host disease for the allogeneic route, and
  clinical conditioning toxicity remain unresolved.
- **Affordability and access:** Removing busulfan could reduce a major safety
  and supportive-care burden, but prime editing, cell manufacture, antibody
  production and dosing, transplant infrastructure, and follow-up remain.
  The preprint supplies no delivered-cost or Indonesia-access evidence. A new
  EHA/EBMT consensus separately identifies price, availability, and resource
  allocation as gene-therapy selection constraints; it is guidance, not new
  outcome evidence.
- **Falsification criterion:** Deprioritize this conditioning route if an
  immunocompetent large-animal study cannot maintain clinically relevant,
  multilineage chimerism after antibody withdrawal without genotoxic
  conditioning or if full genomic, hematologic, and immune safety or total
  delivered cost fails the program threshold.
- **Next decisive action:** A transplant-conditioning owner should obtain the
  complete nonhuman-primate dataset cited only as preliminary support and
  require a controlled antibody-withdrawal study with durable multilineage
  engraftment, marrow and immune safety, genomic-integrity analysis, supportive-
  care use, and a costed autologous-versus-allogeneic process map before any
  clinical or affordable-cure promotion.

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
- [`TMPRSS6`-related IRIDA with beta-thalassemia, PMID 42479051](https://pubmed.ncbi.nlm.nih.gov/42479051/)
- [REGN7999 trial `NCT06421636`](https://clinicaltrials.gov/study/NCT06421636)
- [DMT207 primary study, PMID 41347631](https://pubmed.ncbi.nlm.nih.gov/41347631/)
- [DMT207 evidence decision](../findings/2026-04-27-epigenetic-hbf-target-drilldown.md#dmt207-decision)
- [Matched-sibling LMIC transplant cohort, PMID 42469166](https://pubmed.ncbi.nlm.nih.gov/42469166/)
- [Matched-sibling LMIC transplant full text, DOI 10.1182/bloodadvances.2025019083](https://doi.org/10.1182/bloodadvances.2025019083)
- [Long-term HSCT meta-analysis, PMID 42520329](https://pubmed.ncbi.nlm.nih.gov/42520329/)
- [Long-term HSCT meta-analysis full text, DOI 10.1016/j.htct.2026.106490](https://www.htct.com.br/en-long-term-survival-rates-thalassemia-patients-articulo-S2531137926002373)
- [Pescara 39-year HSCT cohort, PMID 36002533](https://pubmed.ncbi.nlm.nih.gov/36002533/)
- [Pescara primary full text, PMC9400570](https://pmc.ncbi.nlm.nih.gov/articles/PMC9400570/)
- [Pre-HSCT TDT fertility cohort, PMID 42515819](https://pubmed.ncbi.nlm.nih.gov/42515819/)
- [Fertility cohort DOI 10.1093/humrep/deag117](https://doi.org/10.1093/humrep/deag117)
- [Pediatric exa-cel primary result, PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/)
- [Pediatric exa-cel trial `NCT05356195`](https://clinicaltrials.gov/study/NCT05356195)
- [FDA July 1 pediatric supplemental approval](https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-young-children-sickle-cell-disease)
- [FDA July 1 Casgevy supplement approval letter](https://www.fda.gov/media/193444/download)
- [July 17 BPOM exact-term snapshot](../../../data/regulatory/bpom/2026-07-17-casgevy-product-search-refresh.json)
- [`CD117` epitope-shielded conditioning preprint, PMID 42465494](https://pubmed.ncbi.nlm.nih.gov/42465494/)
- [EHA/EBMT gene-therapy selection consensus, PMID 42463828](https://pubmed.ncbi.nlm.nih.gov/42463828/)
- [FT007 phase 2b registry record, NCT07680803](https://clinicaltrials.gov/study/NCT07680803)
- [FT007 record history, version 1](https://clinicaltrials.gov/study/NCT07680803?a=1&tab=history)
- [F-BMT haploidentical-HSCT cohort, PMID 42489576](https://pubmed.ncbi.nlm.nih.gov/42489576/)
- [F-BMT paper DOI 10.1002/1545-5017.70563](https://doi.org/10.1002/1545-5017.70563)
- [WHO ICTRP mirror for ChiCTR2300071890](https://trialsearch.who.int/Trial2.aspx?TrialID=ChiCTR2300071890)
- [Multicenter allo-HSCT comparator, PMID 41730859](https://pubmed.ncbi.nlm.nih.gov/41730859/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
