# Finding: Weekly Transfusion Differential Map

Date checked: 2026-04-27
Evidence label: guideline and literature extraction, not treatment advice

## Working Conclusion

Weekly transfusion in a young adult with thalassemia is a high-priority signal,
but it is not interpretable from interval alone.

The clinically useful question is:

> Is weekly transfusion caused by disease severity, transfusion under-dosing,
> blood-product characteristics, shortened red-cell survival, immune
> destruction, hypersplenism, bleeding/infection, or a deliberate low-volume
> schedule?

This needs medical records and transfusion-blood-bank review. The repo should
not infer the cause from family memory.

## Guideline Anchor

TIF blood-transfusion guidance recommends transfusion every `2-5 weeks` while
maintaining pre-transfusion hemoglobin above `90-105 g/L`, or higher in selected
cardiac-complication contexts. It also recommends tracking red-cell antibodies,
transfusion reactions, and annual transfusion requirements.

This does not mean weekly transfusion is automatically wrong. It means the
schedule needs a reason that can be measured.

## Differential Map

| Possible driver | Why it could cause frequent transfusion | Data needed |
| --- | --- | --- |
| Severe genotype / phenotype | Very low endogenous hemoglobin production can shorten the time to target Hb | exact diagnosis, `HBB/HBA` genotype, HPLC/electrophoresis, baseline HbF |
| Low pre-transfusion Hb target failure | Hb may be falling below target before the next scheduled transfusion | pre-transfusion Hb trend, post-transfusion Hb, symptoms |
| Low transfused hemoglobin per visit | Weekly visits may reflect small-volume transfusion rather than unusually high annual blood exposure | ml transfused, unit count, hematocrit/Hb per unit, body weight |
| Blood-product preparation differences | Red-cell concentrate Hb content can change transfusion indices and interval | product type, Hb grams per unit, leukoreduction method |
| Shortened donor RBC survival | Poor 24-hour survival or faster RBC loss can reduce interval or increase units | post-transfusion increment, hemolysis labs, RBC survival clues |
| Alloantibodies / autoantibodies / AIHA | Immune destruction can cause crossmatch difficulty, hemolysis, or unexpectedly low Hb | antibody screen, named alloantibodies, DAT, IAT, crossmatch history |
| Hypersplenism / spleen effect | Enlarged or overactive spleen can increase blood requirement; splenectomy has serious risks and is not a casual fix | spleen size, platelet/WBC counts, annual pure red-cell requirement |
| Delayed hemolytic transfusion reaction | Hb drops, jaundice, malaise, or dark urine days after transfusion can signal new/undetected antibodies | symptoms 5-14 days post-transfusion, repeat blood-bank workup |
| Infection, inflammation, bleeding, or other comorbidity | Non-thalassemia problems can increase anemia burden | clinician exam, reticulocytes, bilirubin, LDH, stool/bleeding history, infection workup |

## Calculation Checklist

Ask the clinician or transfusion unit for enough data to compute:

```text
annual transfusion volume = total transfused red-cell volume per year / body weight
annual pure red-cell volume = annual transfusion volume x red-cell hematocrit fraction
daily transfusional iron loading = annual pure red-cell volume x 1.08 / 365
```

Interpretation needs clinician review, but the calculation prevents a common
mistake: comparing "weekly" versus "monthly" without knowing volume, body
weight, and blood-product content.

## Records To Request

- last 6-12 months of transfusion dates;
- units and/or ml per transfusion;
- body weight at transfusion visits;
- pre-transfusion and post-transfusion hemoglobin;
- red-cell product type and Hb content if available;
- antibody screen, antibody ID, DAT/direct Coombs, and crossmatch notes;
- delayed reaction history: fever, jaundice, dark urine, back pain, malaise,
  or unexpectedly low Hb after transfusion;
- spleen size and spleen status;
- ferritin, liver iron concentration, and cardiac `T2*` if available.

## Research Implication

This lane changes how we evaluate a possible "cure."

If weekly transfusion is mostly disease severity, then HbF induction or globin
balance remains the strongest cure-mimic lane. If it is partly red-cell
survival, immune destruction, or hypersplenism, then any candidate also needs
red-cell survival, hemolysis, and immune-compatibility gates.

This is why the first assay work order now includes mature red-cell hemolysis
alongside HbF endpoints.

## Sources

- [TIF blood-transfusion chapter, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2021 TDT guideline PDF](https://www.thalassemia.org/wp-content/uploads/2021/06/TIF-2021-Guidelines-for-Mgmt-of-TDT.pdf)
- [TDT pre-transfusion Hb and interval PubMed search](../../../data/literature/pubmed/2026-04-27-tdt-pretransfusion-hb-interval-search.json)
- [TDT transfusion requirement and splenectomy search](../../../data/literature/pubmed/2026-04-27-tdt-transfusion-requirement-splenectomy-search.json)
- [Thalassemia hypersplenism and red-cell survival search](../../../data/literature/pubmed/2026-04-27-thalassemia-hypersplenism-red-cell-survival-search.json)
- [Weekly transfusion differential search](../../../data/literature/pubmed/2026-04-27-tdt-weekly-transfusion-differential-search.json)
- [Weekly transfusion differential selected abstracts](../../../data/literature/pubmed/2026-04-27-weekly-transfusion-differential-selected-abstracts.xml)
- [Immune transfusion risk extraction](2026-04-27-immune-transfusion-risk-extraction.md)
- [First HbF and red-cell safety assay work order](../assays/2026-04-27-first-assay-work-order-v0.md)
