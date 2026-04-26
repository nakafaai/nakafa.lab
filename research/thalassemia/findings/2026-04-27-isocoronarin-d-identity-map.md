# Finding: Isocoronarin D Identity Map

Date checked: 2026-04-27
Evidence label: chemistry identity and K562 activity map, not treatment advice

## Working Conclusion

`Isocoronarin D` is now a chemistry-resolved, low-priority HbF seed.

It has a clean ChEMBL molecule record, PubChem name matches, and ChEMBL activity
records that mirror the PubMed abstract-level K562 reporter signal. This makes
it easier to track chemically than the publication-defined `T-BDMC` trienone
analog, but the biological evidence is still weaker because the current
retrieved evidence does not include beta-thalassemia/HbE primary-cell
validation.

## Identity Resolution

| Compound | ChEMBL | PubChem | Key note |
| --- | --- | --- | --- |
| `isocoronarin D` | `CHEMBL1099267` | PubChem name query returns multiple stereochemical records; `CID 46871816` matches the ChEMBL InChIKey | strongest `Curcuma comosa` HbF signal retrieved so far |
| `curcucomosin A` | `CHEMBL1095928` | `CID 46209660` | weak K562 fold-change in ChEMBL activity record |
| `curcucomosin B` | `CHEMBL1098930` | `CID 46209661` | weak K562 fold-change in ChEMBL activity record |
| `curcucomosin C` | `CHEMBL1095927` | `CID 16081507` | modest K562 fold-change plus unrelated RAW264.7 inflammatory activity records |

ChEMBL records mark these compounds as natural products and not approved
therapeutics.

## Activity Snapshot

| Compound | Retrieved HbF activity | Viability/cytotoxicity context |
| --- | --- | --- |
| `isocoronarin D` | `FC 1.6` in K562 gamma-globin promoter reporter at `20 uM` after 5 days | K562 viability `80.7%` at `20 uM` |
| `curcucomosin A` | `FC 1.0` in K562 reporter at `5 uM` after 5 days | K562 viability `85.8%` at `5 uM` |
| `curcucomosin B` | `FC 1.0` in K562 reporter at `5 uM` after 5 days | K562 viability `87.7%` at `5 uM` |
| `curcucomosin C` | `FC 1.2` in K562 reporter at `30 uM` after 5 days | K562 viability `75.8%` at `30 uM` |

This supports keeping `isocoronarin D` as the only current `Curcuma comosa`
lead worth following deeply.

## Research Decision

Promote `isocoronarin D` from "source-level lead" to
"chemistry-resolved low-priority HbF seed".

Do not promote it to a treatment hypothesis yet. The next gates are:

- obtain or synthesize the exact stereochemical compound matching
  `CHEMBL1099267` / PubChem `CID 46871816`;
- run red-cell hemolysis before broader erythroid interpretation;
- repeat K562 HbF reporter and endogenous HbF assays;
- test HUDEP-2 or primary erythroid maturation models;
- test beta-thalassemia/HbE primary erythroid cells when available;
- compare against hydroxyurea, decitabine, `T-BDMC`, and vehicle controls.

## Sources

- [Isocoronarin D PubChem snapshot](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-isocoronarin-d-properties.json)
- [Isocoronarin D ChEMBL search snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-isocoronarin-d-search.json)
- [Isocoronarin D ChEMBL molecule snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-isocoronarin-d-chembl1099267.json)
- [Isocoronarin D ChEMBL activity snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-isocoronarin-d-chembl-activities.json)
- [Curcucomosin A PubChem snapshot](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-curcucomosin-a-properties.json)
- [Curcucomosin B PubChem snapshot](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-curcucomosin-b-properties.json)
- [Curcucomosin C PubChem snapshot](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-curcucomosin-c-properties.json)
- [Curcucomosin A ChEMBL molecule snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-a-chembl1095928.json)
- [Curcucomosin A ChEMBL activity snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-a-chembl-activities.json)
- [Curcucomosin B ChEMBL molecule snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-b-chembl1098930.json)
- [Curcucomosin B ChEMBL activity snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-b-chembl-activities.json)
- [Curcucomosin C ChEMBL molecule snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-c-chembl1095927.json)
- [Curcucomosin C ChEMBL activity snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-c-chembl-activities.json)
- [Curcucomosin ChEMBL search snapshot](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-curcucomosin-a-search.json)
- [Natural-product HbF expansion map](2026-04-27-natural-product-hbf-expansion-map.md)
