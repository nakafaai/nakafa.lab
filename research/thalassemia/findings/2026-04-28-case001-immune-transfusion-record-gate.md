# Finding: Case-001 Immune Transfusion Record Gate

Date checked: 2026-04-28
Evidence label: de-identified case-context gate, not diagnosis and not
treatment advice

## Working Conclusion

Case-001 should carry an additional record label:

`immune_transfusion_packet_missing`

The family-reported combination of weekly transfusion and an unspecified
autoimmune issue cannot be interpreted safely without blood-bank and
transfusion-medicine records. The repo should not assume the weekly interval is
caused only by genotype or only by immune red-cell loss.

The research-safe question is:

> Is the current transfusion burden driven by beta-globin disease severity,
> transfusion volume/schedule, donor red-cell survival, alloantibodies,
> autoantibodies, DAT-positive hemolysis, delayed hemolytic transfusion
> reaction, hypersplenism, or another comorbidity?

## Why This Matters

If weekly transfusion is driven mostly by beta-globin production failure, the
strongest cure-mimic lane remains HbF/HPFH-like rescue plus globin-balance
readouts.

If weekly transfusion is partly driven by immune destruction, crossmatch
difficulty, delayed hemolysis, or hypersplenism, then HbF induction alone is
not enough. Candidate assays and doctor questions must include mature red-cell
hemolysis, red-cell survival, immune/transfusion safety, and blood-bank
compatibility.

## Source-Backed Update

The 2026-04-28 refresh recovered current and recent PubMed records around
alloimmunization, autoimmunization, direct antiglobulin testing, AIHA, and
red-cell antigen genotyping. The new snapshots do not diagnose case-001. They
raise the priority of asking for exact immune/transfusion records.

| Evidence area | Source signal | Case-001 implication |
| --- | --- | --- |
| Alloimmunization and autoimmunization | PubMed continues to recover adult and pediatric TDT studies on red-cell alloantibodies and autoantibodies, including a 2025 article on alloantibody prevalence in TDT. | Ask for antibody screen history and named alloantibodies instead of using the loose word "autoimmune." |
| DAT/direct Coombs | Focused queries recover direct antiglobulin test positivity in multi-transfused thalassemia and AIHA predictor literature. | Ask whether DAT is positive and whether IgG, C3, or both are involved. |
| Rh/Kell and antigen matching | TIF guidance and PubMed snapshots support Rh/Kell matching and red-cell antigen phenotype/genotype review, especially when serology is confounded. | Ask whether units are matched for Rh C/c, D, E/e, Kell, and whether extended phenotype/genotype is available. |
| Delayed hemolytic reaction | TIF guidance and beta-thalassemia case literature support delayed hemolysis as a transfusion-medicine concern. | Ask for jaundice, dark urine, fever, malaise, back pain, or unexpected Hb fall 5-14 days after transfusion. |
| Weekly interval | TIF guidance frames transfusion intervals and annual requirement as measurable, not guessable. | Ask for transfusion dates, unit or ml volume, body weight, pre-transfusion Hb, and post-transfusion Hb. |

## Highest-Value Record Requests

Ask a hematologist or transfusion-medicine team for exact records:

1. Antibody screen history, dates, and named alloantibodies.
2. `DAT` / direct Coombs result, including IgG and C3 specificity.
3. Whether autoimmune hemolytic anemia (`AIHA`) has ever been diagnosed.
4. Indirect antiglobulin test (`IAT`) or antibody identification panel if
   available.
5. Blood-bank matching policy: `ABO`, Rh D, Rh C/c, Rh E/e, Kell, and any
   extended matching.
6. Red-cell antigen phenotype or genotype, especially if recent transfusion or
   antibodies make serology hard.
7. Crossmatch difficulty or delayed compatible blood history.
8. Delayed reaction symptoms 5-14 days after transfusion: jaundice, dark urine,
   fever, back pain, malaise, or unexpected Hb fall.
9. Transfusion dates, units or ml volume, body weight, pre-transfusion Hb, and
   post-transfusion Hb for the last 6-12 months.
10. Spleen size/status, platelet trend, WBC trend, reticulocytes, bilirubin,
    LDH, haptoglobin, and clinician interpretation of hypersplenism or
    hemolysis.

## Notebook Result

The companion notebook ranks missing records by clinician-routing usefulness:

- highest priority: antibody screen/ID, DAT specificity, transfusion volume and
  Hb trend, Rh/Kell matching, and extended red-cell phenotype/genotype;
- durable label: `immune_transfusion_packet_missing`;
- research consequence: no candidate can be promoted from HbF or antioxidant
  markers alone if mature red-cell hemolysis or immune/transfusion safety is
  unresolved.

Notebook:
[`2026-04-28-case001-immune-transfusion-record-gate.ipynb`](../notebooks/2026-04-28-case001-immune-transfusion-record-gate.ipynb)

## Boundary

This finding is not a diagnosis of alloimmunization, autoimmunization, AIHA,
delayed hemolytic transfusion reaction, or hypersplenism. It is a record gate
that prevents the repo from overinterpreting weekly transfusion while immune
and blood-bank data are missing.

## Sources

- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [Immune transfusion risk extraction](2026-04-27-immune-transfusion-risk-extraction.md)
- [Weekly transfusion differential map](2026-04-27-weekly-transfusion-differential-map.md)
- [TDT alloimmunization refresh snapshot](../../../data/literature/pubmed/2026-04-28-tdt-alloimmunization-autoimmunization-refresh.json)
- [2025 TDT alloantibody snapshot, PMID 41263205](../../../data/literature/pubmed/2026-04-28-tdt-alloantibody-2025-pmid41263205.json)
- [Direct antiglobulin thalassemia snapshot](../../../data/literature/pubmed/2026-04-28-direct-antiglobulin-multitransfused-thalassemics.json)
- [AIHA/DAT beta-thalassemia snapshot](../../../data/literature/pubmed/2026-04-28-beta-thalassemia-aiha-dat-refresh.json)
- [RBC genotyping thalassemia snapshot](../../../data/literature/pubmed/2026-04-28-rbc-genotyping-thalassemia-alloimmunization.json)
- [Rh/Kell matching refresh snapshot](../../../data/literature/pubmed/2026-04-28-thalassemia-rh-kell-matching-refresh.json)
