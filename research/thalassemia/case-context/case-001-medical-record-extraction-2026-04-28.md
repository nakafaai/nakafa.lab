# Case-001 Medical Record Extraction 2026-04-28

Date extracted: 2026-04-28
Source: two historical local PDFs supplied by family
Privacy: de-identified extraction only
Status: clinical-context intake, not treatment advice

## Privacy Boundary

The raw PDFs were reviewed locally and are not copied into this repository.
This note intentionally excludes name, medical record number, lab accession,
exact address, facility name, doctor names, phone or fax numbers, signatures,
and exact sample date.

The committed record uses only broad timing and clinically relevant values.
Keep the raw files outside Git unless a future private medical-record store is
designed and threat-modeled.

## Extracted Facts

### Historical thalassemia screening record

Broad timing: infancy, approximately 11 months old.

| Field | Extracted value |
| --- | --- |
| Clinical context | Screening for suspected thalassemia |
| Hemoglobin | 3.9 g/dL |
| MCV | 69 fL |
| MCH | 22.3 pg |
| MCHC | 32.4 g/dL |
| RDW | 27.8% |
| HbA2 | 2.0% |
| HbF | 97.6% |
| Hemoglobin types reported | A, F, A2 |

Reported red-cell morphology:

- microcytic and hypochromic red cells;
- anisopoikilocytosis;
- many tear drop cells;
- polychromatic macrocytes;
- target cells, elliptocytes, and fragmentocytes;
- very rare nucleated red blood cells.

Report interpretation, paraphrased:

- red-cell indices and hemoglobin analysis were described as consistent with
  beta-thalassemia homozygous or compound heterozygous disease;
- at least one mutation was suspected to be beta-plus because HbA was still
  present;
- HPFH or alpha-thalassemia co-inheritance was raised as a possibility because
  the smear did not appear to show very severe hemolysis;
- parent thalassemia screening and genetic consultation were recommended.

### Historical complete blood count record

Broad timing: infancy, near the same diagnostic period.

| Field | Extracted value |
| --- | --- |
| Hemoglobin | 3.8 g/dL |
| Hematocrit | 12.3% |
| Leukocytes | 10.5 x10^3/uL |
| Platelets | 170 x10^3/uL |
| Erythrocytes | 1.80 x10^6/uL |
| ESR | 65 mm/hour |
| Basophils | 0% |
| Eosinophils | 0% |
| Bands | 3% |
| Segmented neutrophils | 26% |
| Lymphocytes | 64% |
| Monocytes | 7% |

## Research Interpretation Boundary

This record upgrades case-001 from `untyped` to `phenotype_only`: there is now
historical hemoglobin-analysis evidence, but no committed molecular `HBB`,
`HBA1`, `HBA2`, or HbF-modifier result.

The high HbF and reported residual HbA make the case directly relevant to the
repo's beta-thalassemia, HbF/HPFH-like rescue, and alpha-globin-balance lanes.
It does not prove which molecular route is present. The main gap remains
genotype confirmation.

The infancy hemoglobin values show a severe early anemia phenotype. They do not
answer the current adult-state questions: current genotype, transfusion burden,
pre-transfusion hemoglobin trend, iron burden, chelation status, immune status,
or organ-risk packet.

## Clinician Questions Added By This Record

- Was the historical hemoglobin analysis performed before any transfusion?
- Is a molecular `HBB` result available, including whether the variants are
  beta-zero or beta-plus?
- Has `HBA1/HBA2` deletion or duplication testing been performed?
- Were both parents screened, and can those results clarify compound
  heterozygosity?
- Is HPFH or another HbF-modifier context suspected or tested?
- Given current weekly transfusion, what are the latest pre-transfusion
  hemoglobin, antibody screen, DAT/direct Coombs, ferritin trend, liver iron
  MRI, and cardiac T2* results?

## Repository Handling

- Raw clinical PDFs: local-only, not tracked.
- This extraction: de-identified and suitable for public repo review.
- Clinical use: only as a question-preparation aid for hematology review.
- Future updates: use the
  [public case data release checklist](../../../templates/public-case-data-release-checklist.md)
  and
  [private-to-public case extraction template](../../../templates/private-to-public-case-extraction-template.md)
  before committing any new extracted case detail.
