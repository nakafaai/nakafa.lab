# Erythroid Metabolism Endpoint Addendum

Date checked: 2026-06-14
Status: optional quote endpoint addendum, not treatment advice

## Direct Answer

Erythroid metabolism is worth tracking, but it should stay optional in the first
quote. It can add mechanism context for red-cell survival hypotheses only after
the core HbF plus safety package remains intact.

Current operational label:

`case001_metabolism_endpoint_optional_addendum_ready`

## Rule

Do not add metabolism endpoints if they replace core endpoints or make the quote
harder to interpret.

Core endpoints stay first:

- HbF or `HBG`;
- erythroid maturation;
- viability or apoptosis;
- alpha-globin burden or autophagy;
- hemolysis or membrane safety.

Optional metabolism add-ons may be useful only when the lab can report them as
public-safe labels with low marginal cost and no treatment, trial, purchase,
import, or procurement language.

## Optional Add-On Labels

| Label | Meaning |
| --- | --- |
| `metabolism_addon_optional` | ATP, glycolysis, oxidative-stress, or pyruvate-kinase context is cheap, labelable, and additive. |
| `metabolism_addon_hold` | The add-on may be useful, but raw data, marginal cost, timeline, model fit, or endpoint definition is unclear. |
| `metabolism_addon_reject` | The add-on replaces core endpoints or shifts into treatment/procurement language. |
| `core_gate_first` | The core quote gate is not ready enough to discuss metabolism add-ons. |

## Source Read

The June 14 PubMed refresh found current pyruvate-kinase activation and
erythroid-metabolism context, including a June 9, 2026 review record. This
supports metabolism as benchmark context for red-cell survival, not as a reason
to loosen the HbF, maturation, viability, alpha-globin/autophagy, and hemolysis
requirements.

## Biomedical Boundary

This addendum does not recommend mitapivat, pyruvate-kinase activators, AMPK
activation, supplements, dosing, transfusion changes, chelation changes, trial
screening, purchase, import, or procurement. It only defines optional
preclinical endpoint labels.

## Islamic Motivation Boundary

Quran 55:7-9 supports measured claims and avoiding exaggeration. Here that
means metabolism endpoints must be measured and balanced against safety and
core endpoint completeness. It is not biomedical evidence for any intervention.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-14-erythroid-metabolism-endpoint-addendum.json)
- [June 14 PubMed compact snapshot](../../../data/literature/pubmed/2026-06-14-erythroid-metabolism-endpoint-refresh.json)
- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [AMPKB1 autophagy HbF bridge](../findings/2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [First quote request table](2026-06-02-first-quote-request-table.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [PubMed PMID `42261266`](https://pubmed.ncbi.nlm.nih.gov/42261266/)
- [PubMed PMID `41184165`](https://pubmed.ncbi.nlm.nih.gov/41184165/)
- [PubMed PMID `41833294`](https://pubmed.ncbi.nlm.nih.gov/41833294/)
