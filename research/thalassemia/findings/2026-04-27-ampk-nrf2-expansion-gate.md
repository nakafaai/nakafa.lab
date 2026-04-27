# Finding: AMPK/NRF2 Expansion Gate

Date checked: 2026-04-27
Evidence label: computational evidence gate, not wet-lab evidence and not treatment advice

## Working Conclusion

`AMPKB1` / `NRF2` remains worth testing as an expansion lane, but only as a
qualified-lab pathway probe.

It should not be promoted as a patient candidate. The new gating pass found a
useful warning: metformin has HbF-related literature and a K562 signal, but the
retrieved human NTDT study reported no extra benefit when added to stable
hydroxyurea. That makes metformin a translational caution signal, not a lead.

## Gate Result

| Item | Gate label | Meaning |
| --- | --- | --- |
| selective `AMPKB1` / PF-06409577-style probe | `assay_probe_only` | useful if a lab can source a defined research-grade probe and run dual HbF plus alpha-globin/autophagy readouts |
| metformin | `negative_or_low_priority_comparator` | human NTDT signal does not support promotion; useful mainly as a caution against generic AMPK claims |
| generic `NRF2` activation | `mechanism_context_only` | broad stress-response biology must not be treated as therapy without a defined probe and safety gates |

## Why Metformin Matters Here

Metformin is not being proposed as treatment.

It matters because it falsifies an easy but unsafe assumption: if an AMPK-linked
drug can affect fetal-globin biology in vitro, it does not automatically produce
a useful clinical thalassemia effect. The retrieved PubMed snapshot includes:

- a 2024 NTDT study in which metformin added to stable hydroxyurea did not yield
  extra benefit;
- a 2025 K562 cell-line paper on hydroxyurea and metformin fetal-globin
  induction.

That contrast strengthens the repo rule: K562 and pathway signals are not enough
for patient-facing promotion.

## Assay Requirement

If a lab can add an `AMPKB1` / `NRF2` probe, require:

- exact compound identity and batch documentation;
- `HBG1` / `HBG2` messenger RNA;
- HbF protein and F-cell percentage;
- `NRF2` target activation context;
- phospho-`ULK1` or `ULK1` state;
- p62 / `SQSTM1` state;
- alpha/non-alpha globin balance;
- free or insoluble alpha-globin;
- erythroid maturation;
- viability and apoptosis;
- mature red-cell hemolysis.

## Reject Or Hold Conditions

Reject or hold this lane if:

- the evidence is K562-only;
- the signal is only broad oxidative stress or antioxidant activity;
- alpha-globin burden is not measured;
- maturation or viability worsens;
- mature red-cell hemolysis worsens;
- the compound identity, supplier, or batch cannot be verified;
- the proposed item is framed as patient treatment instead of assay biology.

## Research Decision

Keep `AMPKB1` / `NRF2` in the expansion panel as an `assay_probe_only` lane.

Keep metformin as a `negative_or_low_priority_comparator` and translational
warning. Do not add it to the first quote panel unless a lab specifically wants
it as a low-priority comparator.

## Sources

- [AMPK/NRF2 expansion gate notebook](../notebooks/2026-04-27-ampk-nrf2-expansion-gate.ipynb)
- [Metformin HbF thalassemia PubMed snapshot](../../../data/literature/pubmed/2026-04-27-metformin-hbf-thalassemia-search.json)
- [AMPKB1 NRF2 ULK1 HbF refresh snapshot](../../../data/literature/pubmed/2026-04-27-ampkb1-nrf2-ulk1-hbf-refresh.json)
- [NRF2 HbF beta-thalassemia PubMed snapshot](../../../data/literature/pubmed/2026-04-27-nrf2-hbf-beta-thalassemia-search.json)
- [PF-06409577 AMPK PubMed snapshot](../../../data/literature/pubmed/2026-04-27-pf-06409577-ampk-search.json)
- [Metformin NTDT article, PMID 38312174](https://pubmed.ncbi.nlm.nih.gov/38312174/)
- [Hydroxyurea and metformin K562 article, PMID 40200166](https://pubmed.ncbi.nlm.nih.gov/40200166/)
- [NRF2 fetal hemoglobin article, PMID 21464371](https://pubmed.ncbi.nlm.nih.gov/21464371/)
- [Selective AMPKB1 HbF article, PMID 41259521](https://pubmed.ncbi.nlm.nih.gov/41259521/)
