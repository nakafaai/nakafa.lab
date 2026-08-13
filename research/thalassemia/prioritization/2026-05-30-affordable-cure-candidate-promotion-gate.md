# Affordable-Cure Candidate Promotion Gate

Date checked: 2026-05-30
Last evidence update: 2026-08-13
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
| Matched-sibling HSCT | `leading_affordable_curative_route_benchmark_only` | A 176-child multicenter LMIC cohort joins high short-term thalassemia-free survival with a USD 8,000-10,000 mean cost range including follow-up. A Jakarta conference report now adds two-case local execution, but both cases developed VOD and no complete attempted denominator, transfusion-independence, long-term outcome, or itemized cost is reported. A new long-term synthesis and its 39-year primary cohort add historical survival, recurrence, endocrine, fertility, and secondary-cancer evidence, but contain count and possible cohort-overlap limitations. Matched-sibling restriction, modern five-year outcomes, toxicity, lifetime surveillance cost, and Indonesia delivery remain unresolved. |
| Indonesia pediatric matched-sibling HSCT execution | `indonesia_execution_benchmark_only` | APBMT abstract `A-198` reports two pediatric beta-thalassemia major transplants at one Jakarta center, both with HLA-matched sibling donors, day-28 100% donor chimerism, and VOD despite prophylaxis. A current center page supports a facility signal, while a generic Rp800 million to Rp2 billion hospital range remains non-itemized and non-thalassemia-specific. Two selected cases do not establish routine access, scale, durability, safety, payer coverage, or affordability. |
| RSUP Dr. Kariadi government HSCT | `adult_malignancy_hsct_execution_and_cost_audit_benchmark_only` | A 45-adult malignant-disease cohort establishes 38 autologous and 7 allogeneic procedures from 2013-2023, while a three-pair acute-leukemia study adds a 2023-2024 allogeneic activity-based cost benchmark. The cost paper contains two incompatible total, phase, and recovery-ratio calculation sets. No thalassemia case, current license decision, complete safety denominator, corrected cost, or payer evidence supports a thalassemia execution or affordability claim. |
| BUSULFEX conditioning input | `indonesia_registered_conditioning_product_benchmark_only` | A current official BPOM record confirms one valid intravenous busulfan product registration and an Indonesian importer and repacker. The approved product information is not thalassemia-specific and provides no hospital stock, procurement, monitoring-capacity, payer, or delivered-cost evidence. |
| Treosulfan-thiotepa-fludarabine HSCT | `matched_family_donor_conditioning_benchmark_only` | A retrospective 74-child Indian cohort reports 95% five-year overall survival and 88.3% thalassemia-free survival in a combined matched-family group, compared with 57.3% for both estimates in a combined alternative-donor group. No concurrent busulfan comparator, adjusted donor-specific result, complete safety denominator, itemized cost, or Indonesia access supports reduced-toxicity, donor-agnostic, or affordable-route promotion. |
| F-BMT haploidentical HSCT | `conditioning_benchmark_only` | A prospective 29-person cohort reports 93.1% two-year thalassemia-free and overall survival with no graft failure. Single-center design, incomplete abstract-level safety attribution, possible overlap with an earlier multicenter cohort, and absent delivered cost block affordable-route promotion. |
| FT007 lentiviral gene addition | `active_registry_benchmark_only` | The nine-person phase 2b record is now recruiting with an actual start, but design and outcomes did not change and no results are posted. Conditioning, product and clonal safety, durability, manufacturing failures, delivered cost, and Indonesia access remain unresolved. |
| Approved or late gene-cell therapy | `benchmark_only` | Pediatric exa-cel confirms transfusion-independence potential, but adult TDT process evidence now adds repeat mobilization, multiple-product-lot use, and an FDA-described relatively high clinical-lot failure rate with redacted counts. Full myeloablation, a reported fatal busulfan-related event, required long-term safety surveillance, incomplete commercial denominators, and missing delivered cost leave conditioning, safety, access, center, and cost gaps open. BRL-101 has no posted outcomes. HGI-001 now has a source-linked five-child pilot, but its small conflicted evidence base, busulfan route, and missing delivered cost keep it at an early clinical benchmark. |
| Beti-cel lentiviral beta-globin gene addition | `durable_long_term_transfusion_independence_benchmark_only` | A 63-participant pooled follow-up reports durable transfusion independence at median 5.9 years. Separate process evidence now quantifies repeat mobilization in 13 of 66 parent-study participants, three preinfusion discontinuations, eight treated among 15 screened in Germany, and two repeat collections after out-of-specification release results among ten collected at one United States center. Complete commercial referral-to-infusion, failed-lot, itemized-cost, Indonesia, center-capacity, and payer denominators remain unresolved. |
| EDIT-301 / reni-cel HBG promoter editing | `corrected_early_clinical_hbg_promoter_editing_benchmark_only` | A formal NEJM correction limits the day-42 claim to neutrophil engraftment and replaces incorrect adverse-event percentages with 5-of-9, 5-of-9, and 6-of-9 participant counts. Nine-person, nonprespecified, short-follow-up evidence, stopped development, busulfan conditioning, and missing delivered cost and access evidence block promotion. |
| CD34-targeted in vivo HSPC editing | `preclinical_in_vivo_hspc_delivery_benchmark_only` | Anti-CD34 LNP delivery produced persistent BCL11A-enhancer editing and increased HBG relative to beta-like globin RNA after intrafemoral dosing in humanized mice. No TDT donor denominator, therapeutic disease-phenotype endpoint, systemic therapeutic route, broad genomic safety, large-animal result, delivered cost, or Indonesia path supports affordable-route promotion. |
| KIT epitope-edited conditioning | `replicated_preclinical_conditioning_benchmark_only` | A peer-reviewed study independently joins the July preprint in supporting antibody selection of KIT-shielded HSPCs. It adds serial repopulation and genomic-safety experiments, but uses healthy-donor and SCD cells in female immunodeficient mice, not beta-thalassemia donor cells or a TDT disease model. BCL11A off-target deamination, PE3 indels and translocations, absent clinical results, and missing delivered cost block further promotion. |
| Apheresis-waste CD34-positive HSPC recovery | `preclinical_hemoglobinopathy_material_recovery_benchmark_only` | A new preprint reports useful CD34-positive cell recovery and mouse engraftment from clinical apheresis waste, but its verified abstract lacks a beta-thalassemia donor denominator, erythroid and globin endpoints, cost, and Indonesia access. Keep it outside the current quote until the disease-material claim is auditable. |
| Hydroxyurea | `affordable_clinical_comparator` | Useful low-cost HbF comparator; not a cure claim and not case-specific. |
| GATAD2A-CHD4 interface within `MBD2-NuRD` | `preclinical_hbf_probe_benchmark_only` | A structure-defined interaction now has genetic and lentiviral peptide HbF evidence in HUDEP-2 and primary adult erythroid cells. No cell-active therapeutic molecule, beta-thalassemia donor-cell result, long-term safety, delivery, manufacturing, cost, or access path supports further promotion. |
| Epigenetic HbF / `DNMT1` | Decitabine `blocked`; DMT207 `partial_hbf_reproduction_only` | DMT207 adds disease-cell and short mouse evidence but lacks a qualified material route, diverse-genotype replication, long-term safety, practical delivery, cost, total-hemoglobin, or transfusion evidence. |
| Sirolimus, `PRKAB1`/autophagy, `T-BDMC` | `hold_for_endpoint_or_identity_gap` | Assay-only until identity, HbF, chain balance, hemolysis, viability, and safety endpoints are present. |
| Resveratrol | `ntdt_iron_overload_comparator_only`; HbF quote `deprioritized` | A small randomized 2026 abstract reports lower six-month serum ferritin, but not HbF, hemoglobin, transfusion burden, organ iron, durability, or delivered cost. Earlier randomized evidence does not establish a decision-useful HbF or transfusion effect. |
| Thalidomide class | `high_caution_response_benchmark_only` | A 2026 GRADE synthesis supports on-treatment HbF, hemoglobin, and transfusion-response signals, but low-certainty response evidence, extreme heterogeneity, cohort overlap, adverse-event underreporting, thrombosis, regulator-label hazards, and missing delivered cost block therapeutic promotion. |
| Melittin hazard lane | `reject_hazard_or_unmeasured_claim` | Hemolysis and anaphylaxis risk block therapeutic promotion without a new safety-resolution package. |
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

The August 2026 apheresis-waste preprint narrows a different blocker: recovery
of patient-derived CD34-positive HSPCs for preclinical validation. It does not
yet close the beta-thalassemia material-source gap because the verified abstract
does not provide a diagnosis-specific donor denominator. The route must first
establish beta-thalassemia donor provenance, then erythroid and globin function,
safety, research governance, and a lower cost per qualified aliquot before it
can improve the assay-access ranking.

The August 2026 reni-cel correction resolves a source-level contradiction in an
existing clinical editing benchmark. The corrected record supports day-42
neutrophil engraftment, not day-42 neutrophil and platelet engraftment, and
restores the actual common grade 3 or 4 adverse-event denominators. This keeps
the efficacy signal usable for comparison while strengthening the safety and
durability hold.

The August 2026 CD34-targeted LNP study addresses delivery rather than disease
efficacy. It shows persistent in vivo editing of human HSPCs in mice, but its
intrafemoral route, non-TDT therapeutic model, limited safety package, and
missing cost leave the ex vivo manufacturing and conditioning gap open. A
separate `HbbTh3/+` experiment adds short-window serum safety measurements for
the base LNP with luciferase payload, not therapeutic editing or disease rescue.
The 2025 antibody-free intravenous LNP study remains the closer disease-specific
TDT comparator.

The peer-reviewed KIT epitope-editing study independently strengthens the
non-genotoxic conditioning concept. Anti-KIT selection preserved shielded,
multilineage, serially repopulating human hematopoiesis in immunodeficient mice.
It also exposes an editor-specific safety split: KIT epitope edits were clean in
the reported candidate-site assays, while BCL11A base editing produced
off-target deamination and BCL11A PE3 produced high on-target indels plus
translocation evidence. The study used healthy-donor and SCD cells rather than
TDT cells, and no clinical or delivered-cost result exists. The lane therefore
moves from one-study proof of concept to a replicated preclinical benchmark,
not to an affordable-curative route.

The long-term beti-cel paper closes a different gap: durability of autologous
lentiviral beta-globin gene addition. Fifty-two of 63 participants achieved
transfusion independence, sustained through last follow-up, and 51 participants
had at least five years of observation. No malignancy, insertional oncogenesis,
or vector-derived replication-competent lentivirus was reported. This promotes
the lane to a durable long-term transfusion-independence benchmark, not an
affordable route. Only two participants had ten years of follow-up, the phase
3 process performed better than phase 1/2, the parent studies were
nonrandomized, and the route still requires individualized manufacture plus
full busulfan myeloablation. No failed-batch denominator, itemized delivered
cost, Indonesia authorization, qualified-center capacity, or payer route was
reported.

The adult exa-cel trial and FDA manufacturing review now close part of the
comparison gap created by the beti-cel process update. All 59 adult TDT
participants started mobilization and 52 received exa-cel at the interim
cutoff. Nineteen percent of infused participants needed more than one
mobilization cycle, with a range of one to four. FDA's CMC reviewer separately
described a relatively high clinical-lot failure rate and multiple-lot use, but
the exact counts and rates are redacted. This rejects an assumed exa-cel
collection or manufacturing advantage. It does not support a numerical cross-
product comparison or an affordable-route promotion.

## August 13 Exa-Cel Process-Burden Decision

**Question:** Do adult TDT trial and FDA manufacturing records establish a
collection or manufacturing advantage for exa-cel over beti-cel that is strong
enough to change the affordable-curative route ranking?

**Decision:**
`hold_exa_cel_at_strong_curative_benchmark_only_after_process_burden_quantification`.

- **Fact - process denominator:** In adult trial `NCT03655678`, 59
  participants started mobilization, 53 started busulfan conditioning, and 52
  received exa-cel at the January 16, 2023 interim cutoff. Three discontinued
  after mobilization and before conditioning. The visible review does not
  provide final dispositions for the other four participants outside the
  infused and documented-discontinuation groups.
- **Fact - repeat collection:** Eighty-one percent of the 52 infused
  participants required one mobilization cycle. The other 19% needed more than
  one, with a range of one to four. The current FDA label requires backup-cell
  collection and allows additional cycles when the minimum product dose is not
  met.
- **Fact - manufacturing:** FDA's CMC review states that some participants
  needed multiple product lots. The attempted-lot, rejected-lot, and
  indication-specific failure counts are redacted, but the reviewer describes
  a relatively high failure rate and names visible causes including starting-
  material contamination and inadequate cell number.
- **Comparator boundary:** Beti-cel's parent-study collection analysis starts
  with all 66 participants who initiated mobilization, while exa-cel's cycle
  distribution is reported among the 52 infused participants. These are not
  denominator-aligned rates and cannot establish equivalence or superiority.
- **Interpretation:** Exa-cel remains a strong curative benchmark, not an
  affordable route. Future comparisons must count every attempted product lot,
  not only accepted and infused product.
- **Affordability gate:** No reviewed source supplies complete commercial
  referral-to-infusion throughput, exact exa-cel clinical-lot failure rates,
  itemized delivered cost, Indonesia manufacture or authorization, center
  capacity, or payer evidence. Matched-sibling HSCT remains the leading
  affordable-curative route benchmark for its narrow studied scope.
- **Falsification criterion:** Deprioritize exa-cel as an affordable-route
  candidate if a complete commercial cohort shows persistent collection or lot
  failure, unacceptable conditioning or admission burden, or no credible total-
  cost and capacity advantage over beti-cel while approaching matched-sibling
  HSCT.
- **Next decisive action:** Obtain exa-cel and beti-cel commercial cohorts with
  identical referral, authorization, collection, attempted-lot, released-lot,
  rejected-lot, infusion, complication, durable-outcome, and itemized-cost
  fields. Compare the same fields with the narrow matched-sibling HSCT
  benchmark. No patient action or sample routing follows.

## August 12 Beti-Cel Process-Attrition Decision

**Question:** Do denominator-aligned clinical-trial and real-world collection
data close beti-cel's process and affordability gaps enough for promotion?

**Decision:**
`hold_beti_cel_at_durable_long_term_transfusion_independence_benchmark_only_after_process_attrition_quantification`.

- **Fact - parent studies:** A pooled conference abstract reports that 52 of 66
  participants, 78.8%, reached the collection target after one mobilization
  cycle and 13, 19.7%, after two. One had unsuccessful mobilization and
  withdrew. An FDA presentation separately accounts for three people not
  treated among the 66-person intent-to-treat population: inadequate
  mobilization, pregnancy, and withdrawal of consent. These were not three
  manufacturing failures.
- **Fact - German implementation:** A peer-reviewed study reports eight treated
  among 15 evaluated. Four withdrew by choice, two were excluded for severe
  hepatic siderosis, and one had collection failure. Seven treated participants
  required one collection; one required a second after CD34-positive-cell loss
  during manufacturing. Median apheresis-to-infusion time was 113 days and
  median discharge was 31.5 days after infusion. All eight were insured; costs
  exceeded allogeneic HSCT, but no itemized amount was reported.
- **Fact - United States implementation:** A one-center conference abstract
  reports ten commercial collections. Eight required one cycle and two needed
  a second after out-of-specification release testing. Nine had been infused;
  the abstract does not resolve the tenth person's final status. Early safety
  included three VOD events and clinically significant bleeding in seven of
  nine infused participants during prolonged thrombocytopenia.
- **Interpretation:** Replace the generic collection gap with measured repeat
  collection, attrition, delay, admission, and complication burdens. Do not
  promote affordability, comparative safety, Indonesia access, or individual
  suitability. Matched-sibling HSCT remains the leading affordable-curative
  benchmark.
- **Affordability gate:** No source reports a complete commercial
  referral-to-infusion denominator, final failed-lot denominator, itemized
  delivered cost, insurance denials, Indonesia delivery, or matched process
  comparison against exa-cel and matched-sibling HSCT.
- **Falsification criterion:** Deprioritize beti-cel as an affordable-route
  candidate if a complete implementation cohort shows persistent collection or
  release failure, unacceptable conditioning or bleeding burden, or no credible
  activity-based total-cost and capacity advantage over exa-cel while
  approaching matched-sibling HSCT.
- **Next decisive action:** Obtain one owner-verified commercial cohort starting
  with all referrals and reporting authorization, collection, released and
  discarded lots, infusion, admission, complications, surveillance, and
  itemized payer-relevant cost. Compare identical fields across beti-cel,
  exa-cel, and matched-sibling HSCT. No patient action or sample routing follows.

## August 11 Long-Term Beti-Cel Decision

**Question:** Does the 63-participant long-term beti-cel study justify promotion
from a clinical benchmark to an affordable curative route for TDT?

**Decision:**
`promote_beti_cel_to_durable_long_term_transfusion_independence_benchmark_only`.

- **Fact:** DOI `10.1182/blood.2025029196`, PMID `41525466`, reports 63 treated
  participants from four nonrandomized phase 1/2 or phase 3 parent studies who
  entered long-term follow-up. Median age was 17 years and median follow-up was
  5.9 years, range 2.9 to 10.1.
- **Durability gate:** Fifteen of 22 phase 1/2 participants, 68.2%, and 37 of 41
  phase 3 participants, 90.2%, achieved transfusion independence and sustained
  it through last follow-up. Fifty-one participants had at least five years of
  follow-up, while only two had ten years.
- **Biological gate:** Vector copy number and beta-A-T87Q hemoglobin were stable
  from month six through last follow-up. Thirty-eight of 52 participants who
  achieved transfusion independence had stopped iron chelation at last
  follow-up without an increase in liver iron concentration.
- **Safety gate:** No malignancy, insertional oncogenesis, or vector-derived
  replication-competent lentivirus was reported at the February 2024 cutoff.
  The active long-term registry remains incomplete and the FDA label retains a
  potential insertional-oncogenesis warning plus annual monitoring for at least
  15 years.
- **Denominator boundary:** `NCT02633943`, `LTF-303`, currently lists 66 actual
  enrollees and no posted results. That enrollment is not the paper's treated or
  outcome denominator and must not be merged with the 63-person analysis.
- **Manufacturing boundary:** Phase 3 manufacturing increased transduction
  efficiency, drug-product vector copy number, beta-A-T87Q hemoglobin, and the
  transfusion-independence rate relative to phase 1/2. The pooled result does
  not represent one uniform process.
- **Conditioning boundary:** The FDA label requires mobilization, apheresis,
  backup-cell collection, individualized manufacture and testing, and full
  busulfan myeloablation. Its separate 41-person safety cohort reported serious
  adverse reactions in 37%, including three serious VOD events. The label
  states that its adverse-event tables include busulfan-associated events, so
  the route-level burden cannot be assigned to beti-cel alone.
- **Hypothesis:** A transferable phase 3-like beti-cel process can become an
  affordable route only if it preserves durability with low repeat-collection
  and failed-lot rates, reduces conditioning and hospital burden, and improves
  total delivered cost and capacity against exa-cel while approaching
  matched-sibling HSCT.
- **Interpretation:** Promote durability evidence, not affordability,
  comparative safety, Indonesia access, or individual suitability.
- **Affordability and access:** The label describes a target collection of at
  least 12 million CD34-positive cells per kilogram, possible repeat collection
  and manufacture, backup-cell storage, full busulfan conditioning, hospital
  care, and about 70 to 90 days for manufacture and testing. The paper reports
  no itemized delivered cost, manufacturing-failure denominator, Indonesia
  authorization, qualified-center capacity, technology transfer, or payer
  coverage. Exact `ZYNTEGLO` and `betibeglogene` BPOM product-name and
  ingredient searches returned zero public records on 2026-08-11; this is not
  proof of absence or unavailability.
- **Open question:** What are the denominator-aligned manufacturing-failure,
  repeat-collection, bridge-care, admission, complication, fertility,
  surveillance, and payer costs for a phase 3-like route in an Asian delivery
  setting?
- **Falsification criterion:** Deprioritize beti-cel as an affordable-route
  candidate if a denominator-aligned implementation study fails to preserve
  durability, reveals unacceptable clonal or malignant risk, cannot reduce
  conditioning and manufacturing burden, or cannot show a credible total-cost
  and capacity advantage over exa-cel while approaching matched-sibling HSCT.
- **Next decisive action:** Obtain one owner-verified dataset covering attempted
  and repeat collections, released and failed lots, release time, bridge care,
  conditioning, admission, complications, fertility, surveillance, and
  payer-relevant cost. Compare the same fields with exa-cel and matched-sibling
  HSCT. No patient action, referral, or sample routing follows.

## August 10 KIT Epitope-Editing Conditioning Decision

**Question:** Does peer-reviewed KIT epitope editing independently close the
conditioning, safety, and affordability gaps enough for promotion beyond a
preclinical beta-thalassemia benchmark?

**Decision:**
`hold_kit_epitope_editing_at_replicated_preclinical_conditioning_benchmark_only`.

- **Fact:** DOI `10.1038/s41586-026-10737-8`, PMID `42420446`, reports KIT
  H378R base editing or KIT D121L prime editing combined with BCL11A-enhancer
  editing and anti-KIT selection. Shielded HSPCs supported multilineage primary
  and secondary engraftment after antibody conditioning in female NBSGW mice.
- **Evidence tier:** This peer-reviewed study is independent from the July
  `CIM058` beta-thalassemia preprint, so the core platform is now replicated.
  The reporting summary identifies eight healthy donors and SCD cells, not TDT
  cells, and no beta-thalassemia disease model.
- **Safety gate:** Three-donor candidate-site testing found no detected
  off-target substitution from prime editing, but BCL11A base editing produced
  off-target deamination. BCL11A PE3 produced on-target indels up to 44.8% in
  HSPCs, with translocation evidence in two of three donors. Promotion requires
  an optimized editor and a qualified broad genomic and clonal release package.
- **Clinical boundary:** `NCT05357482` remains active, not recruiting, with 40
  actual participants in a study covering sickle cell disease and
  beta-thalassemia, but no condition-stratified enrollment or posted results.
  It combines briquilimab with low-dose irradiation and other transplant
  medicines, not epitope-edited HSPCs or antibody-only conditioning.
- **Hypothesis:** KIT shielding can replace genotoxic conditioning only if it
  preserves a diverse long-term graft, rescues beta-thalassemia biology, and
  reduces total harm without adding prohibitive manufacturing and hospital cost.
- **Interpretation:** Promote confidence in platform replication, but hold the
  route at a preclinical conditioning benchmark. Do not infer clinical efficacy,
  beta-thalassemia cure, lower risk, access, or affordability.
- **Falsification criterion:** Deprioritize if matched TDT-donor and
  immunocompetent large-animal comparisons fail disease-relevant rescue or
  durable multilineage repopulation after antibody withdrawal, breach genomic,
  clonal, immune, organ, fertility, or hematopoietic safety gates, or fail to
  improve delivered cost and infrastructure against exa-cel while approaching
  matched-sibling HSCT.
- **Next decisive action:** Compare KIT plus therapeutic editing with anti-KIT
  selection against the same therapeutic edit with conventional conditioning
  and no-antibody controls. Use at least three genotype-diverse TDT donors, an
  immunocompetent large-animal arm, broad safety endpoints, batch-failure
  accounting, and an activity-based delivered-cost model.

## August 9 CD34-Targeted In Vivo HSPC Editing Decision

**Question:** Does CD34-targeted in vivo HSPC editing close the ex vivo
manufacturing and conditioning gap enough to become an affordable curative
route?

**Decision:**
`hold_cd34_lnpdp_at_preclinical_in_vivo_hspc_delivery_benchmark_only`.

- **Fact:** DOI `10.1038/s41551-026-01765-w`, PMID `42557300`, reports
  anti-CD34-conjugated LNP delivery of SpCas9 messenger RNA and a
  BCL11A-enhancer guide by bilateral intrafemoral injection in humanized mice.
  Marrow analysis 12-16 weeks later found persistent editing and increased
  `HBG/(HBB+HBG)` RNA without a reported change in measured human-cell,
  lineage, or erythroid fractions.
- **Evidence tier:** This is peer-reviewed preclinical evidence. No formal
  sample-size calculation was performed, only female mice were used, and the
  reporting summary does not identify a beta-thalassemia donor denominator,
  genotype, or phenotype.
- **Disease and safety gap:** No beta-thalassemia phenotype, globin-chain
  balance, hemolysis, red-cell survival, or transfusion endpoint was tested.
  The supplement's organ-indel assay is not an unbiased genome-wide off-target
  analysis. Serum markers and cytokines were measured through 72 hours after
  `LNPDP-Luc` dosing in four `HbbTh3/+` mice, while bone-marrow cytokines ended
  at 48 hours in humanized NOG mice and histology ended at one week in C57BL/6J
  mice. These split-model, luciferase-payload checks do not establish
  editor-specific or long-term safety.
- **Comparator:** DOI `10.1038/s41551-025-01480-y`, PMID `40796944`, already
  reports antibody-free intravenous LNP HBG1/HBG2 editing in TDT
  patient-derived HSPCs in humanized mice with a globin-chain-balance endpoint.
  The new platform does not displace that comparator.
- **Hypothesis:** Systemic non-viral delivery could reduce apheresis, ex vivo
  manufacture, and conditioning if it reaches long-term HSCs at a therapeutic
  fraction with acceptable genomic, clonal, organ, inflammatory, and
  reproductive safety.
- **Interpretation:** Keep CD34/LNPDP as a delivery-platform benchmark only.
  Intrafemoral administration and antibody-conjugated LNP manufacture do not
  establish a simpler, scalable, or cheaper route.
- **Affordability and access:** No GMP release path, manufacturing-failure
  denominator, dose-scaled cost, procedure cost, authorization, payer evidence,
  or Indonesia capacity is reported.
- **Falsification criterion:** Deprioritize if systemic dosing fails to
  reproduce durable disease-relevant benefit across at least three independent
  TDT donors, breaches a prespecified genomic, clonal, organ, inflammatory, or
  hematopoietic safety gate, or does not lower delivered cost and infrastructure
  against the ex vivo comparator.
- **Next decisive action:** Compare CD34-targeted and antibody-free LNPs
  head-to-head with the same editor, systemic route, TDT donor panel, long-term
  disease and safety endpoints, editor-matched controls, and an activity-based
  delivered-cost model.

## August 8 Reni-cel Correction Decision

**Question:** Does the formal correction to the nine-person reni-cel report
support promotion beyond an early clinical HBG-promoter-editing benchmark?

**Decision:**
`hold_reni_cel_at_corrected_early_clinical_hbg_promoter_editing_benchmark_only`.

- **Fact:** The [primary phase 1-2 report](https://doi.org/10.1056/NEJMoa2501277)
  covers nine adults with TDT across beta-zero/beta-zero, beta-plus/beta-plus,
  beta-zero/beta-plus, and HbE/beta-zero genotypes. It used autologous
  AsCas12a-edited CD34-positive HSPCs to disrupt BCL11A binding sites in the
  `HBG1` and `HBG2` promoters after myeloablative busulfan conditioning.
- **Fact:** The [formal correction](https://doi.org/10.1056/NEJMx260013)
  limits the day-42 claim to neutrophil engraftment. Table 1 reports platelet
  engraftment from day 23 through day 49.
- **Fact:** The correction replaces incorrect narrative rates with decreased
  platelet count in 5 of 9 participants across 13 events, decreased neutrophil
  count in 5 of 9 across 12 events, and stomatitis in 6 of 9 across 6 events.
  The report records 69 grade 3 or 4 events and six serious events in four
  participants.
- **Evidence tier and phenotype scope:** The sponsor-funded study was
  multicenter but open-label, single-group, terminated early, and analyzed
  nonprespecifically. All nine were transfusion-free at their last observed
  visit, but only six could be evaluated for at least 12 months of transfusion
  independence. This is adult TDT early clinical evidence, not durable-cure
  evidence.
- **Safety risk:** Myeloablative conditioning, cytopenias, stomatitis,
  infection, pneumonitis, and unresolved late genomic, marrow, malignancy,
  organ, endocrine, and fertility risks remain route-level constraints. No
  death or malignancy was reported by the early data cutoff.
- **Conflict:** The current public
  [`NCT05444894`](https://clinicaltrials.gov/study/NCT05444894) record remains
  active, not recruiting, with no posted results, while the paper reports early
  termination after development was discontinued. The 15-year
  [`NCT06363760`](https://clinicaltrials.gov/study/NCT06363760) follow-up has no
  posted results.
- **Hypothesis:** Corrected long-term follow-up can retain the modality as a
  mechanism and durability comparator if editing, hematopoiesis, HbF, and
  transfusion independence remain stable without unacceptable late harm.
- **Interpretation:** The correction preserves the early efficacy benchmark but
  materially tightens safety and engraftment traceability. It does not support
  an active development, clinical route, affordability, access, or safety
  promotion.
- **Affordability and access:** No itemized manufacturing cost, scaled
  commercial manufacturing-failure rate, delivered price, Indonesia
  authorization, qualified-center capacity, payer coverage, or total follow-up
  cost is reported. Stopped development blocks a current access-route
  inference.
- **Falsification criterion:** Deprioritize even the benchmark if corrected
  follow-up does not sustain editing, HbF, or transfusion independence, or if
  death, malignancy, clonal expansion, marrow failure, organ harm, endocrine or
  fertility harm, or manufacturing failure makes the profile unacceptable.
- **Next decisive action:** A research evidence owner should reconcile the
  corrected abstract, Results narrative, Table 1, Table 2, parent registry, and
  long-term follow-up, then obtain a complete participant-level denominator
  separating product, busulfan, transplant, and late follow-up harms.

## August 5 Apheresis-Waste CD34-Positive HSPC Recovery Decision

**Question:** Does the verified apheresis-waste preprint record close the
beta-thalassemia cell-source gap enough to enter the current affordable HbF and
globin-chain-balance quote?

**Decision:**
`hold_apheresis_waste_cd34_hspcs_at_preclinical_hemoglobinopathy_material_recovery_benchmark_only`.

This replaces the morning promotion label after a source-depth audit. It keeps
the lead outside the current quote, does not promote a therapeutic candidate,
and does not alter the current curative-route ranking.

- **Fact:** BioRxiv version 1, DOI `10.64898/2026.08.02.742313`, reports a
  median 4.71 million CD34-positive cells recovered from 1-2 mL of clinical
  apheresis product waste. The reported yield was comparable with 6.0 million
  cells from 10-40 times more peripheral-blood waste, with similar purity and
  approximately half the processing time because density-gradient steps were
  avoided. Recovered cells engrafted NBSGW mice.
- **Evidence boundary:** The abstract frames the work around sickle cell
  disease and beta-thalassemia but does not report total patients, independent
  donors, diagnosis-specific counts, a beta-thalassemia donor denominator,
  genotype, phenotype, repeated-specimen structure, erythroid or globin
  outcomes, processing cost, or an Indonesia route. The separate microfluidic
  pilot included two patients and 11 specimens and reported more than 90%
  viability and purity.
- **Conflict:** The title and conclusion frame a beta-hemoglobinopathy biobank,
  but "similar across diagnoses" cannot verify a beta-thalassemia material
  source. The official page and API available to this audit exposed no
  source-linked donor manifest, full results table, supplement, or donor-level
  dataset. The article page lists two funders while the API `funder` field is
  `NA`; the article page declares no competing interest.
- **Hypothesis:** Research-only recovery from otherwise discarded
  beta-thalassemia apheresis product can provide a lower-cost multi-donor
  primary-cell model if provenance, ethics, chain of custody, function, and
  actual cost are independently reproduced.
- **Interpretation:** Concentrated waste material and shorter processing are
  credible hemoglobinopathy recovery signals. They do not verify a
  beta-thalassemia source and are not evidence of affordability, access,
  therapeutic manufacture, or clinical benefit.
- **Open question:** Across at least three genetically distinct
  beta-thalassemia donors, does the route preserve colony formation, erythroid
  maturation, enucleation, HbF, F-cells, total hemoglobin, globin-chain balance,
  free alpha-globin, viability, and hemolysis relative to the current source?
- **Falsification criterion:** Do not enter a quote or experiment if
  beta-thalassemia provenance and the independent-patient and specimen
  denominators cannot be confirmed. Remove or deprioritize the benchmark if
  recovered cells materially underperform the comparator on erythroid, globin,
  or safety endpoints, or if measured cost per qualified aliquot is not lower.
- **Next decisive owner action:** The research evidence owner should obtain a
  source-linked full manuscript or supplement, a de-identified diagnosis and
  donor manifest, independent-patient and specimen denominators, and
  diagnosis-stratified results. Only after beta-thalassemia material is verified
  should a lab-operations owner price a paired research-material feasibility
  line. No outreach or sample routing is authorized here.

## August 4 RSUP Dr. Kariadi HSCT Execution And Cost Decision

**Question:** Do two 2026 primary studies resolve the morning capacity-only
classification strongly enough to promote RSUP Dr. Kariadi as an Indonesia HSCT
execution and cost benchmark?

**Decision:**
`promote_kariadi_to_adult_malignancy_hsct_execution_and_cost_audit_benchmark_only`.

This replaces `government_hsct_capacity_development_benchmark_only`. It does not
promote a thalassemia route. Matched-sibling HSCT remains
`leading_affordable_curative_route_benchmark_only`.

- **Fact - execution denominator:** Primary cross-sectional study PMID
  `42052597` reports 45 adults with malignant diseases who underwent HSCT at
  Kariadi from 2013 through 2023: 38 autologous and 7 allogeneic procedures. The
  diagnoses were multiple myeloma, AML, Hodgkin lymphoma, non-Hodgkin lymphoma,
  ALL, and mixed-phenotype acute leukemia.
- **Fact - endpoint and design:** PMID `42052597` reports mean neutrophil
  engraftment at 14.29 days and mean platelet engraftment at 13.53 days. It is a
  selected complete-record, single-center cohort, not a complete attempted
  denominator or a long-term outcome dataset.
- **Fact - cost evidence:** Primary mixed-method study PMID `42345166` uses
  retrospective activity-based cost data for three acute-leukemia
  donor-recipient pairs who underwent allogeneic HSCT in 2023-2024. Donors were
  related or haploidentical family members. The endpoint was unit cost, not
  efficacy or safety.
- **Mechanism and genotype or phenotype scope:** The papers cover autologous and
  allogeneic HSCT for adult malignancies. The acute-leukemia paper describes
  conditioning plus graft-versus-leukemia activity. Neither study includes
  thalassemia, an `HBB` genotype, TDT or NTDT classification, donor erythropoiesis,
  or transfusion independence.
- **Resolved source tension:** The primary cohorts establish that Kariadi had
  performed HSCT before the June 2026 licensing assessment. They do not identify
  whether the assessment concerned a new license, renewal, scope expansion, or
  another administrative step. Historical execution is not current
  authorization.
- **Unresolved numeric conflict:** The cost paper's abstract and narrative report
  Rp377,978,399 per case, split into Rp297,063,048 for the recipient and
  Rp80,915,351 for the donor. Table 1 instead totals Rp439,598,636, split into
  Rp389,880,946 and Rp49,717,690. Its phase costs and tariff cost-recovery ratios
  also differ between the abstract, narrative, and tables. Neither set may be
  selected without a correction.
- **Evidence tier and safety risk:** This is retrospective, single-center clinical
  and costing evidence. No complete mortality, relapse, graft-failure, VOD,
  infection, GVHD, endocrine, fertility, organ, or long-term denominator was
  reported. Technical execution does not establish acceptable safety.
- **Hypothesis:** Kariadi could support a government thalassemia HSCT route only
  if current authorization, a thalassemia protocol, complete
  screened-through-followed denominators, long-term outcomes, and reproducible
  delivered cost are independently documented.
- **Interpretation:** The lane moves from capacity-only to adult malignancy
  execution plus cost audit. It does not establish thalassemia execution,
  durable transfusion independence, routine access, affordability, payer
  coverage, or suitability.
- **Affordability and access:** The phase-mapped cost study is more informative
  than a generic price range, but its internal arithmetic conflict blocks use as
  an affordability estimate, hospital quote, or payer amount. Its statement that
  HSCT was outside national insurance coverage is study context, not a current
  BPJS decision.
- **Falsification criterion:** Remove the execution benchmark if the center-level
  procedure and transplant-type denominators cannot be reproduced. Keep the cost
  lane audit-only until one corrected calculation reconciles phase totals,
  formulas, inclusions, currency year, and payer scope. Do not promote the
  thalassemia route without durable transfusion independence, acceptable long-
  term safety, and reproducible delivered cost in the relevant population.
- **Next decisive owner action:** The health-economics owner should ask the
  authors and journal for a correction plus the de-identified activity-based
  costing workbook that reconciles the abstract, narrative, and tables. No
  patient routing follows.

## August 2 Indonesia Pediatric HSCT Execution Decision

**Question:** Do the Jakarta two-case report, current center page, and hospital
cost range close enough of the Indonesia delivery gap to promote
matched-sibling HSCT beyond a benchmark-only route?

**Decision:**
`promote_tzu_chi_pediatric_msd_hsct_to_indonesia_execution_benchmark_only`.

This is a local-execution benchmark, not evidence of routine access,
affordability, suitability, or a treatment route. Matched-sibling HSCT remains
`leading_affordable_curative_route_benchmark_only`.

- **Fact - mechanism and scope:** APBMT abstract `A-198` reports two pediatric
  beta-thalassemia major cases treated with allogeneic HSCT at Tzu Chi Hospital
  Jakarta. Both donors were HLA-matched brothers. The report does not state
  `HBB` genotype or current TDT classification.
- **Fact - endpoint:** The report states `Bu4Cy2+ATG` and `Bu4Cy4+ATG`
  conditioning. Neutrophil engraftment occurred on days 11 and 12, platelet
  engraftment on days 43 and 25, and both cases had 100% donor chimerism at day
  28. The regimen strings are reported evidence, not protocol guidance.
- **Evidence tier and safety:** This is a two-case conference report without a
  comparator or complete attempted denominator. Both cases developed VOD
  despite ursodeoxycholic-acid prophylaxis and received defibrotide plus
  low-molecular-weight heparin. The report gives no transfusion-independence,
  survival, graft-failure, infection, GVHD, fertility, endocrine, organ, or
  quality-of-life outcome beyond the short engraftment window.
- **Resolved source overlap:** The 2023 APBMT abstract described the first case
  during screening. The 2024 report includes two transplanted cases. Count the
  newer report as two cases with at least one overlapping earlier case, not
  three independent transplants.
- **Current facility signal:** The hospital's current page lists trained
  pediatric transplant staff, apheresis equipment, sterile recovery rooms, and
  diagnostic support. It does not state current thalassemia case volume or
  outcomes.
- **Affordability and access:** A September 2025 hospital article gives a
  general Indonesian HSCT range of Rp800 million to Rp2 billion. It is not an
  itemized thalassemia quote or payer decision and is not directly comparable
  with the 2026 LMIC cohort's USD 8,000-10,000 mean.
- **Hypothesis:** A governed Indonesian pediatric matched-sibling HSCT program
  can reproduce durable transfusion independence with acceptable toxicity only
  if its complete attempted denominator, pharmacokinetic monitoring, long-term
  outcomes, and delivered cost are measured prospectively.
- **Interpretation:** The local delivery gap is narrowed to two-case execution.
  The two VOD events and absent denominator, durability, capacity, and cost data
  keep the route at `benchmark_only`.
- **Open question:** Since the first 2023 case, how many children have been
  screened, conditioned, transplanted, engrafted, and followed, and what are
  their complete one-, two-, and five-year outcomes and costs?
- **Falsification criterion:** Remove the execution benchmark if the center
  cannot confirm an ongoing governed service or a complete attempted
  denominator. Remove the leading affordable-route label if modern follow-up
  shows unacceptable death, graft failure, VOD, infection, GVHD, endocrine or
  fertility harm, loss of transfusion independence, or itemized Indonesia cost
  above the program threshold.
- **Next decisive action:** A transplant-program owner should produce one
  public-safe center dataset with screened, conditioned, transplanted, and
  followed denominators; phenotype, genotype, donor and regimen scope;
  busulfan pharmacokinetic monitoring; engraftment, transfusion, survival,
  VOD, infection, GVHD, organ, endocrine, and fertility outcomes; and follow-up
  dates. A health-economics owner should reconcile it with an itemized hospital
  and payer cost model. No patient routing follows.

## August 2 BPOM BUSULFEX Conditioning-Input Decision

**Question:** Does the current BPOM BUSULFEX record close the Indonesia
conditioning-access gap enough to promote matched-sibling HSCT beyond a
benchmark-only route?

**Decision:**
`promote_busulfex_to_indonesia_registered_conditioning_product_benchmark_only`.

This is a component-level regulatory finding. Matched-sibling HSCT remains
`leading_affordable_curative_route_benchmark_only`.
The evidence is newly integrated into the repo, not a new 2026 approval.

- **Fact - public registration:** The August 2 CekBPOM product-name query
  returns BUSULFEX registration `DKI1905000743A1` with status `Berlaku`, a
  product date of 2024-03-01, expiry of 2029-03-01, and Otsuka Indonesia as the
  named manufacturer entry.
- **Fact - product identity:** BPOM-approved product information identifies a
  6 mg/mL intravenous busulfan product manufactured in Germany and imported
  and repacked by PT Otsuka Indonesia. The document was approved on 2024-02-27.
- **Indication boundary:** The approved product information describes
  conditioning before allogeneic transplantation for chronic myelogenous
  leukemia. It does not establish a thalassemia indication, protocol, or
  patient route.
- **Safety and infrastructure boundary:** The product information requires
  experienced transplant supervision, adequate diagnostic and treatment
  facilities, pharmacokinetic monitoring, and intensive support for profound
  myelosuppression and other serious toxicities. Product registration does not
  resolve conditioning safety or center capacity.
- **Resolved search contradiction:** Searching the public database by product
  name returned two BUSULFEX package rows, while searching product name or
  ingredient for `busulfan` returned zero. Ingredient-only negative searches
  therefore cannot support a general absence claim.
- **Interpretation:** The product-identity and public-registration gap for one
  busulfan conditioning input is narrower than the prior generic Indonesia
  access statement implied. The route-level access, safety, and affordability
  gates remain open.
- **Confidence:** High that a current public BPOM record exists for the named
  product. Low that the record translates into thalassemia use, current stock,
  procurement, monitoring capacity, payer coverage, or affordable delivery.
- **Hypothesis:** A governed Indonesian transplant program can include a
  BPOM-registered intravenous busulfan input only if a qualified center can
  verify institutional availability, thalassemia-specific protocol governance,
  pharmacokinetic monitoring, supportive-care capacity, and itemized total
  delivered cost.
- **Open question:** Can one Indonesian transplant center verify all of those
  capabilities without exceeding the program's delivered-cost threshold?
- **Affordability and access:** The public sources contain no price, stock,
  procurement lead time, hospital formulary, pharmacokinetic assay price,
  supportive-care cost, complication cost, or payer decision. Registration is
  not availability or affordability.
- **Falsification criterion:** Remove even the component-level access bridge if
  qualified center and pharmacy verification cannot confirm institutional
  availability and pharmacokinetic monitoring, or if the itemized route cost
  exceeds the program threshold. Do not promote the HSCT route beyond
  `benchmark_only` without independent modern outcomes and center-level
  capacity and cost evidence.
- **Next decisive action:** A transplant-program and health-economics owner
  should produce one public-safe Indonesia center-capacity and itemized-cost
  dataset covering product availability, pharmacokinetic monitoring,
  transplant staffing, supportive care, complication management, and
  follow-up. No patient routing or treatment recommendation follows.

## August 1 GATAD2A-CHD4 Interface Decision

**Question:** Does the newly indexed structure and erythroid-cell evidence
resolve enough of the MBD2-NuRD target blocker to justify a candidate-specific
affordable-cure experiment?

**Decision:**
`promote_gatad2a_chd4_interface_to_preclinical_hbf_probe_benchmark_only`.

The decision promotes a target-specific probe experiment, not a molecule,
treatment, or cure candidate. Matched-sibling HSCT remains the leading
affordable-curative route benchmark only.

- **Fact - mechanism and endpoint:** PMID `42539289` maps the GATAD2A CR2 helix
  to the CHD4 C-terminal domain. GATAD2A `L387P/L390P` prime editing in HUDEP-2
  cells produced 39% HbF by HPLC versus 7% in the prime-editing control.
  Lentiviral intracellular expression of the CR2 helix in primary adult
  CD34-positive HSPC-derived erythroid cells produced 74% HbF versus 8.9% with
  the mutant peptide control.
- **Fact - genotype and phenotype scope:** The paper does not state the
  primary-cell donor count and does not test beta-thalassemia donor cells, TDT,
  NTDT, transfusion burden, total hemoglobin, or clinical benefit. Application
  to beta-thalassemia is a mechanistic hypothesis.
- **Resolved contradiction:** The abstract describes about 40% HbF versus less
  than 1% in control HUDEP-2 cells, while Figure 3F reports 39% versus 7% by
  HPLC. The figure-bound values define the quantitative comparison.
- **Fact - modality:** The functional peptide was expressed by lentivirus.
  Companion PMID `42282813` reports low-nanomolar macrocyclic binders in
  purified biochemical assays, but no cell permeability or cellular HbF result.
- **Evidence tier:** Unreviewed preclinical structure, biophysics, genetic
  perturbation, lentiviral peptide expression, and short human erythroid-cell
  evidence.
- **Safety risk:** Short differentiation-marker results do not resolve broad
  chromatin-complex risk. Edited HUDEP-2 cells had about 50% lower `HBB` RNA,
  and RNA sequencing found 89 upregulated and 35 downregulated genes, including
  embryonic globins `HBE1` and `HBZ`. Long-term marrow, organ, genotoxicity, and
  in vivo safety were not tested.
- **Hypothesis:** A selective, cell-permeant inhibitor can reproduce HbF
  protein and F-cell induction in genetically distinct beta-thalassemia donor
  erythroid cultures while preserving globin balance, viability, maturation,
  and enucleation.
- **Interpretation:** The structure-defined interface resolves the broad-target
  blocker enough for probe development. It does not resolve disease-cell,
  safety, delivery, durability, manufacturing, affordability, or access gaps.
- **Open question:** Can a chemically defined inhibitor enter erythroid cells
  and reproduce the HbF effect without broad NuRD or embryonic-gene
  derepression?
- **Affordability and access:** No administered product, scalable synthesis,
  pharmacokinetic route, manufacturing package, delivered cost, or Indonesia
  access path is reported. Avoiding ex vivo therapy remains a future
  hypothesis, not an affordability result.
- **Falsification criterion:** Deprioritize if a chemically verified,
  cell-permeant inhibitor cannot raise HbF protein and F-cell percentage in at
  least three genetically distinct beta-thalassemia donor cultures while
  preserving viability, maturation, enucleation, and alpha/non-alpha globin
  balance, or if transcriptome, safety, manufacturing, or cost boundaries fail.
- **Next decisive action:** Medicinal chemistry must supply one identity-,
  purity-, permeability-, and cost-qualified cell-active probe. Erythroid
  biology must then run a dose-response comparison against vehicle, mutant
  control, and hydroxyurea in at least three genetically distinct
  beta-thalassemia donor cultures with HbF HPLC, F-cells, `HBG1/HBG2`, total
  hemoglobin, globin balance, viability, apoptosis, `CD71/CD235a`, enucleation,
  hemolysis, and off-target RNA sequencing.

## August 1 Resveratrol Decision

**Question:** Does the 2026 randomized Thailand ferritin result, read with the
earlier human resveratrol trial, justify keeping purified resveratrol in the
first affordable-cure HbF quote panel?

**Decision:**
`deprioritize_resveratrol_from_first_affordable_cure_hbf_panel_to_ntdt_iron_overload_comparator_only`.

The decision changes experimental priority, not the curative-route ranking.
Matched-sibling HSCT remains the leading affordable-curative route benchmark
only.

- **Fact:** EHA-3064 reports 30 randomized adults with NTDT on stable iron
  chelation: resveratrol `n=10`, omeprazole `n=11`, and placebo `n=9`. Median
  six-month serum-ferritin change was -116, -8, and +8 ng/mL, respectively.
  Resveratrol differed from omeprazole (`P=0.016`) and placebo (`P=0.012`).
- **Fact:** The conference abstract reports three adverse events in the
  resveratrol group. It does not report HbF, hemoglobin, transfusion
  burden, liver iron concentration, labile plasma iron, non-transferrin-bound
  iron, chelation changes, follow-up after withdrawal, or cost.
- **Fact:** ISRCTN `73258526` planned 60 participants and registered labile
  plasma iron, non-transferrin-bound iron, erythroferrone, hepcidin, and an HbF
  association as secondary measures. The registry remained recruiting or
  ongoing when checked and does not reconcile its target with the 30-person
  conference report.
- **Fact:** PMID `29926158` randomized 54 adults with NTDT to hydroxyurea,
  resveratrol plus piperine, or their combination. The abstract reports no
  significant response-rate difference. The 2023 Cochrane synthesis reports a
  hydroxyurea-versus-resveratrol hemoglobin mean difference of -0.30 g/dL,
  95% CI -1.14 to 0.54, in 34 participants, with low-certainty evidence. HbF
  was not reported for the comparison, and transfusion frequency or interval
  was not available.
- **Contradiction:** The 2018 human formulation included piperine and cannot
  validate purified resveratrol. The 2026 registry target and conference cohort
  also differ. Registered HbF and labile-iron measures remain unreported.
- **Hypothesis:** The ferritin signal is an iron-axis adjunct effect distinct
  from HbF induction. It becomes credible only if organ iron or registered
  labile-iron biomarkers improve with stable chelation and no worsening of
  hemoglobin or transfusion burden.
- **Interpretation:** Remove purified resveratrol from the active first HbF
  quote and retain it only as an NTDT iron-overload comparator pending complete
  randomized outcomes.
- **Open question:** Does the complete trial reconcile enrollment and show
  organ-iron or labile-iron benefit without anemia, transfusion, or safety
  tradeoffs?
- **Affordability and access:** No source reports itemized product, chelation,
  monitoring, adverse-event, or total delivered cost. Oral administration does
  not establish affordability, availability, or an Indonesia access path.
- **Falsification criterion:** Reconsider HbF-panel priority only if a complete
  controlled report shows reproducible HbF protein or F-cell improvement plus
  hemoglobin or transfusion benefit, acceptable safety, durability, and
  delivered cost. If the complete iron study does not reproduce ferritin with
  organ-iron or labile-iron improvement, deprioritize the iron-comparator lane.
- **Next decisive action:** Monitor the EHA report and ISRCTN record for the
  full cohort, registered biomarkers, HbF, hemoglobin, transfusion outcomes,
  chelation stability, complete adverse events, follow-up, and itemized cost.
  Do not spend first-quote capacity on resveratrol before that result.

## July 31 TTF Conditioning Decision

**Question:** Does a new 74-child treosulfan-thiotepa-fludarabine cohort support
promoting TTF as a reduced-toxicity affordable conditioning route across donor
types in TDT?

**Decision:**
`promote_ttf_to_matched_family_donor_conditioning_benchmark_only_pending_adjusted_comparison_safety_and_cost`.
Matched-sibling HSCT remains the leading affordable-curative route benchmark
only.

- **Fact:** PMID `42467967` reports a retrospective single-center cohort of 74
  children with TDT treated with TTF conditioning from January 2017 through May
  2025. Donors were 45 matched siblings, 4 other matched relatives, 16
  matched-unrelated donors, and 9 haploidentical donors.
- **Outcome:** At median follow-up of 45.2 months, five-year overall and
  thalassemia-free survival were 82.2% and 77.7%. In the combined
  matched-family group, the estimates were 95% and 88.3%. In the combined
  alternative-donor group, both were 57.3%.
- **Safety:** Four children had primary graft failure. Ten had mixed chimerism,
  including two with secondary graft failure. Acute GVHD occurred in 25,
  chronic GVHD in 7, CMV reactivation in 42, and veno-occlusive disease in 6.
- **Contradiction:** The abstract describes TTF as reduced toxicity and a
  promising busulfan alternative, but reports no concurrent busulfan comparator.
  It does not establish a causal toxicity advantage.
- **Evidence boundary:** The retrospective analysis combines donor types and
  does not expose adjusted donor-specific estimates in the accessible record.
  Its follow-up range begins at 1.5 months, while the five-year number at risk,
  death count and causes, GVHD grade, complete infection and hospitalization
  burden, late safety, and delivered cost are not reported in the abstract.
- **Interpretation:** Promote TTF to a matched-family donor conditioning
  benchmark only. The 57.3% alternative-donor estimates block donor-agnostic
  promotion and do not overturn F-BMT's separate conditioning-benchmark label.
- **Confidence:** Moderate that outcomes differ materially by the combined
  donor grouping under this program. Low that TTF is superior, less toxic, or
  affordable.
- **Affordability and access:** The article provides no itemized cost. Exact
  public BPOM product-name and ingredient searches for the three conditioning
  agents and named brands returned no record on July 31. This is an unresolved
  public-registry gap, not proof of authorization, procurement, unavailability,
  affordability, or suitability in Indonesia.
- **Hypothesis:** In an independently enrolled matched-family donor pediatric
  cohort, TTF can preserve five-year thalassemia-free survival within a
  preregistered non-inferiority margin while reducing a prespecified composite
  severe-toxicity endpoint relative to a contemporary busulfan-based protocol.
- **Open question:** Can donor-stratified comparison reproduce the
  matched-family outcome, explain the alternative-donor result, and show lower
  severe toxicity at an itemized Indonesia-relevant delivered cost?
- **Falsification criterion:** Remove the conditioning-benchmark promotion if
  independent evidence fails the five-year thalassemia-free-survival margin,
  does not reduce the severe-toxicity endpoint, confirms poor
  alternative-donor survival, or exceeds the program's delivered-cost threshold.
- **Next decisive action:** Obtain the full report and compare one
  donor-stratified TTF cohort with one contemporary busulfan-based cohort using
  five-year survival, number-at-risk, complete death, graft-failure, GVHD,
  infection, organ-toxicity, hospitalization, late-safety, and itemized-cost
  denominators.

## July 30 Thalidomide Response-Benchmark Decision

**Question:** Do two 2026 meta-analyses, a genotype-response cohort, and a new
case report support promoting thalidomide from a high-caution HbF comparator to
an affordable disease-modifying route?

**Decision:** `hold_thalidomide_at_high_caution_response_benchmark_only`.

- **Fact:** PMID `42136903` describes 26 studies with 2,422 people with TDT,
  including five randomized trials. One 99-person randomized trial supplied
  the response-rate comparison (`RR=6.95`, 95% CI `2.96-16.27`, low
  certainty). Five randomized trials supported a hemoglobin signal and three
  supported an HbF signal, both graded moderate certainty.
- **Primary evidence:** PMID `42333196` reports that 10 of 25 participants with
  TDT in a prospective single-center cohort were transfusion-independent after
  24 weeks. The study was not randomized and did not establish off-treatment
  or long-term durability.
- **Independent synthesis:** PMID `41933128` reviewed 19 studies with 1,731
  people with beta-thalassemia or HbE/beta-thalassemia across TDT and NTDT.
  Only two studies were randomized. TDT pooled single-arm response proportions
  were 0.76 for at least a 50% transfusion reduction and 0.55 for complete
  transfusion cessation, with high heterogeneity. These are not controlled or
  durable effects.
- **Genotype and phenotype scope:** PMID `42415097` associates `HBG2`
  `rs7482144`, `BCL11A` `rs766432`, and `HBS1L-MYB` `rs9399137` with excellent
  response in a three-month, uncontrolled, single-center cohort of 100 people
  with TDT in Karachi. It is an early unedited responder hypothesis, not a
  validated predictor or eligibility rule. PMID `42526830` is one pediatric
  NTDT case with autoimmune hemolytic anemia and no numeric abstract endpoint,
  follow-up, or safety denominator.
- **Safety:** Four randomized trials reported more adverse drug events with
  thalidomide (`RR=1.94`, 95% CI `1.64-2.29`). Seven thromboses across one
  randomized and four pre-post studies all led to discontinuation. The review
  states that adverse events were underreported in some studies.
- **Contradictions:** The review refers to both 26 and 21 included studies,
  defines major and overall response with the same formula despite reporting
  different pooled estimates, and identifies overlap among several follow-up
  cohorts. Its 2,422-person total is not a confirmed independent denominator.
- **Second-review conflict:** PMID `41933128` excludes two overlapping
  Chen-cohort papers but reports incompatible safety denominators of 1,124,
  1,670, and `n=1,620`. It describes adverse events as transient and reversible
  despite discontinuations after seizures and thrombotic or cerebrovascular
  events. It does not reconcile the broader review or establish long-term
  safety.
- **Regulatory boundary:** The current DailyMed label retains boxed warnings
  for embryo-fetal toxicity and venous thromboembolism and warns that
  peripheral neuropathy may be severe and irreversible. The label is not a
  thalassemia-specific incidence source.
- **Interpretation:** Thalidomide now has a distinct high-caution human response
  benchmark label. It should no longer be conflated with the melittin reject
  lane, but it does not become an affordable route, a cure, or a patient-facing
  candidate.
- **Affordability and access:** No reviewed source provides an itemized drug,
  monitoring, risk-control, or adverse-event cost or establishes Indonesia
  authorization, access, or a locally governed safety system.
- **Confidence:** Moderate that an on-treatment response signal exists. High
  that affordable-route promotion is unsupported.
- **Hypothesis:** A prospectively defined responder subgroup may sustain
  clinically meaningful transfusion reduction if controlled evidence
  independently validates `HBG2`, `BCL11A`, and `HBS1L-MYB` markers while
  separating genotype, baseline HbF, spleen status, dose, and co-interventions
  from response and completely captures serious safety events.
- **Open question:** Can an independent controlled cohort reproduce a
  standardized response for 12 to 24 months, test post-withdrawal durability,
  and deliver complete safety controls at an itemized Indonesia-relevant cost?
- **Falsification criterion:** Deprioritize the lane even as a response
  benchmark if independent controlled evidence does not reproduce hemoglobin,
  HbF, or transfusion benefit, or if serious adverse events and required risk
  controls make the delivered route infeasible.
- **Next decisive action:** A clinical-research owner and independent
  biostatistics/genomics owner should preregister one controlled multicenter TDT
  study with standardized response definitions, complete participant and
  safety denominators, 12- to 24-month and post-withdrawal follow-up,
  prespecified `HBG2`, `BCL11A`, and `HBS1L-MYB` validation, and itemized drug
  plus monitoring cost.

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
- [Current FDA CASGEVY label](https://www.fda.gov/media/174615/download)
- [Adult exa-cel TDT primary report, PMID 38657265](https://pubmed.ncbi.nlm.nih.gov/38657265/)
- [Adult exa-cel TDT full report, DOI 10.1056/NEJMoa2309673](https://doi.org/10.1056/NEJMoa2309673)
- [FDA Casgevy TDT approval-review archive](https://www.fda.gov/media/176033/download?attachment=)
- [FDA Casgevy TDT Summary Basis for Regulatory Action](https://www.fda.gov/media/175842/download)
- [Adult exa-cel TDT trial NCT03655678](https://clinicaltrials.gov/study/NCT03655678)
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
- [GATAD2A-CHD4 HbF preprint, PMID 42539289](https://pubmed.ncbi.nlm.nih.gov/42539289/)
- [GATAD2A-CHD4 open full text, PMC13419836](https://pmc.ncbi.nlm.nih.gov/articles/PMC13419836/)
- [CHD4 macrocycle preprint, PMID 42282813](https://pubmed.ncbi.nlm.nih.gov/42282813/)
- [CHD4 macrocycle open full text, PMC13252415](https://pmc.ncbi.nlm.nih.gov/articles/PMC13252415/)
- [GATAD2A-CHD4 evidence decision](../findings/2026-04-27-epigenetic-hbf-target-drilldown.md#gatad2a-chd4-interface-decision)
- [GATAD2A-CHD4 thalassemia trial query](https://clinicaltrials.gov/search?term=%28GATAD2A%20OR%20CHD4%20OR%20MBD2-NuRD%29%20AND%20%28thalassemia%20OR%20thalassaemia%20OR%20beta-thalassemia%29)
- [Resveratrol HbF and iron-overload evidence](../findings/2026-04-27-resveratrol-hbf-beta-thalassemia-seed.md)
- [Randomized NTDT trial, PMID 29926158](https://pubmed.ncbi.nlm.nih.gov/29926158/)
- [Cochrane HbF-inducer review, PMID 36637054](https://pubmed.ncbi.nlm.nih.gov/36637054/)
- [EHA-3064 conference abstract](https://library.ehaweb.org/eha/2026/eha-2026/4208939/)
- [ISRCTN73258526 registry record](https://doi.org/10.1186/ISRCTN73258526)
- [Thalidomide GRADE meta-analysis, PMID 42136903](https://pubmed.ncbi.nlm.nih.gov/42136903/)
- [Second thalidomide meta-analysis, PMID 41933128](https://pubmed.ncbi.nlm.nih.gov/41933128/)
- [Three-month genotype-response cohort, PMID 42415097](https://pubmed.ncbi.nlm.nih.gov/42415097/)
- [Pediatric NTDT case report, PMID 42526830](https://pubmed.ncbi.nlm.nih.gov/42526830/)
- [Matched-sibling LMIC transplant cohort, PMID 42469166](https://pubmed.ncbi.nlm.nih.gov/42469166/)
- [Matched-sibling LMIC transplant full text, DOI 10.1182/bloodadvances.2025019083](https://doi.org/10.1182/bloodadvances.2025019083)
- [APBMT 2024 abstract book, abstract A-198](https://bct.apbmt.org/wordpress/wp-content/uploads/Abstract-Book-2024.pdf)
- [APBMT 2023 abstract book, abstract 44](https://bct.apbmt.org/wordpress/wp-content/uploads/Abstract-Book-2023_final.pdf)
- [Tzu Chi pediatric blood-stem-cell transplant facility](https://tzuchihospital.co.id/facilities-and-services/hematopoietic-stem-cell-transplantation-center)
- [Tzu Chi Hospital HSCT cost article](https://tzuchihospital.co.id/article/transpalantasi-sumsum-tulang)
- [TTF pediatric TDT cohort, PMID 42467967](https://pubmed.ncbi.nlm.nih.gov/42467967/)
- [TTF cohort DOI 10.1097/MPH.0000000000003246](https://doi.org/10.1097/MPH.0000000000003246)
- [BPOM public product registry](https://cekbpom.pom.go.id/produk-obat)
- [Long-term HSCT meta-analysis, PMID 42520329](https://pubmed.ncbi.nlm.nih.gov/42520329/)
- [Long-term HSCT meta-analysis full text, DOI 10.1016/j.htct.2026.106490](https://www.htct.com.br/en-long-term-survival-rates-thalassemia-patients-articulo-S2531137926002373)
- [Pescara 39-year HSCT cohort, PMID 36002533](https://pubmed.ncbi.nlm.nih.gov/36002533/)
- [Pescara primary full text, PMC9400570](https://pmc.ncbi.nlm.nih.gov/articles/PMC9400570/)
- [Pre-HSCT TDT fertility cohort, PMID 42515819](https://pubmed.ncbi.nlm.nih.gov/42515819/)
- [Fertility cohort DOI 10.1093/humrep/deag117](https://doi.org/10.1093/humrep/deag117)
- [Long-term beti-cel primary paper, PMID 41525466](https://pubmed.ncbi.nlm.nih.gov/41525466/)
- [Long-term beti-cel full text, DOI 10.1182/blood.2025029196](https://doi.org/10.1182/blood.2025029196)
- [Long-term beti-cel study NCT02633943](https://clinicaltrials.gov/study/NCT02633943)
- [German real-world beti-cel study, PMID 39418614](https://pubmed.ncbi.nlm.nih.gov/39418614/)
- [German real-world beti-cel full text, PMCID PMC11732601](https://pmc.ncbi.nlm.nih.gov/articles/PMC11732601/)
- [Pooled beti-cel mobilization analysis, DOI 10.1016/j.jtct.2023.12.305](https://doi.org/10.1016/j.jtct.2023.12.305)
- [FDA beti-cel advisory presentation](https://www.fda.gov/media/159126/download)
- [United States commercial beti-cel abstract, DOI 10.1016/j.jtct.2025.01.386](https://doi.org/10.1016/j.jtct.2025.01.386)
- [FDA ZYNTEGLO product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [FDA ZYNTEGLO package insert](https://www.fda.gov/media/160991/download)
- [Pediatric exa-cel primary result, PMID 42274009](https://pubmed.ncbi.nlm.nih.gov/42274009/)
- [Pediatric exa-cel trial `NCT05356195`](https://clinicaltrials.gov/study/NCT05356195)
- [FDA July 1 pediatric supplemental approval](https://www.fda.gov/news-events/press-announcements/fda-approves-first-gene-therapy-young-children-sickle-cell-disease)
- [FDA July 1 Casgevy supplement approval letter](https://www.fda.gov/media/193444/download)
- [July 17 BPOM exact-term snapshot](../../../data/regulatory/bpom/2026-07-17-casgevy-product-search-refresh.json)
- [`CD117` epitope-shielded conditioning preprint, PMID 42465494](https://pubmed.ncbi.nlm.nih.gov/42465494/)
- [Peer-reviewed KIT epitope-editing study, PMID 42420446](https://pubmed.ncbi.nlm.nih.gov/42420446/)
- [Peer-reviewed KIT epitope-editing full text, DOI 10.1038/s41586-026-10737-8](https://doi.org/10.1038/s41586-026-10737-8)
- [Nature reporting summary](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10737-8/MediaObjects/41586_2026_10737_MOESM2_ESM.pdf)
- [Anti-KIT transplant study NCT05357482](https://clinicaltrials.gov/study/NCT05357482)
- [EHA/EBMT gene-therapy selection consensus, PMID 42463828](https://pubmed.ncbi.nlm.nih.gov/42463828/)
- [FT007 phase 2b registry record, NCT07680803](https://clinicaltrials.gov/study/NCT07680803)
- [FT007 record history, version 1](https://clinicaltrials.gov/study/NCT07680803?a=1&tab=history)
- [F-BMT haploidentical-HSCT cohort, PMID 42489576](https://pubmed.ncbi.nlm.nih.gov/42489576/)
- [F-BMT paper DOI 10.1002/1545-5017.70563](https://doi.org/10.1002/1545-5017.70563)
- [WHO ICTRP mirror for ChiCTR2300071890](https://trialsearch.who.int/Trial2.aspx?TrialID=ChiCTR2300071890)
- [Multicenter allo-HSCT comparator, PMID 41730859](https://pubmed.ncbi.nlm.nih.gov/41730859/)
- [Quran 13:17 benefit-versus-foam anchor](../../islamic/quran/013-ar-rad/017.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
