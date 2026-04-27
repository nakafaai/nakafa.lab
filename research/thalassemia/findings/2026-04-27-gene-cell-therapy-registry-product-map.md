# Finding: Gene And Cell Therapy Registry Product Map

Date checked: 2026-04-27
Scope: ClinicalTrials.gov registry curation, not treatment advice

## Working Conclusion

The active `gene therapy` keyword snapshot is useful but noisy. It contains 30
records, but not all of them are gene or cell therapy records. After curation,
the useful signal is that beta-thalassemia cure-like development is clustering
around two validated mechanisms:

- add or restore beta-globin capacity in autologous hematopoietic stem cells;
- reactivate fetal hemoglobin by editing or suppressing HbF repressors such as
  `BCL11A`.

This strengthens the Nakafa Lab benchmark rule: an affordable discovery
candidate must explain whether it is trying to imitate beta-globin restoration,
HbF reactivation, erythroid maturation, red-cell survival, or iron-burden
modification.

## Curated Product/Mechanism Map

| Class | Registry examples | Endpoint pattern |
| --- | --- | --- |
| Beta-globin addition/restoration | `KL003`, vebeglogene autotemcel, `ALS20`, `LentiRed`, `OTL-300` / `TNS9.3.55`, beta-globin restored autologous HSCs, betibeglogene follow-up | transfusion independence, Hb at least 9 g/dL without transfusion, engraftment, vector safety |
| HbF reactivation / editing | `CTX001`, `EDIT-301`, `CS-101`, `YOLT-204`, `VGB-Ex01`, BCL11A-enhancer Cas9 RNP, BCL11A shRNA gene-transfer records | HbF, total Hb, transfusion independence or reduction, engraftment, clonal and malignancy monitoring |
| Transplant and conditioning systems | `Supergraft`, alpha/beta T-cell depletion, reduced-intensity or alternative-donor transplant records | donor chimerism, GVHD, engraftment, transplant mortality |
| Registry noise to keep out of gene-therapy claims | thalidomide, hydroxyurea, PUM1 expression, microRNA-155, panobinostat, mitapivat, stakeholder survey records | useful elsewhere only if separately justified |

## Evidence Hygiene

The registry is not enough to claim mechanism, efficacy, or access. Product
names, titles, interventions, and primary outcomes are registry metadata. Each
lane still needs peer-reviewed outcome extraction, protocol review, and expert
interpretation before it becomes a benchmark in the paper.

The most useful translational readouts for Nakafa Lab are:

- transfusion independence duration;
- transfusion reduction duration;
- total hemoglobin and HbF;
- engraftment and chimerism;
- insertional oncogenesis or clonal dominance monitoring;
- transplant-related mortality and GVHD;
- long-term follow-up duration;
- age range and eligibility constraints.

## Implication For Doctor Questions

For `case-001`, this product map only supports asking a hematologist whether
advanced therapy or trial referral is medically relevant. It does not support
choosing or changing treatment. The minimum information needed before such a
conversation remains subtype, genotype, HbF/HPLC, iron burden, immune antibody
status, organ status, and transfusion burden.

## Sources

- [Active gene-therapy keyword snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-gene-therapy-beta-thalassemia.json)
- [Active HbF keyword snapshot](../../../data/registries/clinicaltrials/2026-04-27-active-hbf-beta-thalassemia.json)
- [ClinicalTrials.gov NCT06647979](https://clinicaltrials.gov/study/NCT06647979)
- [Current clinical trial landscape](2026-04-27-current-clinical-trial-landscape.md)
- [Gene therapy access frontier](2026-04-27-gene-therapy-access-frontier.md)
