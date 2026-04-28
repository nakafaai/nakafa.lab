# De-identified Case Context 001

Date recorded: 2026-04-26
Last updated: 2026-04-28
Source: family-reported conversation plus de-identified extraction from two
historical local medical-record PDFs
Privacy: no name, exact address, hospital, phone number, ID, or photo

## Known From Family Report

- Age: 20 years old.
- Transfusion: reported as weekly.
- Daily medication: yes, exact medicine not yet recorded.
- Autoimmune issue: reported, exact diagnosis not yet recorded.
- Thalassemia subtype: not yet recorded.
- Genetic test result: not yet recorded.
- Iron overload status: not yet recorded.

## Known From Historical Medical Records

- Broad timing: infancy, approximately 11 months old.
- Historical thalassemia screening showed severe anemia with hemoglobin
  3.9 g/dL, MCV 69 fL, MCH 22.3 pg, RDW 27.8%, HbA2 2.0%, HbF 97.6%, and
  hemoglobin types A, F, and A2.
- Screening interpretation was consistent with beta-thalassemia homozygous or
  compound heterozygous disease, with possible beta-plus mutation, HPFH, or
  alpha-thalassemia co-inheritance. This is not molecular confirmation.
- A near-period complete blood count showed hemoglobin 3.8 g/dL, hematocrit
  12.3%, leukocytes 10.5 x10^3/uL, platelets 170 x10^3/uL, erythrocytes
  1.80 x10^6/uL, and ESR 65 mm/hour.
- Parent screening and genetic consultation were recommended in the historical
  screening record.

## Interpretation Boundary

Weekly transfusion suggests a severe or transfusion-dependent phenotype. The
historical screening record supports a beta-thalassemia phenotype, but the repo
must not assign a final molecular diagnosis without `HBB` and `HBA` results or
clinician confirmation.

Current genotype-first label: `phenotype_only`.

The reported autoimmune issue is important because it may affect transfusion
compatibility, hemolysis risk, medication choices, and clinical-trial
eligibility. The exact term should be confirmed from a doctor's note or lab
report before we use it as evidence.

The 2026-04-27 immune/transfusion complication lane turns this into a concrete
data request: antibody screen, named alloantibodies, direct antiglobulin test
(direct Coombs), crossmatch difficulty, transfusion reaction history, spleen
status, hemolysis markers, and the exact autoimmune diagnosis if one exists.

The 2026-04-27 iron-overload organ-risk gate adds a second concrete packet:
ferritin trend, liver iron concentration MRI, cardiac `T2*`, chelator name and
dose, adherence, side effects, kidney/liver monitoring, and endocrine/organ
screening. Until those are known, patient-fit claims should stay blocked.

## Research Relevance

This case makes the first Nakafa Lab program practical, not abstract. The near
term research priority is not replacing the clinician. It is building an
evidence map that can help clinicians evaluate:

- whether the current care matches modern thalassemia guidelines;
- whether transfusion frequency can be safely reduced by approved or
  investigational approaches;
- whether iron overload and organ monitoring are complete;
- whether immune complications need a separate specialist review;
- which curative or disease-modifying options are scientifically plausible and
  financially realistic.

## Data To Collect Later

- Exact current diagnosis and subtype.
- HPLC or electrophoresis fractions from current records: HbA, HbA2, HbF, and
  HbE if reported.
- Whether the historical hemoglobin analysis happened before any transfusion.
- HBB and HBA genetic testing results if available.
- HbF modifier results if available, especially XmnI-HBG2 and BCL11A variants.
- Hemoglobin values before transfusion.
- Ferritin trend and liver/cardiac iron assessment if available.
- Current chelation medicine, dose, adherence, and side effects.
- Blood type, antibody history, transfusion reactions, and alloimmunization
  status if available.
- Direct antiglobulin test / direct Coombs result if available.
- Whether transfused red cells are matched for ABO, Rh C/c, Rh D, Rh E/e, and
  Kell.
- Autoimmune diagnosis, tests, symptoms, and treatment.
- Spleen status plus liver, heart, endocrine, and bone monitoring.
- Prior genetic testing for patient and parents if available.

Do not add identifying details to this file.

## Linked Notes

- [Clinician review brief](clinician-brief-case-001.md)
- [Hematologist question sheet](hematologist-question-sheet-case-001.md)
- [Medical record extraction 2026-04-28](case-001-medical-record-extraction-2026-04-28.md)
- [Immune and transfusion complication lane](../findings/2026-04-27-immune-transfusion-complication-lane.md)
- [Iron overload organ-risk gate](../findings/2026-04-27-iron-overload-organ-risk-gate.md)
- [Indonesia genotype-first rule](../findings/2026-04-27-indonesia-genotype-first-rule.md)
