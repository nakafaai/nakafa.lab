# Finding: Hydroxyurea Response Predictor Map

Date checked: 2026-04-27
Scope: responder biology, not treatment advice

## Working Conclusion

Hydroxyurea is useful as the first affordability comparator, but response is not
uniform. The current predictor map points to three practical gates:

1. exact thalassemia subtype, especially `NTDT` versus `TDT` and HbE/beta;
2. fetal-hemoglobin modifier context, especially XmnI-HBG2 where available;
3. functional erythroid response, ideally measured before claiming a candidate
   will work.

This matters because a low-cost candidate should not be compared against
"hydroxyurea in general." It should be compared against hydroxyurea in the same
subtype and responder context.

## Extracted Evidence

| Evidence source | Numeric signal | Predictor implication |
| --- | --- | --- |
| NTDT meta-analysis | 17 studies, 709 patients; severe NTDT complete response 42%, overall response at least 50% in 79% | hydroxyurea signal is stronger in some NTDT contexts than a generic TDT framing |
| HbE/beta-thalassemia XmnI study | 49 transfusion-dependent HbE/beta patients; 30 responders, 61.22%; XmnI genotype correlated with transfusion-free interval, p < 0.001 | XmnI-HBG2 can be a practical response-stratification marker |
| Beta-thalassemia/HbE erythroid culture | 18 patients; 30 micromolar hydroxyurea for 96 hours; HbF proportion increased at least 30% in 4 cultures, 20-30% in 9, less than 20% in 5, less than 3% in 2 | ex-vivo erythroid response can separate stronger and weaker responders |
| TDT meta-analysis | five studies, 294 patients; transfusion interval MD 10.07 days; Hb MD 1.71; ferritin MD -299.65 | TDT effect exists but still needs genotype and response subgroup extraction |

The NTDT PubMed abstract reports hemoglobin increase as `1g/L`; that unit should
be verified against the full text before quantitative reuse.

## Case-001 Data Needed

To know whether this lane is even a useful comparator for case-001, collect or
ask the hematologist about:

- exact diagnosis: `TDT`, `NTDT`, HbE/beta-thalassemia, alpha-thalassemia, or
  mixed disease;
- HPLC/electrophoresis: HbA, HbA2, HbF, HbE;
- `HBB` and `HBA` genotype;
- XmnI-HBG2, `BCL11A`, and `HBS1L-MYB` modifier status if available;
- spleen status and hypersplenism markers;
- baseline transfusion interval and pre-transfusion hemoglobin;
- whether previous hydroxyurea exposure occurred and why it was stopped or
  continued.

## Research Implication

The next computational object should be a responder-signature table. It should
not predict treatment for a patient. It should rank which variables are required
before hydroxyurea-like, HbF-like, or natural-product-adjacent candidates can be
interpreted.

For example, a candidate that looks weak in generic beta-thalassemia might still
be relevant in HbE/beta-thalassemia with favorable HbF modifiers. The reverse is
also possible.

## Boundaries

- This does not recommend hydroxyurea use.
- Hydroxyurea has marrow-suppression, infection, fertility, pregnancy, liver,
  kidney, and interaction considerations.
- Any decision belongs to a licensed hematologist.

## Sources

- [Hydroxyurea response predictor PubMed XML](../../../data/literature/pubmed/2026-04-27-hydroxyurea-response-predictors.xml)
- [Hydroxyurea deep dive](2026-04-26-hydroxyurea-deep-dive.md)
- [Indonesia genotype-first rule](2026-04-27-indonesia-genotype-first-rule.md)
- [Top clinical lanes numeric extraction](2026-04-27-top-clinical-lanes-numeric-extraction.md)
