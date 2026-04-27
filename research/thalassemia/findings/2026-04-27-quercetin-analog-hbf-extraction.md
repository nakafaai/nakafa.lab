# Finding: Quercetin Analog HbF Extraction

Date checked: 2026-04-27
Evidence label: publisher-abstract extraction and chemistry identity, not treatment advice

## Working Conclusion

The quercetin analog paper is no longer only a DOI/title lead. The Springer
publisher page exposes an abstract-level signal: `3,4'-Di-O-methylquercetin`
(`compound 7`) induced gamma-globin reporter expression with `2.6-fold` change
at `8 uM` in K562 reporter cells.

This upgrades the lane to "chemistry-resolved lower-priority HbF seed", but it
still remains below `T-BDMC` because no beta-thalassemia/HbE primary-cell
validation has been retrieved.

## Extracted Biology

The publisher abstract reports:

- quercetin parent compound `1` was isolated from the heartwoods of
  `Anaxagorea luzonensis`;
- fourteen methyl ether analogs, `2-15`, were chemically prepared;
- parent quercetin induced less gamma-globin expression than cisplatin and
  hemin positive controls;
- `3,4'-Di-O-methylquercetin` (`compound 7`) produced the strongest described
  signal, `2.6-fold` at `8 uM`;
- the reporter model was `K562::Delta G gamma-A gamma EGFP`;
- the abstract-level SAR says methoxy groups at `3` and `4'`, plus a free
  hydroxyl at `7`, are required for stronger HbF-inducing activity.

This is direct HbF-adjacent evidence, but still K562 reporter evidence.

## Chemistry Resolution

| Compound | PubChem | ChEMBL | Note |
| --- | --- | --- | --- |
| quercetin parent | `CID 5280343` | `CHEMBL50` | parent comparator; also tracked in the bee-constituent panel |
| `3,4'-Di-O-methylquercetin` / quercetin `3,4'-dimethyl ether` | `CID 5380905` | `CHEMBL309263` by InChIKey search | compound 7 seed from the publisher abstract |

The exact title query did not resolve in PubMed, and the ChEMBL document query
for DOI `10.1007/s00044-019-02412-7` returned zero documents. Therefore, the
HbF activity should be attributed to the Springer publisher abstract snapshot,
not to ChEMBL activity records.

ChEMBL activity records for `CHEMBL309263` exist, but the first-page activities
are unrelated cancer/tubulin/TRAIL/PTP-sigma records, not HbF records. Those
records are kept only to avoid falsely claiming ChEMBL HbF support.

ChEMBL text searches for the analog name and the `3-O-methyltamarixetin`
synonym were noisy. The clean ChEMBL identity route is the PubChem InChIKey
`ZSPZNFOLWQEVQJ-UHFFFAOYSA-N`, which resolves `CHEMBL309263`.

## Research Decision

Track `3,4'-Di-O-methylquercetin` as a lower-priority quercetin analog seed.

It should not be treated as ordinary quercetin supplementation. The promotion
gates are:

- obtain the exact `CID 5380905` / `CHEMBL309263` structure or supplier record;
- verify purity and stereochemical/tautomer identity where relevant;
- repeat K562 reporter and add endogenous HbF protein/F-cell endpoints;
- test red-cell hemolysis;
- test HUDEP-2 or primary erythroid maturation models;
- test beta-thalassemia/HbE primary erythroid cells when accessible;
- compare against `T-BDMC`, `isocoronarin D`, hydroxyurea, decitabine, and
  vehicle controls.

## Sources

- [Quercetin analogs DOI](https://doi.org/10.1007/s00044-019-02412-7)
- [Quercetin analogs Crossref snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-analogs-hbf-crossref.json)
- [Quercetin analogs exact-title PubMed snapshot](../../../data/literature/pubmed/2026-04-27-quercetin-analogs-hbf-title.json)
- [Quercetin analogs ChEMBL DOI document snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-quercetin-analogs-document.json)
- [Quercetin PubChem snapshot](../../../data/chemistry/pubchem/quercetin-analogs/2026-04-27-quercetin-properties.json)
- [Quercetin ChEMBL search snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-quercetin-search.json)
- [3,4'-Di-O-methylquercetin PubChem snapshot](../../../data/chemistry/pubchem/quercetin-analogs/2026-04-27-quercetin-3-4-dimethyl-ether-properties.json)
- [3,4'-Di-O-methylquercetin ChEMBL search snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-3-4-di-o-methylquercetin-search.json)
- [3-O-methyltamarixetin ChEMBL noisy search snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-3-o-methyltamarixetin-search.json)
- [3,4'-Di-O-methylquercetin ChEMBL InChIKey snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-3-4-di-o-methylquercetin-inchikey-search.json)
- [3,4'-Di-O-methylquercetin ChEMBL molecule snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-3-4-di-o-methylquercetin-chembl309263.json)
- [3,4'-Di-O-methylquercetin ChEMBL activity snapshot](../../../data/chemistry/chembl/quercetin-analogs/2026-04-27-3-4-di-o-methylquercetin-chembl-activities.json)
- [Natural-product HbF expansion map](2026-04-27-natural-product-hbf-expansion-map.md)
