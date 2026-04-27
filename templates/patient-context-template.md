# Patient Context Template

Use this only for de-identified research context. Do not include name, exact
address, hospital record number, phone number, ID number, face photo, or exact
birth date.

## Core Fields

- Case ID:
- Date recorded:
- Source type: family report / clinician note / lab result / publication
- Age range and broad region:
- Thalassemia type and genotype if known:
- Genotype-first intake label: `untyped` / `phenotype_only` /
  `hbb_confirmed` / `hbb_hba_confirmed` / `modifier_context_known`
- HPLC or electrophoresis date and transfusion proximity:
- Transfusion-dependent status:
- Important comorbidities:
- Transfusion schedule and pre-transfusion hemoglobin:
- Chelation medicine and other daily medicines:
- Known allergies or transfusion reactions:
- Ferritin trend, liver iron, and cardiac iron:
- Heart, liver, endocrine, and bone monitoring:
- Alloantibodies, autoantibodies, or autoimmune diagnosis:
- Linked clinical timeline CSV:
- Linked clinical record index CSV:

## Research Questions

- What problem are we trying to clarify?
- What evidence is needed?
- Which clinician should review this?

## Privacy Check

- No direct identifier included:
- Details are broad enough to avoid re-identification:
- Patient or family permission status:

## Timeline Workflow

- Record index copied from `templates/clinical-record-index-template.csv`:
- Timeline copied from `templates/case-clinical-timeline-template.csv`:
- Timeline summary command run:
