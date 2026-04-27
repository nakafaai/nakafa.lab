# Finding: Trimethylangelicin and Citropten Identity Map

Date checked: 2026-04-27
Evidence label: furanocoumarin/coumarin sub-lane, not treatment advice

## Working Conclusion

The follow-on furanocoumarin search resolves two more concrete molecules from
the angelicin and bergamot literature:

- `4,6,4'-trimethylangelicin`, abbreviated here as exact TMA;
- `citropten`, also called `5,7-dimethoxycoumarin` or `limettin`.

Both remain research probes, not therapy candidates. Exact TMA is more directly
tied to the angelicin analog HbF paper. Citropten is tied to the bergamot
gamma-globin paper. Neither has a retrieved thalassemia trial, and both belong
inside the hazard-first furanocoumarin/coumarin boundary.

## Identity Resolution

| Candidate | Resolution | Evidence status | Decision |
| --- | --- | --- | --- |
| generic `trimethylangelicin` | PubChem `CID 129664851`, InChIKey `BWANQBUNIUOZBC-UHFFFAOYSA-N` | name-only PubChem hit; not the exact PubMed phototoxicity synonym checked here | do not use as the assay identity without structure confirmation |
| exact `4,6,4'-trimethylangelicin` | PubChem `CID 107731`, ChEMBL `CHEMBL173365`, InChIKey `ZARUKNQGJBWWBA-UHFFFAOYSA-N` | matches PubMed naming for `4,6,4'-trimethylangelicin` / `4,4',6-trimethylangelicin` | use this identity when tracking TMA |
| `citropten` / `limettin` | PubChem `CID 2775`, ChEMBL `CHEMBL481049`, InChIKey `NXJCRELRQHZBQA-UHFFFAOYSA-N` | matches bergamot paper naming and ChEMBL identity | track as citropten, not bergapten |

The generic and exact TMA records have the same formula, `C14H12O3`, but
different InChIKeys. This is enough to block procurement or assay planning until
the exact structure is pinned to the paper compound.

## Biomedical Evidence

PubMed search results:

- `trimethyl angelicin gamma globin` returned PMID `19777196`;
- `trimethyl angelicin fetal hemoglobin` returned no first-pass records;
- `citropten gamma globin` returned PMID `19371028`;
- `citropten fetal hemoglobin` returned PMID `19371028`.

Interpretation:

- exact TMA is an angelicin-analog lead, not a standalone clinical lead;
- citropten is a bergamot-extract component with K562 and healthy-donor
  erythroid precursor evidence in the abstract;
- neither result changes the priority order above `T-BDMC` or resveratrol.

## Safety Boundary

Exact TMA has a mixed signal:

- PubMed includes a 1984 title describing `4,4',6-trimethylangelicin` as very
  photoreactive and non skin-phototoxic;
- PubMed includes a Jurkat-cell phototoxicity study for UVA-activated
  `4,6,4'-trimethylangelicin`;
- PubMed includes a furocoumarin DNA-protein cross-link study where exact TMA
  was assessed in the same hazard neighborhood;
- ChEMBL `CHEMBL173365` includes DNA association, DNA-synthesis inhibition
  after irradiation, UVA treatment, lesion-clearance, erythema, and
  pigmentation records.

Citropten has a different but still cautionary signal:

- PubMed safety search links limettin/citropten to photomutagenicity and
  citrus phototoxicity contexts;
- ChEMBL `CHEMBL481049` activity records are broad and do not establish HbF
  relevance by themselves.

## Research Decision

Do not promote exact TMA or citropten to the active affordable-candidate list.

Use them as:

- positive mechanistic comparators for older natural-world HbF inducer papers;
- chemical identity test cases for avoiding ambiguous natural-product names;
- safety-boundary examples for phototoxicity, genotoxicity, and no-UVA handling.

Minimum gate before any wet-lab thought:

- exact `CID` and structure match to source paper;
- no-UVA handling and storage plan;
- hemolysis screen before efficacy claims;
- erythroid viability and maturation endpoints;
- endogenous HbF validation;
- phototoxicity and genotoxicity review by qualified collaborators.

## Sources

- [Trimethyl angelicin gamma-globin PubMed search](../../../data/literature/pubmed/2026-04-27-trimethyl-angelicin-gamma-globin-search.json)
- [Trimethyl angelicin fetal-hemoglobin PubMed search](../../../data/literature/pubmed/2026-04-27-trimethyl-angelicin-fetal-hemoglobin-search.json)
- [Citropten gamma-globin PubMed search](../../../data/literature/pubmed/2026-04-27-citropten-gamma-globin-search.json)
- [Citropten fetal-hemoglobin PubMed search](../../../data/literature/pubmed/2026-04-27-citropten-fetal-hemoglobin-search.json)
- [Trimethylangelicin PubChem properties](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-trimethylangelicin-properties.json)
- [Exact TMA PubChem properties](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-464-trimethylangelicin-properties.json)
- [Citropten PubChem properties](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-citropten-properties.json)
- [Exact TMA ChEMBL filter](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-464-trimethylangelicin-inchikey-filter.json)
- [Exact TMA ChEMBL activities](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-464-trimethylangelicin-chembl-activities.json)
- [Citropten ChEMBL molecule](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-citropten-chembl481049.json)
- [Citropten ChEMBL activities](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-citropten-chembl-activities.json)
- [TMA and citropten safety ESummary](../../../data/literature/pubmed/2026-04-27-trimethylangelicin-citropten-safety-esummary.json)
- [TMA and citropten safety abstract XML](../../../data/literature/pubmed/2026-04-27-trimethylangelicin-citropten-safety-abstracts.xml)
- [Trimethylangelicin thalassemia ClinicalTrials.gov snapshot](../../../data/registries/clinicaltrials/2026-04-27-trimethylangelicin-thalassemia-trials.json)
- [Citropten thalassemia ClinicalTrials.gov snapshot](../../../data/registries/clinicaltrials/2026-04-27-citropten-thalassemia-trials.json)
