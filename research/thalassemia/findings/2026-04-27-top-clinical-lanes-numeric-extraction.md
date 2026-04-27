# Finding: Top Clinical Lanes Numeric Extraction

Date checked: 2026-04-27
Scope: clinical benchmark extraction, not treatment advice

## Working Conclusion

The strongest cure-like endpoint is still stem-cell intervention: lentiviral
gene addition or CRISPR HbF reactivation can make many selected TDT patients
transfusion-independent. The practical Nakafa Lab problem is access, risk, and
cost.

For lower-cost discovery, hydroxyurea remains the first comparator because it
has human thalassemia evidence and realistic access. Luspatercept and mitapivat
are important disease-modifying benchmarks. Thalidomide and sirolimus are useful
mechanism comparators but have safety or evidence-size limits.

## Numeric Benchmarks

| Lane | Source signal | Numeric extraction | Current interpretation |
| --- | --- | --- | --- |
| Exa-cel / CRISPR HbF reactivation | Phase 3 TDT study | transfusion independence in 32/35 evaluable patients, 91%; mean total Hb 13.1 g/dL; mean HbF 11.9 g/dL | strongest HbF cure-like proof, high access and conditioning barrier |
| Beti-cel / lentiviral gene addition | Phase 3 non-beta0/beta0 TDT study | transfusion independence in 20/22 evaluable patients, 91%; average Hb 11.7 g/dL during independence | strongest beta-globin addition proof, high access and conditioning barrier |
| Luspatercept | BELIEVE phase 3 TDT trial | primary endpoint 21.4% vs 4.5%; any 12-week 33% transfusion-burden reduction 70.5% vs 29.5%; at least 50% reduction 40.2% vs 6.3% | disease-modifying benchmark, not a cure |
| Mitapivat | FDA summary plus ENERGIZE phase 3 NTDT abstract | TDT transfusion reduction response 30% vs 13%; NTDT Hb response 42% vs 2%; FACIT-Fatigue mean change 4.9 vs 1.5 | oral disease-modifying benchmark; liver-toxicity REMS matters |
| Hydroxyurea | TDT meta-analysis | five studies, 294 patients; transfusion interval MD 10.07 days; Hb MD 1.71; ferritin MD -299.65 | best low-cost HbF comparator, response heterogeneous |
| Sirolimus | Sirthalaclin pilot | eight patients; 1 mg/day for 24-48 weeks; transfusion demand index decreased in 7/8 | mechanism-strengthening signal, small cohort and immune-monitoring limits |
| Thalidomide | phase 2 randomized TDT trial | 100 patients; Hb median increase 14.0 g/L; 12-week RBC volume 5.4 +/- 5.0 U vs 10.3 +/- 6.4 U | strong effect signal but severe safety barrier |

## Implication For Discovery

Any affordable candidate should be compared against at least one benchmark:

- HbF correction benchmark: exa-cel;
- beta-globin addition benchmark: beti-cel;
- transfusion-burden benchmark: luspatercept;
- oral disease-modifying benchmark: mitapivat;
- low-cost HbF benchmark: hydroxyurea;
- high-caution HbF/responder benchmark: thalidomide;
- small-cohort repurposing benchmark: sirolimus.

This makes the project harder but cleaner. A candidate cannot be promoted just
because it is natural, affordable, or mechanistically interesting. It must
explain which benchmark it is trying to approach and which endpoint it can
actually measure.

## Open Extraction Gaps

- Hydroxyurea needs subgroup extraction by `TDT`, `NTDT`, HbE/beta-thalassemia,
  baseline HbF, XmnI, and spleen status.
- Luspatercept and mitapivat need local access and cost mapping for Indonesia.
- Sirolimus needs full-text numeric extraction beyond the abstract.
- Thalidomide needs genotype-response and adverse-event frequency extraction.
- Gene therapy needs cost, conditioning, fertility, and long-term follow-up
  extraction.

## Sources

- [Top clinical lane PubMed XML snapshot](../../../data/literature/pubmed/2026-04-27-top-clinical-lanes-abstracts.xml)
- [Beti-cel PubMed XML snapshot](../../../data/literature/pubmed/2026-04-27-beti-cel-abstract.xml)
- [FDA Aqvesme mitapivat approval](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [FDA Reblozyl luspatercept approval](https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-luspatercept-aamt-anemia-patients-beta-thalassemia)
- [FDA Casgevy product page](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo product page](https://www.fda.gov/vaccines-blood-biologics/zynteglo)

## Linked Repo Notes

- [Candidate scoring V0](../prioritization/2026-04-27-candidate-scoring-v0.md)
- [Candidate ranking](../prioritization/2026-04-26-candidate-ranking.md)
- [Gene therapy access frontier](2026-04-27-gene-therapy-access-frontier.md)
- [Luspatercept transfusion-burden benchmark](2026-04-27-luspatercept-transfusion-burden-benchmark.md)
- [Hydroxyurea deep dive](2026-04-26-hydroxyurea-deep-dive.md)
- [Sirolimus deep dive](2026-04-26-sirolimus-deep-dive.md)
- [Thalidomide-class deep dive](2026-04-26-thalidomide-class-deep-dive.md)
