# Current Curative Evidence Radar

Date checked: 2026-06-22
Last evidence update: 2026-07-13
Status: general evidence radar, not treatment advice

## Direct Answer

The July 13 evidence update does not change Case-001 action status. It adds two
current registry signals to the general curative-route radar so research can
distinguish approved gene-cell benchmarks, pre-efficacy pipeline entries, HSCT
conditioning comparators, and non-curative disease-modifying comparators.

Current operational label:

`case001_curative_evidence_radar_ready_general_only`

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
| Autologous gene-cell therapy | FDA CASGEVY page, pediatric exa-cel PubMed record, CTX001 registry records | Strong curative benchmark, not patient eligibility or access. |
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
- [PubMed PMID 42252696](https://pubmed.ncbi.nlm.nih.gov/42252696/)
- [PubMed PMID 42091200](https://pubmed.ncbi.nlm.nih.gov/42091200/)
- [PubMed PMID 42261266](https://pubmed.ncbi.nlm.nih.gov/42261266/)
- [PubMed PMID 41947014](https://pubmed.ncbi.nlm.nih.gov/41947014/)
- [Quran 49:6 anchor](../../islamic/quran/049-al-hujurat/006.md)
- [Quran 4:58 anchor](../../islamic/quran/004-an-nisa/058.md)
