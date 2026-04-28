# Finding: Case-001 High-HbF Genotype Evidence Gate

Date checked: 2026-04-28
Evidence label: de-identified case-context interpretation, not diagnosis and
not treatment advice

## Working Conclusion

Case-001 should stay labeled `phenotype_only`.

The historical infancy record is strong enough to route the case into a
genotype-first gate: severe microcytic hypochromic anemia, HbF 97.6%, HbA2
2.0%, and reported hemoglobin types A, F, and A2 are compatible with a severe
beta-globin disorder, but they do not resolve the molecular subtype.

The most important blocker is still not "which candidate should we test?"
It is:

> What exact globin genotype and modifier context produced this phenotype?

## Why This Matters

The case is directly relevant to the repo's strongest research lane:

`HPFH-like HbF/F-cell rescue + alpha-globin/autophagy cleanup + preserved erythroid maturation + no mature red-cell hemolysis`.

But the case does not prove HPFH, beta-plus disease, alpha-thalassemia
co-inheritance, or a specific HbF modifier. It only proves that those are
reasonable questions to ask the hematologist because the original clinical
report itself raised beta-plus, HPFH, and alpha-thalassemia co-inheritance as
possible interpretations.

## Source-Backed Interpretation

| Observation | What it supports | What it does not prove |
| --- | --- | --- |
| Hb around 3.8-3.9 g/dL in infancy with microcytosis, hypochromia, anisopoikilocytosis, and rare nucleated RBCs | Severe thalassemia phenotype is plausible and aligns with beta-thalassemia major suggestive findings. | It does not identify the exact `HBB` alleles or exclude interacting disorders. |
| HbF 97.6% | HbF biology is highly relevant to this case and to HPFH-like rescue benchmarks. | It does not prove hereditary persistence of fetal hemoglobin because beta-thalassemia major can also show very high HbF. |
| HbA reported present | Residual beta-globin production, beta-plus context, or transfusion context must be considered. | It does not prove beta-plus unless the sample timing and molecular result support it. |
| HbA2 2.0% | The classic age-over-12-month beta-thalassemia major pattern is not fully captured by this value. | It does not rule out beta-thalassemia because age, transfusion, delta-beta/HPFH context, and molecular variation can complicate hemoglobin fractions. |
| Original report mentioned HPFH or alpha-thalassemia co-inheritance | `HBA1/HBA2`, HPFH, delta-beta, and HBG modifier questions are justified. | It does not establish that either modifier is present. |

## Highest-Value Missing Evidence

Ask for these records before making any patient-relevance claim:

1. Was the historical hemoglobin analysis performed before any transfusion?
2. Is there an `HBB` molecular result, including beta-zero or beta-plus
   interpretation?
3. Has `HBA1/HBA2` deletion and duplication testing been performed?
4. Is there any HPFH, delta-beta-thalassemia, `HBG1/HBG2` promoter, XmnI-HBG2,
   `BCL11A`, or `HBS1L-MYB` modifier result?
5. What are the current adult-state records: pre-transfusion Hb trend,
   transfusion volume, antibody screen, DAT/direct Coombs, spleen status,
   ferritin trend, liver iron MRI, cardiac `T2*`, chelation drug, and immune
   diagnosis?

## Research Routing Decision

| Lane | Current status for case-001 |
| --- | --- |
| HbF/HPFH-like rescue | Relevant, but only as a research benchmark until molecular context is known. |
| Alpha-globin burden and autophagy cleanup | Relevant because alpha co-inheritance and globin balance are unresolved. |
| Hydroxyurea, sirolimus, PF-06409577, curcuminoid analogs, or other candidates | Not patient-matched from this record alone. They remain assay candidates or comparators only. |
| Gene therapy, CRISPR, HSCT, luspatercept, mitapivat, iron-axis drugs | Clinician/referral questions only; no patient recommendation from Nakafa Lab. |

## Notebook Result

The companion notebook ranks missing evidence by record-request urgency, not by
diagnostic probability:

- highest blockers: `HBB`, `HBA1/HBA2`, HPFH/delta-beta/HBG modifier context,
  and transfusion proximity before historical HPLC;
- durable conclusion: case-001 remains `phenotype_only`;
- research consequence: the case strengthens HbF and globin-balance relevance,
  but blocks candidate-to-patient claims.

Notebook:
[`2026-04-28-case001-high-hbf-genotype-evidence-gap.ipynb`](../notebooks/2026-04-28-case001-high-hbf-genotype-evidence-gap.ipynb)

## Boundary

This finding is not diagnosis, prognosis, or therapy advice. It is a research
and clinician-question gate for a de-identified case. Treatment decisions,
transfusion interval, chelation, immune management, genetic testing, and
advanced-therapy eligibility belong to qualified clinicians.

## Sources

- [Beta-Thalassemia GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [TIF 2025 genetic basis, pathophysiology, and diagnosis chapter](https://www.ncbi.nlm.nih.gov/books/NBK614253/)
- [Alpha-Thalassemia GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1435/)
- [Delta beta thalassemia and HPFH, PubMed PMID 1713909](https://pubmed.ncbi.nlm.nih.gov/1713909/)
- [Flow cytometric measurement of HbF for HPFH distinction, PubMed PMID 12047136](https://pubmed.ncbi.nlm.nih.gov/12047136/)
- [Contrasting co-inheritance of alpha and beta mutations in delta beta thalassemia and HPFH, PubMed PMID 29621931](https://pubmed.ncbi.nlm.nih.gov/29621931/)
- [Alpha globin alterations modifying homozygous beta-thalassemia phenotype, PubMed PMID 38895064](https://pubmed.ncbi.nlm.nih.gov/38895064/)
- [Case-001 medical record extraction](../case-context/case-001-medical-record-extraction-2026-04-28.md)
- [`case001` PubMed snapshot set](../../../data/literature/pubmed/)
