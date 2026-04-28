# Finding: China HbF Editing Proximity Gate

Date checked: 2026-04-27
Evidence label: trial-proximity audit, not treatment advice

## Direct Answer

China has at least one registered trial that is closer to the Nakafa Lab
mechanism than the previous Asia/Russia audit made explicit.

The key record is `NCT06041620` for `VGB-Ex01`, an autologous CRISPR-Cas12b
edited hematopoietic stem-cell intervention for transfusion-dependent
beta-thalassemia. Its registry description explicitly routes through `HBG1/2`
promoter editing, gamma-globin / HbF induction, reduced uncompounded
alpha-globin chain burden, improved red-cell survival, reduced hemolysis, and
reduced transfusion need.

That means:

- the integrated `HbF + alpha-chain burden + hemolysis` concept is not fully
  new as a broad therapeutic idea;
- Nakafa Lab's remaining novelty should be framed more narrowly as a non-editing
  or affordability-first discovery and validation program;
- any lab pitch must avoid saying that no one has connected HbF rescue with
  alpha-globin burden or hemolysis.

## Closest China Records

| Record | Why it matters | Boundary |
| --- | --- | --- |
| `NCT06041620` / `VGB-Ex01` | CRISPR-Cas12b edited HSCs for TDT. The record links `HBG1/2` promoter editing to HbF, alpha-chain burden, red-cell survival, hemolysis, and transfusion need. | Very close mechanistically, but it is ex vivo HSC gene editing with transplant-style infrastructure and long follow-up, not an affordable small-molecule or natural-product screen. |
| `NCT06678165` / `YOLT-204` | TDT-specific YOLT-204 pilot record with safety, laboratory, sustained transfusion-reduction, and 3-month transfusion-independence primary endpoints. | High-interest China registry watchlist record, but not yet recruiting in the compact source pass and no posted results. |
| `NCT07190001` / `YOLT-204` | Hemoglobinopathy trial with sustained HbF >=20%, transfusion reduction, HbF concentration, intended-modification, and F-cell proportion outcomes. | Registry condition includes TDT and SCD, but eligibility text is heavily SCD-genotype oriented in this snapshot. Track separately from the TDT-specific YOLT-204 record. |
| `NCT07338344` / luspatercept plus low-dose thalidomide | Randomized China phase 2 trial in adult beta-TDT with transfusion-burden, HbF, gamma-globin, hemolysis indices, iron deposition, and safety readouts. | Clinically important pharmacologic combination, but not a cure claim and not a new Nakafa candidate. Luspatercept access/cost and thalidomide safety remain major boundaries. |

## What This Changes

Before this audit, the working novelty statement was:

> The full integrated package is underanswered.

That still holds for affordable non-editing discovery, but it needs sharper
wording:

> China already has gene-editing trials that approach the integrated HbF,
> alpha-chain, hemolysis, and transfusion-reduction logic. Nakafa Lab's practical
> gap is to test whether a cheaper, monitorable, non-editing candidate can pass
> similar multi-endpoint gates before any clinical claim is made.

This is a better claim. It is harder to attack because it admits the closest
existing work.

## Lab-Pitch Wording

Do not say:

> "Nobody has integrated HbF with alpha-globin and hemolysis."

Say:

> "The integrated gene-editing direction already exists. Nakafa Lab wants to
> build an affordability-first screen that asks whether any non-editing
> candidate can approximate useful HbF/F-cell rescue while also passing
> alpha-globin burden, autophagy, maturation, viability, and mature red-cell
> hemolysis gates."

## Practical Consequences

1. Use `VGB-Ex01` as a benchmark, not as a patient recommendation.
2. Add a competitor gate for any future claim of novelty:
   "Does this idea differ from active HBG promoter editing trials?"
3. Keep the first wet-lab request focused on non-editing candidates and
   measurable safety gates.
4. Add `HBG1/2 promoter editing`, `HbF >=20%`, F-cell percentage, alpha-chain
   burden, and hemolysis to the benchmark terms used in future searches.
5. Do not collapse the two YOLT-204 records. Treat `NCT06678165` as the
   TDT-specific registry watchlist record and `NCT07190001` as a mixed
   hemoglobinopathy/SCD-leaning HbF/F-cell endpoint record.

## Public-Repo Handling

The detail snapshots saved for this audit are compact redacted records. Contact
names, phone numbers, email addresses, facility-level coordinates, and
location-level contacts were intentionally excluded before committing.

## Sources

- [ClinicalTrials.gov NCT06041620, VGB-Ex01](https://clinicaltrials.gov/study/NCT06041620)
- [ClinicalTrials.gov NCT06678165, YOLT-204 TDT pilot](https://clinicaltrials.gov/study/NCT06678165)
- [ClinicalTrials.gov NCT07190001, YOLT-204](https://clinicaltrials.gov/study/NCT07190001)
- [ClinicalTrials.gov NCT07338344, luspatercept plus low-dose thalidomide](https://clinicaltrials.gov/study/NCT07338344)
- [`NCT06041620` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct06041620-vgb-ex01-detail.json)
- [`NCT06678165` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-28-nct06678165-yolt204-tdt-detail.json)
- [`NCT07190001` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct07190001-yolt204-detail.json)
- [`NCT07338344` compact detail snapshot](../../../data/registries/clinicaltrials/2026-04-27-nct07338344-luspatercept-thalidomide-detail.json)
