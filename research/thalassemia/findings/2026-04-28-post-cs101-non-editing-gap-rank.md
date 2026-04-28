# Finding: Post-CS-101 Non-Editing Gap Rank

Date checked: 2026-04-28
Evidence label: computational triage, not wet-lab evidence and not treatment advice

## Direct Answer

After `CS-101`, especially after the `NCT07489196` phase 2 registry escalation,
the strongest next Nakafa Lab lane is not "find any HbF inducer." That is too
weak, because `CS-101` and `VGB-Ex01` already make HbF-restoring editing a
close benchmark.

The best remaining no-lab-to-lab bridge is:

> keep hydroxyurea and sirolimus as comparators, and add PF-06409577 /
> `PRKAB1`-AMPK beta1 only as an expansion assay probe if a qualified lab can
> document material identity and measure HbF plus alpha-globin/autophagy,
> maturation, viability, and hemolysis.

This is not a patient-use recommendation. It is a lab-planning decision.

## Why This Was Needed

The CS-101 benchmark changes the ranking logic. A candidate is not useful just
because it raises HbF. It now has to answer:

- is it cheaper or lower-infrastructure than autologous HSC editing?
- is it safer or more monitorable than high-caution epigenetic or thalidomide
  biology?
- can it be tested in the same run for HbF/F-cells, alpha-globin burden or
  autophagy, erythroid maturation, viability, apoptosis, and mature red-cell
  hemolysis?

## Notebook Result

The notebook
[`2026-04-28-post-cs101-non-editing-gap-rank.ipynb`](../notebooks/2026-04-28-post-cs101-non-editing-gap-rank.ipynb)
re-ranks the current lanes after applying benchmark, safety, and infrastructure
penalties.

| Lane | Current role after CS-101 | Decision |
| --- | --- | --- |
| Hydroxyurea | Affordable positive HbF comparator | Keep in first lab panel, not a new discovery claim. |
| Sirolimus | Autophagy and alpha-globin-cleanup comparator | Keep as comparator if immune/drug-monitoring boundary is clear. |
| PF-06409577 / `PRKAB1`-AMPK beta1 | First expansion assay probe | Promote only as assay biology, not treatment advice. |
| `T-BDMC`-like curcuminoid analog | Identity-gated screen seed | Keep conditional until exact compound identity, source, purity, and hemolysis gate are solved. |
| LSD1 / DNMT1 epigenetic HbF targets | High-caution target class | Assay-only benchmark; do not pitch as affordable treatment. |
| CRBN / WIZ / IKZF degrader class | High-caution HbF comparator | Benchmark only because of drug-class safety and access barriers. |
| Luspatercept plus low-dose thalidomide | Closest non-editing pharmacologic benchmark | Comparator only; not Nakafa discovery. |
| CS-101 / VGB-Ex01 editing | Strongest editing benchmark set | Comparator only; blocks weak HbF novelty claims. |

## Operational Decision

Do not expand the first lab quote into many candidate materials.

Keep the first quote panel stable:

- hydroxyurea;
- resveratrol;
- sirolimus;
- standardized 6-shogaol-rich ginger extract;
- melittin hazard control.

If the lab can add one expansion lane, ask about PF-06409577 / `PRKAB1`-AMPK
beta1 with exact identity and dual-readout support. If the lab cannot support
that, keep the expansion lane out rather than replacing it with vague
natural-product claims.

## Boundary

This ranking is a computational triage artifact. It does not show efficacy,
safety, dosing, eligibility, or clinical relevance for any patient.

## Sources

- [Post-CS-101 non-editing gap-rank notebook](../notebooks/2026-04-28-post-cs101-non-editing-gap-rank.ipynb)
- [CS-101 base-editing benchmark](2026-04-28-cs101-base-editing-benchmark.md)
- [CS-101 phase 2 escalation gate](2026-04-28-cs101-phase2-escalation-gate.md)
- [Proximity novelty gate V0](../prioritization/2026-04-28-proximity-novelty-gate-v0.md)
- [Candidate scoring V0](../prioritization/2026-04-27-candidate-scoring-v0.md)
- [First lab quote brief V0](../assays/2026-04-27-first-lab-quote-brief-v0.md)
- [AMPKB1 autophagy HbF bridge](2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [PF-06409577 probe material gate](2026-04-27-pf-06409577-probe-material-gate.md)
- [T-BDMC identity resolution](2026-04-27-t-bdmc-identity-resolution.md)
