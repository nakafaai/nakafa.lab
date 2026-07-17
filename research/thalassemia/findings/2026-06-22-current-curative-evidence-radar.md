# Current Curative Evidence Radar

Date checked: 2026-06-22
Last evidence update: 2026-07-17
Status: general evidence radar, not treatment advice

## Direct Answer

The pediatric exa-cel result confirms a strong transfusion-independence
benchmark but does not make ex vivo editing an affordable-cure candidate. The
reported conditioning-related fatality makes route efficacy, editing safety,
and myeloablative safety inseparable in promotion decisions.

Current operational label:

`case001_curative_evidence_radar_ready_general_only`

## July 17 Pediatric Exa-Cel Decision

**Question:** Does current pediatric exa-cel outcome evidence justify promoting
ex vivo gene editing from curative benchmark to affordable-cure candidate?

**Decision:** `hold_exa_cel_benchmark_only_conditioning_not_separable`.

- **Fact:** The primary phase 3 report treated 15 children with TDT. At its data
  cutoff, all 8 with at least 16 months of follow-up met 12-month transfusion
  independence; 7 were not yet evaluable. Across the parallel TDT and SCD
  cohorts, all 26 children had at least one grade 3 or 4 adverse event. Two
  children with TDT had severe hepatic veno-occlusive disease attributed to
  busulfan conditioning, and one died.
- **Fact:** FDA's later July 1 analysis reports that 8 of 9 efficacy-evaluable
  children with TDT met 12-month transfusion independence, with a median
  independence duration of 20.1 months. FDA also states that full myeloablative
  conditioning precedes Casgevy.
- **Resolved contradiction:** `8/8` in the paper and `8/9` in the FDA release
  are different analysis sets or data cuts. They should not be merged into one
  response rate. The current registry lists 16 actual enrollees, remains active
  but not recruiting, and has no posted results.
- **Interpretation:** The efficacy signal is high-confidence for the evaluable
  children at each source's cutoff. Durability for the full cohort, why the
  ninth FDA-evaluable child did not meet the endpoint, long-term safety,
  delivered cost, and transferability to other editing products remain
  unresolved.
- **Current-source check:** An exact PubMed July 16-17 entry-date query returned
  two non-curative records about beta-thalassemia trait iron and TDT
  dysglycemia. Exact ClinicalTrials.gov beta-thalassemia queries found no result
  first posted or study update from July 16 onward. These are query-bounded
  negatives, not proof that no relevant evidence exists elsewhere.
- **Affordability and access:** The route still requires individualized cell
  collection, editing, release, full myeloablation, infusion, and specialist
  follow-up. Exact `CASGEVY` and `exagamglogene` BPOM product-name and ingredient
  searches returned no public record on July 17. That bounded negative does not
  prove absence, unavailability, or ineligibility.
- **Falsification criterion:** An ex vivo editing route fails affordable-cure
  promotion while it retains full myeloablation and individualized external
  manufacturing without owner-validated evidence of materially lower serious
  toxicity and total delivered cost below a recorded program threshold.
- **Next decisive action:** Require every proposed affordable curative route to
  state whether it removes full myeloablation. If it does not, keep it
  `benchmark_only` until route-level safety and total delivered cost are
  independently documented.

## July 13 Evidence Delta

Decision: `hold_registry_watch`

- **Fact:** ClinicalTrials.gov version 2026-07-13 lists `NCT07680803` as a
  planned nine-person phase 2b study of FT007, autologous `CD34+` cells
  transduced with an improved GLOBE beta-globin lentiviral vector. Its status
  remains not yet recruiting, its start date remains estimated, and it has no
  posted results. This is a pipeline and endpoint-design signal, not evidence
  of safety, efficacy, durability, access, or affordability.
- **Fact:** ClinicalTrials.gov version 2026-07-13 lists `NCT07599176` as
  recruiting, with status verified July 7 and actual start July 8. The record's
  last update was submitted July 10, correcting the earlier July 9 wording.
  The phase 1/2 NIH study includes severe beta-thalassemia in a matched-related
  donor hematopoietic-cell transplant protocol using alemtuzumab, 400 cGy total
  body irradiation, and abatacept. It has no posted results and remains a
  conditioning and HSCT comparator, not a patient route.
- **Fact:** the FDA Casgevy age expansion is already captured by the
  [July 7 benchmark](./2026-07-07-casgevy-age-expansion-benchmark.md) and
  [July 8 consistency update](./2026-07-08-casgevy-source-consistency-gate.md).
- **Interpretation:** both new registry records expand the set of curative
  approaches worth monitoring, but neither changes the current candidate or
  access decision.
- **Open question:** will either study produce peer-reviewed transfusion
  independence, toxicity, long-term engraftment, and delivered-cost evidence
  strong enough to change `hold_registry_watch`?

## Route Read

| Route | Current signal | Interpretation boundary |
| --- | --- | --- |
| Autologous gene-cell therapy | FDA CASGEVY page, pediatric exa-cel primary result, CTX001 registry records | Strong curative benchmark; full myeloablation and the reported busulfan-related fatality block affordable-route promotion. |
| Lentiviral gene addition watch | `NCT07680803` FT007 phase 2b record | Not-yet-recruiting pipeline signal; no outcome evidence. |
| Lentiviral gene addition | FDA ZYNTEGLO page | Approved benchmark, not Indonesia availability or route selection. |
| Allogeneic HSCT | 2026 HSCT burden and second-HSCT records | Curative comparator, but donor/HLA/organ-risk data are private blockers. |
| Reduced-intensity matched-donor HSCT watch | `NCT07599176` NIH phase 1/2 record | Recruiting conditioning comparator, not eligibility or access. |
| Asia watch | China BD211 recruiting record and China gamma-globin autologous HSC benchmark | Useful regional radar, not a referral instruction. |
| Metabolism comparator | Pyruvate-kinase activation review | Disease-modifying context, not a cure route. |

## What This Means For Doctor Conversation

The clean question is not "which treatment should we do?" The clean question is:

> After reviewing the private packet, which branch is even in scope for
> specialist screening: allogeneic HSCT, autologous gene-cell therapy,
> disease-modifying non-curative therapy, standard-care stabilization first, or
> benchmark-only tracking?

## Boundary

Some PubMed records have future print issue dates with earlier electronic
publication dates. They are treated as PubMed-visible current records, not as
post-June clinical events.

This radar does not provide diagnosis, dosing, treatment selection,
trial-screening instruction, referral, travel guidance, import guidance,
purchase guidance, or sample-routing permission.

Quran 49:6 and 4:58 are process-ethics anchors only: verify reports and route
consequential questions to qualified owners. They are not biomedical evidence.

## Sources

- [June 22 source JSON](../../../data/literature/pubmed/2026-06-22-current-curative-evidence-radar.json)
- [June 22 workflow JSON](../../../data/workflows/case-001/2026-06-22-current-curative-evidence-radar-gate.json)
- [FDA CASGEVY](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA ZYNTEGLO](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [ClinicalTrials.gov NCT05356195](https://clinicaltrials.gov/study/NCT05356195)
- [ClinicalTrials.gov NCT05477563](https://clinicaltrials.gov/study/NCT05477563)
- [ClinicalTrials.gov NCT06465550](https://clinicaltrials.gov/study/NCT06465550)
- [ClinicalTrials.gov NCT07599176](https://clinicaltrials.gov/study/NCT07599176)
- [ClinicalTrials.gov NCT07680803](https://clinicaltrials.gov/study/NCT07680803)
- [PubMed PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/)
- [FDA July 1 pediatric supplemental approval](https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-young-children-sickle-cell-disease)
- [July 17 BPOM exact-term snapshot](../../../data/regulatory/bpom/2026-07-17-casgevy-product-search-refresh.json)
- [PubMed July 16-17 entry-date query](https://pubmed.ncbi.nlm.nih.gov/?term=%28beta+thalassemia%5BTitle%2FAbstract%5D+OR+beta-thalassemia%5BTitle%2FAbstract%5D%29+AND+2026%2F07%2F16%3A2026%2F07%2F17%5BEDAT%5D)
- [ClinicalTrials.gov July 16 onward results query](https://clinicaltrials.gov/api/v2/studies?query.cond=beta%20thalassemia&filter.advanced=AREA%5BResultsFirstPostDate%5DRANGE%5B07%2F16%2F2026%2C%20MAX%5D&pageSize=100&countTotal=true&sort=ResultsFirstPostDate%3Adesc)
- [ClinicalTrials.gov July 16 onward update query](https://clinicaltrials.gov/api/v2/studies?query.cond=beta%20thalassemia&filter.advanced=AREA%5BLastUpdatePostDate%5DRANGE%5B07%2F16%2F2026%2C%20MAX%5D&pageSize=100&countTotal=true&sort=LastUpdatePostDate%3Adesc)
- [PubMed PMID 42252696](https://pubmed.ncbi.nlm.nih.gov/42252696/)
- [PubMed PMID 42091200](https://pubmed.ncbi.nlm.nih.gov/42091200/)
- [PubMed PMID 42261266](https://pubmed.ncbi.nlm.nih.gov/42261266/)
- [PubMed PMID 41947014](https://pubmed.ncbi.nlm.nih.gov/41947014/)
- [Quran 49:6 anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 anchor](../../islamic/quran/004-an-nisa/058.md)
