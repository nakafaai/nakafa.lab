# Finding: Chemistry Identity Benchmark Map

Date checked: 2026-04-27
Evidence label: chemistry identity and assay benchmark, not treatment advice

## Working Conclusion

Nakafa Lab needs exact material identity before any candidate enters an HbF
or red-cell safety screen. A vague label such as "honey", "propolis",
"venom", or "curcumin extract" is not enough for cure-oriented research.

The current benchmark set is:

- hydroxyurea as the low-cost positive HbF comparator;
- decitabine as a high-caution `DNMT1` proof-of-biology boundary;
- sirolimus as an mTOR/autophagy repurposing comparator;
- curcumin as a natural-product-adjacent chemistry comparator, not as a
  thalassemia cure claim.

## Benchmark Identity Table

| Compound | PubChem CID | ChEMBL snapshot | Research role | Caution |
| --- | --- | --- | --- | --- |
| Hydroxyurea | `3657` | `CHEMBL467` search hit | Positive HbF comparator with clinical familiarity and affordability relevance. | ChEMBL flags a black-box warning; use as assay comparator, not unsupervised therapy. |
| Decitabine | `451668` | `CHEMBL1201129` search hit | `DNMT1` proof-of-biology comparator for epigenetic HbF induction. | High-caution marrow and dosing boundary; not a casual chronic-use candidate. |
| Sirolimus | `5284616` | `CHEMBL413` via rapamycin search hit | mTOR/autophagy repurposing comparator linked to beta-thalassemia pilot evidence. | ChEMBL flags a black-box warning; immune suppression and monitoring burden must stay explicit. |
| Curcumin | `969516` | `CHEMBL140` search hit | Natural-product-adjacent benchmark for curcuminoid/trienone analog follow-up. | Bioavailability, potency, and replication gaps remain major blockers. |

## Research Rules

- A material cannot be promoted by name alone; it needs `CID`, `ChEMBL ID`,
  supplier/batch identity, or an equivalent chemistry/batch record.
- Extracts and bee-derived materials need standardization markers before they
  are compared with purified compounds.
- The first scientific question is whether the material reproducibly affects
  `HBG1/HBG2`, HbF protein, erythroid maturation, and mature red-cell
  hemolysis.
- Safety blockers outrank enthusiasm. A candidate with HbF signal but
  hemolysis, broad cytotoxicity, immune risk, or vague identity stays on hold.

## What This Changes

The discovery path now has a stricter intake layer. Candidate ideas from
Quranic motivation, natural products, or repurposed drugs can enter the same
assay funnel, but only after the material identity is auditable.

This protects the project from false positives. It also makes future
clinician review easier because every assay result can be traced back to a
defined compound, fraction, or batch.

## Sources

- [PubChem hydroxyurea snapshot](../../../data/chemistry/pubchem/2026-04-27-hydroxyurea-properties.json)
- [PubChem decitabine snapshot](../../../data/chemistry/pubchem/2026-04-27-decitabine-properties.json)
- [PubChem sirolimus snapshot](../../../data/chemistry/pubchem/2026-04-27-sirolimus-properties.json)
- [PubChem curcumin snapshot](../../../data/chemistry/pubchem/2026-04-27-curcumin-properties.json)
- [ChEMBL hydroxyurea snapshot](../../../data/chemistry/chembl/2026-04-27-hydroxyurea-search.json)
- [ChEMBL decitabine snapshot](../../../data/chemistry/chembl/2026-04-27-decitabine-search.json)
- [ChEMBL rapamycin search snapshot for sirolimus](../../../data/chemistry/chembl/2026-04-27-rapamycin-search.json)
- [ChEMBL sirolimus search snapshot, noisy query control](../../../data/chemistry/chembl/2026-04-27-sirolimus-search.json)
- [ChEMBL sirolimus rapamycin search snapshot](../../../data/chemistry/chembl/2026-04-27-sirolimus-rapamycin-search.json)
- [ChEMBL curcumin snapshot](../../../data/chemistry/chembl/2026-04-27-curcumin-search.json)
- [Epigenetic HbF screen V0](../assays/2026-04-27-epigenetic-hbf-screen-v0.md)
- [Epigenetic HbF target drilldown](2026-04-27-epigenetic-hbf-target-drilldown.md)
