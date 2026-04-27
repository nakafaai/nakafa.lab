# Finding: Furanocoumarin HbF Hazard Map

Date checked: 2026-04-27
Evidence label: HbF mechanism probes with hazard-first triage, not treatment advice

## Working Conclusion

Angelicin and bergapten are real natural-product HbF/gamma-globin seeds, but
they should be treated as hazard-first mechanism probes rather than affordable
therapy leads.

The reason is not weak biology. The retrieved literature connects
furanocoumarins to erythroid differentiation, gamma-globin messenger RNA, and
HbF-adjacent endpoints. The problem is safety translation: these compounds sit
in a psoralen/furanocoumarin neighborhood where DNA binding, UVA-linked
phototoxicity, and cytotoxicity are central concerns.

## Identity Snapshot

| Compound | PubChem | ChEMBL | Formula | Translation status |
| --- | --- | --- | --- | --- |
| angelicin | `CID 10658` | `CHEMBL53569` | `C11H6O3` | natural-product HbF seed; no retrieved thalassemia trial |
| bergapten / 5-methoxypsoralen | `CID 2355` | `CHEMBL24171` | `C12H8O4` | natural-product HbF seed; no retrieved thalassemia trial |

## Biomedical Evidence

| PMID | Focus | Useful signal | Limitation |
| --- | --- | --- | --- |
| `12930320` | angelicin | K562 gamma-globin mRNA plus normal human erythroid precursor HbF signal | no beta-thalassemia patient-cell data in the abstract |
| `19777196` | angelicin analogs | K562, gamma-globin EGFP reporter, and erythroid progenitors from normal donors and beta-thalassemia patients | analog identity and safety need deeper extraction |
| `19371028` | bergamot extract, citropten, bergapten | K562, gamma-globin EGFP reporter, and healthy-donor erythroid progenitors | extract mixture plus no patient-cell validation in the abstract |
| `23518160` | furocoumarins and photoproducts | furocoumarins induce K562 erythroid differentiation and globin messenger RNA | UV-A/DNA photodamage context is a safety red flag |
| `20001626` | fetal globin induction review | angelicin and resveratrol described as natural HbF inducers in thalassemia progenitors | review-level source, not a clinical trial |
| `18955291` | natural-world HbF inducers review | angelicin, linear psoralens, resveratrol, and rapamycin framed as HbF-inducer leads | review-level source, not a therapy decision |

## Hazard Boundary

ChEMBL activity records for both compounds include UVA-linked cell-growth
inhibition in HT1080 human fibrosarcoma cells.

For angelicin, retrieved records include IC50 values of `15700 nM`, `2600 nM`,
and `2500 nM` after UVA irradiation at increasing dose conditions. Additional
records include calf thymus DNA association and DNA/RNA synthesis inhibition
after irradiation.

For bergapten, retrieved records include IC50 values of `8500 nM`, `1800 nM`,
and `900 nM` after UVA irradiation at increasing dose conditions.

Interpretation:

- these records do not directly prove red-cell toxicity;
- they do prove this chemical neighborhood needs phototoxicity and genotoxicity
  review before any translational enthusiasm;
- for a severe anemia program, a candidate that can damage DNA or cells under
  light-linked conditions cannot be ranked like a normal polyphenol seed.

## Clinical Registry Check

ClinicalTrials.gov first-pass intervention/condition snapshots returned zero
thalassemia studies for:

- `angelicin` and thalassemia;
- `bergapten` and thalassemia.

This does not mean the compounds are useless. It means they currently belong in
the mechanistic comparison and hazard-boundary lane, not a patient-facing lane.

## Research Decision

Do not rank angelicin or bergapten above `T-BDMC`, resveratrol, or other seeds
with cleaner safety-translation paths.

If a qualified collaborator ever tests this lane, the minimum guardrails are:

- purified compound identity and batch trace;
- no-UVA handling condition specified;
- mature red-cell hemolysis before efficacy claims;
- erythroid viability and maturation endpoints;
- endogenous HbF or primary erythroid validation;
- genotoxicity and phototoxicity review before any animal or clinical thought;
- no patient self-experimentation.

## Relation To Quranic Natural-Material Search

This lane supports a broad Quran-inspired search posture without collapsing
spiritual inspiration into biomedical proof. Quran 6:99 widens attention to
botanical diversity, including fruits and plant materials, but the ranking here
comes from PubMed, PubChem, ChEMBL, and ClinicalTrials.gov evidence.

## Sources

- [Angelicin fetal-hemoglobin PubMed search](../../../data/literature/pubmed/2026-04-27-angelicin-fetal-hemoglobin-search.json)
- [Bergapten fetal-hemoglobin PubMed search](../../../data/literature/pubmed/2026-04-27-bergapten-fetal-hemoglobin-search.json)
- [Furanocoumarin gamma-globin PubMed search](../../../data/literature/pubmed/2026-04-27-furanocoumarin-gamma-globin-search.json)
- [Furanocoumarin HbF PubMed ESummary](../../../data/literature/pubmed/2026-04-27-furanocoumarin-hbf-esummary.json)
- [Furanocoumarin HbF PubMed abstract XML](../../../data/literature/pubmed/2026-04-27-furanocoumarin-hbf-abstracts.xml)
- [Angelicin PubChem properties](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-angelicin-properties.json)
- [Bergapten PubChem properties](../../../data/chemistry/pubchem/natural-product-hbf/2026-04-27-bergapten-properties.json)
- [Angelicin ChEMBL molecule](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-angelicin-chembl53569.json)
- [Bergapten ChEMBL molecule](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-bergapten-chembl24171.json)
- [Angelicin ChEMBL activities](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-angelicin-chembl-activities.json)
- [Bergapten ChEMBL activities](../../../data/chemistry/chembl/natural-product-hbf/2026-04-27-bergapten-chembl-activities.json)
- [Angelicin thalassemia ClinicalTrials.gov snapshot](../../../data/registries/clinicaltrials/2026-04-27-angelicin-thalassemia-trials.json)
- [Bergapten thalassemia ClinicalTrials.gov snapshot](../../../data/registries/clinicaltrials/2026-04-27-bergapten-thalassemia-trials.json)
- [Quran 6:99 structured note](../../islamic/quran/006-al-anam/099.md)
