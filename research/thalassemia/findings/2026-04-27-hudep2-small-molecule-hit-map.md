# Finding: HUDEP2 Small-Molecule Hit Map

Date checked: 2026-04-27
Evidence label: assay-platform hit map, not treatment advice

## Working Conclusion

The 2024 HUDEP2 `HBG1` HiBiT screen gives Nakafa Lab a stronger validation
benchmark than K562-only natural-product hits.

The study screened about 5000 annotated clinical-stage or FDA-approved
compounds, confirmed 10 HUDEP2 hits, and highlighted four novel HbF-inducing
small molecules: `avadomide`, `autophinib`, `triciribine`, and `R574`.

This does not make any of them patient-ready. It does create a useful comparator
lane for mechanism discovery and assay validation.

The primary-cell validation boundary matters: the source selected
`pomalidomide`, `avadomide`, and `idoxuridine` for human `CD34+` validation.
Among the four novel hit names, only `avadomide` clearly crosses into that
primary-cell lane in the published text.

## Retrieved Hit Identity

| Hit | Identity status | Mechanism lane from source context | Current research interpretation |
| --- | --- | --- | --- |
| `avadomide` | PubChem `CID 24967599`; ChEMBL `CHEMBL3989934`; ChEMBL max phase `2` | thalidomide/pomalidomide analog; cereblon/IKZF/BCL11A-adjacent repression biology | strongest mechanistic comparator, but high caution because it sits near thalidomide-class pharmacology |
| `autophinib` | PubChem `CID 129626605`; ChEMBL `CHEMBL4639853` | VPS34/autophagy inhibition | target-discovery lead, not an access-ready therapy idea |
| `triciribine` | PubChem `CID 65399`; ChEMBL `CHEMBL331237`; phosphate form PubChem `CID 43860`, ChEMBL `CHEMBL462018` | AKT/DNA-synthesis inhibitor context | high-caution oncology-like signaling/cytotoxicity lane |
| `R574` / probable `R547` | `R574` text search returned no clean ChEMBL hit; source citation and CDK1/2/4 mechanism resolve to `R547` / ChEMBL `CHEMBL384304` / PubChem `CID 6918852` | CDK1/2/4 ATP-competitive inhibitor in source context | label discrepancy; use `R547` for chemistry lookup, keep high-caution benchmark status |

## Assay Evidence From The Source

The PLOS/PubMed source reports:

- a HUDEP2 `HBG1` HiBiT endogenous reporter system;
- a screen of about 5000 annotated compounds;
- 10 confirmed HUDEP2 hits;
- known HbF inducers in the hit set, including pomalidomide, lenalidomide,
  decitabine, idoxuridine, and azacytidine;
- four novel hit names: `avadomide`, `autophinib`, `triciribine`, and `R574`;
- orthogonal confirmation of selected top hits in parental HUDEP2 cells and
  human primary `CD34+` hematopoietic stem/progenitor cells;
- mechanistic follow-up showing pomalidomide and avadomide, but not
  idoxuridine, downregulated fetal-globin repressors including `BCL11A`,
  `ZBTB7A`, and `IKZF1`.

## Research Decision

Use these molecules as a validation benchmark, not as patient treatment leads.

Priority use:

1. benchmark whether our natural-product seeds can survive the same HUDEP2 and
   primary-cell ladder;
2. use avadomide as a mechanistic comparator for `BCL11A`/`IKZF` downregulation
   biology, with thalidomide-class caution;
3. keep autophinib and triciribine as pathway probes until erythroid toxicity
   and disease-cell relevance are clearer;
4. track `R574` as probable `R547`, but do not treat the label discrepancy as
   fully closed until the exact screening-library record is recovered.

## Sources

- [Yang 2024 PubMed snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-small-molecule-hbf-agonists.dom.txt)
- [Yang 2024 PLOS snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-yang-2024-hudep2-hbf-agonists-plos.dom.txt)
- [Yang 2024 PMC blocked-route snapshot](../../../data/literature/fulltext/pubmed/2026-04-27-yang-2024-hudep2-hbf-agonists-pmc.dom.txt)
- [Avadomide PubChem snapshot](../../../data/chemistry/pubchem/hudep2-hbf-hits/2026-04-27-avadomide-properties.json)
- [Avadomide ChEMBL molecule snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-avadomide-chembl3989934.json)
- [Autophinib PubChem snapshot](../../../data/chemistry/pubchem/hudep2-hbf-hits/2026-04-27-autophinib-properties.json)
- [Autophinib ChEMBL molecule snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-autophinib-chembl4639853.json)
- [Triciribine PubChem snapshot](../../../data/chemistry/pubchem/hudep2-hbf-hits/2026-04-27-triciribine-properties.json)
- [Triciribine ChEMBL molecule snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-triciribine-chembl331237.json)
- [Triciribine phosphate PubChem snapshot](../../../data/chemistry/pubchem/hudep2-hbf-hits/2026-04-27-triciribine-phosphate-properties.json)
- [Triciribine phosphate ChEMBL molecule snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-triciribine-phosphate-chembl462018.json)
- [R574 ChEMBL unresolved search snapshot](../../../data/chemistry/chembl/hudep2-hbf-hits/2026-04-27-r574-search.json)
- [R574 / R547 label resolution](2026-04-27-r574-r547-label-resolution.md)
- [HUDEP2 primary validation boundary](2026-04-27-hudep2-primary-validation-boundary.md)
- [K562 to HUDEP2 validation guardrail](2026-04-27-k562-to-hudep2-validation-guardrail.md)
