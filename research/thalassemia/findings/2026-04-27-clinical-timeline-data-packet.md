# Clinical Timeline Data Packet

Date: 2026-04-27
Status: no-lab workflow, not treatment advice

## Bottom Line

The highest-value no-lab work is to turn medical records into a de-identified,
source-linked timeline. This lets Nakafa Lab and a hematologist distinguish
three different problems that can look similar from the outside:

- severe beta-globin production failure;
- poor red-cell survival from immune, spleen, or transfusion factors;
- iron/organ-risk or chelation problems.

Without that timeline, every candidate ranking stays weak because the repo does
not know which blocker it is trying to solve.

## What To Build

Use two public-safe templates:

- [clinical record index template](../../../templates/clinical-record-index-template.csv);
- [case clinical timeline template](../../../templates/case-clinical-timeline-template.csv).

The record index tracks which de-identified records exist. The timeline tracks
events extracted from those records.

Do not put names, exact birth dates, hospital IDs, addresses, phone numbers,
photos, or medical-record numbers in either file.

## Timeline Event Types

Use these event types first:

- `diagnosis`;
- `hplc_or_electrophoresis`;
- `genetic_test`;
- `transfusion`;
- `pre_transfusion_hb`;
- `post_transfusion_hb`;
- `antibody_screen`;
- `dat_direct_coombs`;
- `transfusion_reaction`;
- `ferritin`;
- `liver_iron_mri`;
- `cardiac_t2star`;
- `chelation`;
- `chelation_toxicity_monitoring`;
- `spleen`;
- `endocrine`;
- `liver`;
- `kidney`;
- `bone`;
- `autoimmune`;
- `therapy_review`;
- `trial_or_referral_review`.

## Routing Labels

Use existing repo labels rather than inventing new ones:

- genotype labels: `untyped`, `phenotype_only`, `hbb_confirmed`,
  `hbb_hba_confirmed`, `modifier_context_known`;
- transfusion labels: `high_annual_volume`, `weekly_low_volume`,
  `low_hb_increment`, `reaction_history`, `red_cell_survival_unknown`;
- immune labels: `antibody_unknown`, `alloantibody_present`,
  `dat_unknown`, `dat_positive`, `aiha_possible`;
- iron labels: `iron_packet_missing`, `ferritin_trend_only`, `lic_known`,
  `cardiac_t2star_known`, `organ_screen_incomplete`,
  `chelation_review_needed`, `toxicity_review_needed`,
  `specialist_managed`;
- access labels: `not_yet_evaluated`, `data_missing`,
  `medically_unsuitable`, `access_blocked`, `trial_or_referral_candidate`,
  `under_specialist_review`.

## Scripted Summary

The timeline can be summarized without exposing patient identity:

```bash
uv run python scripts/summarize_case_timeline.py <deidentified-timeline.csv>
```

Use a copied, de-identified working CSV when real records arrive. Do not commit
private case data unless it is explicitly de-identified and public-safe.

The script checks:

- required columns exist;
- obvious identifier columns are not present;
- `event_date` sorting anchors use `YYYY-MM-DD`;
- `event_time_precision` is `year`, `month`, `relative`, `unknown`, or `day`;
- day-level dates are rejected unless `--private-input` is used for ignored
  private timelines;
- event types and routing labels are countable.

## Research Consequence

This is a dry-lab experiment in evidence organization. It can reveal whether
the next useful work is:

- genotype-first review;
- transfusion-burden calculation;
- immune/transfusion complication review;
- iron-overload organ-risk review;
- existing curative/disease-modifying eligibility review;
- computational candidate ranking.

It still cannot prove a new drug works. It can make the next lab or clinician
conversation much sharper.

## Sources

- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [Beta-Thalassemia GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [No-lab research lane](2026-04-27-no-lab-research-lane.md)
- [Case-001 research routing matrix](../case-context/case-001-research-routing-v0.md)
- [Case-001 genotype-first intake gate](../case-context/case-001-genotype-first-intake-gate-v0.md)
- [Iron overload organ-risk gate](2026-04-27-iron-overload-organ-risk-gate.md)
