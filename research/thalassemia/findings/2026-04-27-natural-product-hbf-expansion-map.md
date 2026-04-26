# Finding: Natural-Product HbF Expansion Map

Date checked: 2026-04-27
Evidence label: early HbF lead expansion, not treatment advice

## Working Conclusion

The curcuminoid trienone lane led to two adjacent natural-product HbF leads:

- `Curcuma comosa` labdane diterpenes, with a PubMed-indexed K562 reporter
  study;
- quercetin analogs, with DOI and publisher metadata but no clean PubMed hit in
  the first-pass query.

These are not cure claims. They are seed records for the HbF discovery funnel.
`T-BDMC` remains the stronger current natural-product-adjacent seed because it
has beta-thalassemia/HbE primary erythroid validation in addition to K562 data.

## Lead 1: Curcuma comosa Labdane Diterpenes

The PubMed-indexed article reports three new labdane diterpenes,
`curcucomosins A-C`, four known labdane diterpenes, and one known
diarylheptanoid from aerial parts of `Curcuma comosa`.

The assay used a K562 reporter cell line with EGFP under the control of the
`G gamma-globin` promoter. The strongest reported signal was compound `6`,
`isocoronarin D`, with `1.6-fold` HbF induction at `20 microM`.

Interpretation:

- this is direct HbF-adjacent evidence;
- the model is still K562 only in the currently retrieved abstract;
- there is no retrieved beta-thalassemia patient-cell validation yet;
- compound identity needs PubChem/ChEMBL/supplier or synthesis resolution before
  assay planning.

## Lead 2: Quercetin Analogs

Crossref and the publisher DOI resolve the article:
`Quercetin analogs with high fetal hemoglobin-inducing activity`.

The first-pass PubMed exact-title query returned zero records. A broader PubMed
query returned an unrelated `Hippophae rhamnoides` radiation-protection paper,
so that broad query is recorded as noisy and should not be used as evidence for
quercetin analog HbF activity.

Interpretation:

- the DOI-confirmed article is worth extracting because the title directly
  mentions fetal hemoglobin induction;
- until compound identities, model system, effect size, and toxicity readouts
  are extracted, this lane stays below `T-BDMC`;
- this should be kept separate from ordinary quercetin supplement claims.

## Research Decision

Current priority order inside the natural-product HbF lane:

| Priority | Candidate | Reason | Gate before promotion |
| --- | --- | --- | --- |
| 1 | `T-BDMC` trienone analog | K562 plus beta-thalassemia/HbE primary-cell bridge | clean structure/supplier/synthesis record |
| 2 | `isocoronarin D` / `Curcuma comosa` labdane diterpenes | direct K562 `G gamma-globin` reporter signal | compound identity, hemolysis, and disease-cell validation |
| 3 | quercetin analogs | DOI-confirmed HbF-inducing title | full extraction of compounds, assays, effect size, and safety |

## Assay Gate

Do not promote either new lead to therapy hypothesis without:

- exact compound identity or standardized fraction marker;
- red-cell hemolysis screen;
- K562 repeat only as a first screen, not as final proof;
- HUDEP-2 or primary erythroid maturation validation;
- beta-thalassemia/HbE primary-cell validation when accessible;
- HbF protein, F-cell percentage, `HBG1/HBG2`, globin-chain balance, and
  erythroid maturation endpoints;
- toxicity and bioavailability review.

## Sources

- [Labdane diterpenes PubMed search snapshot](../../../data/literature/pubmed/2026-04-27-labdane-diterpenes-hbf.json)
- [Labdane diterpenes PubMed ESummary](../../../data/literature/pubmed/2026-04-27-labdane-diterpenes-hbf-esummary.json)
- [Labdane diterpenes PubMed abstract XML](../../../data/literature/pubmed/2026-04-27-labdane-diterpenes-hbf-abstract.xml)
- [Labdane diterpenes Crossref snapshot](../../../data/literature/pubmed/2026-04-27-labdane-diterpenes-hbf-crossref.json)
- [Curcuma comosa thalassemia/HbF query snapshot](../../../data/literature/pubmed/2026-04-27-curcuma-comosa-hbf-thalassemia.json)
- [Quercetin analogs Crossref snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-analogs-hbf-crossref.json)
- [Quercetin analogs exact-title PubMed snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-analogs-hbf-title.json)
- [Quercetin analogs broad PubMed noisy snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-analogs-hbf.json)
- [Curcuminoid analog assay map](2026-04-27-curcuminoid-analog-assay-map.md)
