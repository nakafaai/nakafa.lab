# Finding: Hepcidin-Ferroportin Iron-Restriction Axis

Date checked: 2026-04-27
Last evidence update: 2026-07-15
Evidence label: disease-modifying iron-axis lane, not cure and not patient advice

## Working Conclusion

The hepcidin-ferroportin-TMPRSS6 axis is a credible disease-modifying research
lane for beta-thalassemia because it targets iron traffic and ineffective
erythropoiesis, not only downstream antioxidant stress.

It is not the same as HbF reactivation. It does not repair `HBB`, replace stem
cells, or directly make fetal hemoglobin. Its goal is narrower: reduce
pathologic iron availability, iron absorption, transferrin saturation, and
iron-driven erythroid damage so red-cell production may become less ineffective.

This lane is strongest as a comparator and adjunct strategy. For
transfusion-dependent thalassemia (`TDT`), it cannot be assumed to remove the
need for transfusion because transfusional iron loading remains central. For
non-transfusion-dependent beta-thalassemia (`NTDT`), the fit is more direct
because ineffective erythropoiesis suppresses hepcidin and drives intestinal
iron absorption.

The 2026 sapablursen result narrows this conclusion. `TMPRSS6` inhibition is
not one interchangeable class: sapablursen monotherapy failed its hemoglobin
and liver-iron endpoints in `NTDT` and is now deprioritized. Other iron-axis
modalities remain comparators until they show human thalassemia efficacy.

## Mechanism Map

| Node | Disease role | Research implication |
| --- | --- | --- |
| `ERFE` / erythroferrone | high erythroid stress can suppress hepcidin | biomarker and possible upstream target |
| hepcidin | low relative to iron burden in thalassemia biology | raising hepcidin can restrict iron entry to plasma |
| ferroportin | exports iron from enterocytes and macrophages | inhibition can reduce serum iron and transferrin saturation |
| `TMPRSS6` / matriptase-2 | suppresses hepcidin signaling through `HJV` cleavage | inhibition can increase endogenous hepcidin |
| minihepcidin / hepcidin agonism | mimics hepcidin-like iron restriction | useful preclinical probe, not a current cure |

## Evidence Snapshot

| Intervention class | Retrieved evidence | Boundary |
| --- | --- | --- |
| Ferroportin inhibition / vamifeport | preclinical beta-thalassemia model evidence; 2025 randomized phase 2a `NTDT` safety and pharmacodynamic study | disease-modifying signal, not transfusion-independence proof |
| `TMPRSS6` inhibition / sapablursen | 2026 open-label phase 2a result in 29 adults with `NTDT`; hemoglobin and liver-iron endpoints failed and serum hepcidin did not increase consistently | deprioritized monotherapy; result does not falsify every `TMPRSS6` or iron-axis modality |
| `TMPRSS6` inhibition / SLN124 | mouse beta-thalassemia plus deferiprone evidence; healthy-volunteer phase 1 hepcidin and plasma-iron pharmacodynamics | thalassemia patient translation remains early |
| `TMPRSS6` inhibition / REGN7999 | 2025 mouse beta-thalassemia and healthy-human iron-reduction report; recruiting `NTDT` iron-overload trial | early clinical lane, not approved thalassemia therapy |
| Hepcidin agonism / minihepcidin | mouse adult beta-thalassemia major model improved ineffective erythropoiesis and splenomegaly | preclinical tool, not a patient protocol |
| Erythroferrone biology | mouse beta-thalassemia work links `ERFE` to hepcidin suppression and iron overload | target/biomarker lane, not a retail supplement lane |

## Clinical-Trial Readout

The ClinicalTrials.gov hepcidin-axis snapshot returned eight thalassemia or
iron-overload-adjacent records:

- `NCT04364269`: completed phase 2 VIT-2763 / vamifeport beta-thalassemia study.
- `NCT04938635`: withdrawn phase 2 VIT-2763 study in adult `TDT`.
- `NCT04718844`: completed phase 1 SLN124 study in adults with alpha or
  beta-thalassemia and low-risk `MDS`.
- `NCT04176653`: withdrawn SLN124 beta-thalassemia or `MDS` study.
- `NCT04059406`: terminated sapablursen / IONIS-TMPRSS6-LRx study.
- `NCT06421636`: recruiting REGN7999 phase 2 `NTDT` iron-overload study using
  MRI iron endpoints.
- `NCT03381833`: terminated LJPC-401 myocardial-iron-overload `TDT` study.
- `NCT03165864`: completed healthy-volunteer IONIS TMPRSS6-LRx phase 1 study.

The pattern is important: the biology is strong enough for clinical programs,
but the trial landscape is mixed, early, and not yet a cure claim.

## July 15 Sapablursen Result

**Question:** Does the published phase 2a result justify retaining sapablursen
as an active affordable route toward durable transfusion independence?

**Decision:** `deprioritize_sapablursen_monotherapy`. Keep the broader
hepcidin-ferroportin axis as `comparator_only`.

- **Fact:** The industry-sponsored study enrolled 29 adults with genotypically
  confirmed `NTDT` into three open-label active-dose cohorts. Sapablursen was
  given subcutaneously every four weeks at initial doses of 30, 50, or 80 mg,
  later increased to as much as 160 mg. There was no placebo cohort.
- **Fact:** The study did not meet its primary hemoglobin endpoint at week 27
  or its secondary hemoglobin and liver iron concentration endpoints at week
  53. The publication reports no consistent dose-dependent serum-hepcidin
  increase. The registry says development in this population stopped because
  efficacy did not meet the sponsor's minimum target product profile.
- **Safety boundary:** The paper describes generally favorable tolerability,
  and the registry reports no deaths. Three participants had serious adverse
  events across the dose cohorts, but the registry display does not establish
  that those events were caused by sapablursen. The small, uncontrolled design
  cannot establish comparative safety.
- **Contradiction:** Earlier mouse studies and studies in healthy volunteers or
  polycythemia vera supported hepcidin induction. That pharmacodynamic effect
  did not translate consistently in this `NTDT` cohort.
- **Hypothesis:** In the companion mouse study, high `ERFE` or
  severe iron loading blunted the hepcidin, erythroid, and iron response to a
  `Tmprss6` antisense oligonucleotide despite similar target reduction. This
  makes disease-state resistance plausible; it does not prove that baseline
  `ERFE` or liver iron concentration predicts human response.
- **Interpretation:** The human endpoint failure is enough to deprioritize
  sapablursen monotherapy, while the model-only resistance explanation is not
  enough to reject every `TMPRSS6` or iron-axis modality.
- **Confidence:** High that sapablursen missed the prespecified clinical
  endpoints in this small `NTDT` study; moderate that `ERFE` and iron loading
  explain the failure; low for extrapolation to other modalities, `TDT`, or
  durable transfusion independence.
- **Affordability and access:** Repeated injectable antisense therapy plus
  hepcidin, iron, anemia, and MRI monitoring is not a low-infrastructure cure
  path. With no demonstrated clinical benefit in this study, there is no
  evidence-backed affordability case for sapablursen in thalassemia.
- **Falsification criterion:** Restore a `TMPRSS6` modality only if a human
  thalassemia study shows target engagement plus prespecified hepcidin or iron
  improvement and hemoglobin or transfusion benefit, with resistance assessed
  against baseline `ERFE` and iron burden. Promotion into the cure lane would
  additionally require durable transfusion independence and a documented total
  delivered-cost path.
- **Open question:** Can another modality overcome high-`ERFE` or high-iron
  resistance and produce both pharmacodynamic and clinical benefit in human
  thalassemia?
- **Next decisive action:** Do not allocate Nakafa assay or outreach effort to
  sapablursen-specific work. Reassess the broader lane only when another
  modality reports human thalassemia outcomes with both pharmacodynamic and
  clinical endpoints.

## Assay And Endpoint Gates

Any candidate in this lane should be judged against iron-homeostasis and
erythroid endpoints:

- serum ferritin, transferrin saturation, serum iron, `NTBI`, and labile plasma
  iron where available;
- liver iron concentration by MRI, and cardiac `T2*` when clinically relevant;
- hepcidin, `ERFE`, reticulocytes, erythroid maturation, spleen size, and
  hemolysis markers;
- hemoglobin, transfusion burden, interval between transfusions, and chelation
  burden;
- liver, kidney, infection, anemia-worsening, and drug-interaction safety.

This is not a supplement pathway. Iron restriction can help only when the
patient's iron physiology and anemia severity make it safe under clinical
supervision.

## Fit With Quran 57:25

Quran 57:25 mentions iron as having great might and benefits for humanity. For
Nakafa Lab, the scientific lesson is not "give iron." The lesson is balance:
iron is powerful and beneficial, but in thalassemia excess iron is also a major
source of organ injury.

Therefore, Al-Hadid is documented here as an ethical and conceptual guardrail:
study iron seriously, measure it carefully, and never convert a Quranic mention
of iron into an iron-supplement claim for patients with iron overload.

## Research Decision

Promote the hepcidin-ferroportin-TMPRSS6 axis into the active disease-modifying
map as an `iron-restriction comparator`:

- below cure-oriented HSCT, gene addition, gene editing, and direct HbF
  reactivation lanes;
- above generic antioxidant claims because it has a strong causal iron-biology
  model and named clinical-stage interventions;
- useful for `NTDT` iron-overload hypotheses and for `TDT` adjunct comparison;
- sapablursen monotherapy is `deprioritized` after endpoint failure and lack of
  consistent hepcidin induction in the 2026 phase 2a result;
- mandatory hematologist review before any patient-facing interpretation.

## Sources

- [Hepcidin/ferroportin beta-thalassemia PubMed search](../../../data/literature/pubmed/2026-04-27-hepcidin-ferroportin-beta-thalassemia-search.json)
- [Selected hepcidin-axis PubMed abstracts](../../../data/literature/pubmed/2026-04-27-hepcidin-axis-selected-abstracts.xml)
- [Vamifeport beta-thalassemia PubMed search](../../../data/literature/pubmed/2026-04-27-vamifeport-beta-thalassemia-search.json)
- [SLN124/TMPRSS6 beta-thalassemia PubMed search](../../../data/literature/pubmed/2026-04-27-sln124-tmprss6-beta-thalassemia-search.json)
- [Minihepcidin beta-thalassemia PubMed search](../../../data/literature/pubmed/2026-04-27-minihepcidin-beta-thalassemia-search.json)
- [Minihepcidin TDT-major mouse-model PubMed search](../../../data/literature/pubmed/2026-04-27-minihepcidin-tdt-major-search.json)
- [Erythroferrone beta-thalassemia hepcidin search](../../../data/literature/pubmed/2026-04-27-erythroferrone-beta-thalassemia-hepcidin-search.json)
- [REGN7999/TMPRSS6 beta-thalassemia PubMed search](../../../data/literature/pubmed/2026-04-27-regn7999-tmprss6-beta-thalassemia-search.json)
- [Hepcidin-axis ClinicalTrials.gov snapshot](../../../data/registries/clinicaltrials/2026-04-27-hepcidin-axis-thalassemia-trials.json)
- [Sapablursen phase 2a result, PMID 42241700](https://pubmed.ncbi.nlm.nih.gov/42241700/)
- [Sapablursen trial `NCT04059406`](https://clinicaltrials.gov/study/NCT04059406)
- [`Tmprss6` resistance study, PMID 41954608](https://pubmed.ncbi.nlm.nih.gov/41954608/)
- [Vamifeport ChEMBL search](../../../data/chemistry/chembl/iron-axis/2026-04-27-vamifeport-search.json)
- [Vamifeport PubChem properties](../../../data/chemistry/pubchem/iron-axis/2026-04-27-vamifeport-properties.json)
- [Rusfertide ChEMBL search](../../../data/chemistry/chembl/iron-axis/2026-04-27-rusfertide-search.json)
- [Rusfertide PubChem properties](../../../data/chemistry/pubchem/iron-axis/2026-04-27-rusfertide-properties.json)
- [Quran 57:25](https://quran.com/57/25)
- [Quran 57:25 structured note](../../islamic/quran/057-al-hadid/025.md)
