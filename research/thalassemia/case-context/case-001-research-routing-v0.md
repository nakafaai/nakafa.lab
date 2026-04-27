# Case-001 Research Routing Matrix V0

Date: 2026-04-27
Status: de-identified research routing, not treatment advice

## Purpose

This file keeps research moving while case-001 records are incomplete. It maps
future medical-record answers into research lanes, so new details do not become
loose conversation notes.

The core question is not "which medicine should the patient take?" The core
question is:

> Which measurable blocker explains the current burden, and which research lane
> can address that blocker without creating a new safety problem?

## First Gate

Do not make a patient-relevance claim until these fields are known or explicitly
marked unknown:

- thalassemia class: `TDT`, `NTDT`, HbE/beta, alpha, or mixed;
- `HBB` and `HBA` genotype if available;
- Hb fractions: HbA, HbA2, HbF, and HbE if present;
- transfusion dates, units or volume, and pre-transfusion hemoglobin;
- antibody screen, named alloantibodies, `DAT`, and crossmatch notes;
- ferritin trend, liver iron MRI, and cardiac `T2*`;
- chelation drug, dose, adherence, and toxicity monitoring;
- spleen size/status;
- exact autoimmune diagnosis and immune medicines.

## Routing Matrix

| If the record shows | Route to | Why it matters | Next research action |
| --- | --- | --- | --- |
| Exact subtype or genotype is missing | genotype-first lane | Indonesian beta-thalassemia and HbE/beta-thalassemia are heterogeneous; wrong subtype can mis-rank candidates | keep all patient-fit labels as `unknown` |
| TDT with high annual red-cell volume | HbF and advanced-therapy benchmark lane | high burden strengthens the need for transfusion-reduction endpoints | compare candidates to gene/cell therapy, luspatercept, mitapivat, and HbF benchmarks |
| Weekly visits but low volume per visit | transfusion-schedule interpretation lane | interval alone can exaggerate burden if each visit is low-volume | calculate annual ml/kg/year and pure red-cell volume |
| Low baseline HbF or low F-cell signal | HPFH-like HbF lane | cure-mimic logic is strongest when increasing HbF could plausibly compensate beta-globin loss | prioritize `HBG1/HBG2`, HbF protein, F-cell, and globin-balance assays |
| High baseline HbF or HbF modifier signal | responder-signature lane | natural protection can explain phenotype and guide candidate interpretation | document `XmnI-HBG2`, `BCL11A`, `HBS1L-MYB`, and HPFH-like variants if available |
| Positive antibody screen, named alloantibodies, positive `DAT`, AIHA, or crossmatch difficulty | immune-transfusion lane | immune red-cell loss can mimic treatment failure or increase transfusion need | require red-cell survival, hemolysis, antibody, and blood-bank review gates |
| Jaundice, dark urine, malaise, fever, or unexpected Hb fall after transfusion | delayed hemolysis lane | delayed reactions can appear days after transfusion and change the interpretation of weekly need | ask for repeat blood-bank workup and reaction history |
| High ferritin, high liver iron, abnormal cardiac `T2*`, or chelator toxicity | iron and chelation lane | iron risk can be the urgent harm even before a cure exists | keep iron-axis candidates separate from iron-supplement or diet claims |
| Enlarged spleen, low platelets/WBC, or suspected hypersplenism | spleen and red-cell survival lane | hypersplenism can increase blood requirement and confound candidate response | record spleen status before interpreting HbF or transfusion response |
| Autoimmune diagnosis or immune medicines | safety/exclusion lane | immune context can change feasibility of sirolimus, thalidomide-class, transplant, or trial eligibility | do not promote immune-active candidates without clinician review |
| Doctor says luspatercept, mitapivat, HSCT, gene therapy, or CRISPR therapy is relevant | access and benchmark lane | current therapies define the strongest real-world endpoint standard | capture why it is possible, inaccessible, unsuitable, or not indicated |

## Cure-Search Implication

If the main driver is beta-globin production failure, the strongest cure-mimic
lane remains HPFH-like HbF reactivation and globin-chain rescue.

If the main driver is immune destruction, hypersplenism, or poor donor red-cell
survival, then HbF alone is not enough. Candidate assays must include mature
red-cell hemolysis, viability, and immune/transfusion safety context.

If the main driver is iron overload or chelation difficulty, the immediate
research value may be risk reduction and access optimization rather than a new
HbF drug.

## Doctor-Facing Questions

Ask these in order:

1. What exact subtype, genotype, and Hb fractions define this case?
2. Is weekly transfusion caused by high annual red-cell need, low per-visit
   volume, short red-cell survival, immune destruction, hypersplenism, or
   another factor?
3. Are antibody screen, named alloantibodies, `DAT`, Rh/Kell matching, extended
   phenotype/genotype, and crossmatch notes available?
4. Are ferritin, liver iron MRI, cardiac `T2*`, and chelation toxicity
   monitoring sufficient to judge current risk?
5. Are luspatercept, mitapivat, HSCT, gene therapy, CRISPR therapy, or a trial
   medically relevant, unsuitable, or inaccessible?

## Repo Rule

Every new case detail should update one of these files:

- [de-identified case context](deidentified-case-001.md);
- [clinician review brief](clinician-brief-case-001.md);
- [hematologist question sheet](hematologist-question-sheet-case-001.md);
- [HbF responder signature](../prioritization/2026-04-27-hbf-responder-signature-v0.md);
- [assay run template](../../../templates/assay-run-template.md), if lab data
  arrives.

## Islamic Research Boundary

The Islamic lane supports discipline: ask experts when knowledge is missing and
measure with balance. It does not turn any verse, food, supplement, or natural
material into a thalassemia treatment claim.

## Sources

- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [FDA mitapivat approval summary](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [Weekly transfusion differential map](../findings/2026-04-27-weekly-transfusion-differential-map.md)
- [Immune transfusion risk extraction](../findings/2026-04-27-immune-transfusion-risk-extraction.md)
- [HbF responder signature V0](../prioritization/2026-04-27-hbf-responder-signature-v0.md)
- [HPFH-like assay readout spec V0](../assays/2026-04-27-hpfh-like-assay-readout-spec-v0.md)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
