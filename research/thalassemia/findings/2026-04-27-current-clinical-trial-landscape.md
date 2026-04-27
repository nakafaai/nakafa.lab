# Finding: Current Clinical Trial Landscape

Date checked: 2026-04-27
Scope: ClinicalTrials.gov API v2 snapshot, not treatment advice

## Working Conclusion

The active trial landscape still points to the same cure-oriented hierarchy:
cell or gene therapy is the closest existing cure-like path, while lower-cost
drug discovery should benchmark itself against measurable outcomes used in
human studies: transfusion independence, transfusion-reduction response,
hemoglobin response, HbF, liver iron concentration, safety, and long-term
follow-up.

The Indonesia-specific ClinicalTrials.gov pass remains thin: six all-status
records and no active Indonesia-located cure trial in this snapshot.

## Snapshot Summary

| Query | Total count | First-pass interpretation |
| --- | ---: | --- |
| `Thalassemia`, active/recruiting/not-yet-recruiting | 132 | broad active landscape, mixed relevance |
| `Thalassemia`, all statuses | 561 | broad historical registry context |
| `Thalassemia` + `Indonesia`, all statuses | 6 | completed/unknown supportive or observational studies |
| `beta thalassemia` + `gene therapy`, active statuses | 30 | useful but noisy keyword set; curated gene/cell therapy subset needed |
| `beta thalassemia` + `Luspatercept`, active statuses | 9 | transfusion-burden benchmark lane |
| `beta thalassemia` + `Mitapivat`, active statuses | 5 | oral disease-modifying benchmark lane |
| `beta thalassemia` + `Thalidomide`, active statuses | 3 | high-caution HbF / transfusion-reduction lane |
| `beta thalassemia` + iron-axis terms, active statuses | 2 | NTDT iron-overload disease-modifying lane |
| `beta thalassemia` + `Hydroxyurea`, active statuses | 9 | mostly transplant/supportive/adherence contexts in registry |
| `beta thalassemia` + `Sirolimus`, active statuses | 4 | mostly transplant immune-conditioning contexts in registry |

## Active Lane Notes

- Gene/cell therapy records include autologous gene-modified stem-cell
  products, CRISPR/editing follow-up, and long-term safety endpoints, but the
  keyword query also pulls unrelated drug and observational records. This
  supports a curated product map rather than treating all 30 hits as gene
  therapy evidence.
- Mitapivat has active/not-yet-recruiting pediatric phase 3 TDT and NTDT
  records plus active-not-recruiting adult phase 3 records. Its registry
  endpoints map cleanly to hemoglobin response and transfusion reduction.
- Luspatercept active records mostly ask safety, real-world effectiveness,
  transfusion burden, hemoglobin, and ferritin questions.
- Iron-axis records in the active snapshot are NTDT-focused and use liver iron
  concentration by MRI plus safety endpoints. This lane is not a cure lane, but
  it matters for disease modification and overload biology.
- Thalidomide remains visible in active Pakistan records, but it stays
  high-caution because trial activity does not remove known safety barriers.
- Hydroxyurea and sirolimus did not surface as clean standalone active
  thalassemia cure trials in this pass; they remain comparator or context lanes.

## Practical Use For Nakafa Lab

The candidate funnel should require each affordable or natural-product
candidate to declare its closest human benchmark:

- HbF or transfusion-independence benchmark: CRISPR / gene therapy;
- transfusion-burden benchmark: luspatercept;
- oral hemoglobin or transfusion-reduction benchmark: mitapivat;
- low-cost HbF comparator: hydroxyurea;
- iron-overload modifier benchmark: hepcidin/ferroportin/`TMPRSS6` axis;
- high-caution positive-control comparator: thalidomide-class biology.

For a doctor conversation, this snapshot supports asking whether the patient is
medically eligible for any approved disease-modifying drug, transplant/gene
therapy referral discussion, or clinical-trial referral. It does not support
changing transfusion, chelation, immune therapy, supplements, or medicines.

## Sources

- [ClinicalTrials.gov thalassemia search](https://clinicaltrials.gov/search?cond=Thalassemia)
- [ClinicalTrials.gov API about page](https://clinicaltrials.gov/data-api/about-api)
- [Active thalassemia landscape snapshot](../../../data/registries/clinicaltrials/2026-04-27-thalassemia-active-landscape.json)
- [All-status thalassemia landscape snapshot](../../../data/registries/clinicaltrials/2026-04-27-thalassemia-all-status-landscape.json)
- [Indonesia thalassemia snapshot](../../../data/registries/clinicaltrials/2026-04-27-thalassemia-indonesia-all-status-landscape.json)
- [Gene-therapy active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-gene-therapy-beta-thalassemia.json)
- [Gene/cell therapy registry product map](2026-04-27-gene-cell-therapy-registry-product-map.md)
- [Mitapivat active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-mitapivat-beta-thalassemia.json)
- [Luspatercept active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-luspatercept-beta-thalassemia.json)
- [Thalidomide active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-thalidomide-beta-thalassemia.json)
- [Iron-axis active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-iron-axis-beta-thalassemia.json)
- [HbF active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-hbf-beta-thalassemia.json)
- [Hydroxyurea active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-hydroxyurea-beta-thalassemia.json)
- [Sirolimus active snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-sirolimus-beta-thalassemia.json)
