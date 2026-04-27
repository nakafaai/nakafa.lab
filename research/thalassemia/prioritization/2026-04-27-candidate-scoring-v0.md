# Candidate Scoring V0

Date: 2026-04-27
Scope: research prioritization, not treatment advice

## Purpose

This file turns the current candidate ranking into a small scoring model. The
goal is to make assumptions visible before Nakafa Lab spends time on a candidate
lane.

Scores are provisional. They should be updated when numeric effect sizes,
patient genotype, safety details, or assay results are added.

## Score Fields

Each field is scored from `0` to `5`.

| Field | Meaning |
| --- | --- |
| Endpoint fit | How directly the lane maps to HbF, globin balance, transfusion burden, red-cell survival, or iron burden |
| Human evidence | Human thalassemia evidence strength, not generic biology |
| Safety | Higher means more monitorable; lower means higher toxicity or uncertainty |
| Access | Cost, availability, and realistic Indonesian access |
| Assay readiness | How easy it is to test with HbF, hemolysis, erythroid, or iron-axis assays |

Weighted score:

```text
0.30 endpoint + 0.25 human evidence + 0.20 safety + 0.15 access + 0.10 assay
```

Hard blockers override the score. A candidate with major safety or identity
uncertainty cannot be promoted just because the weighted score looks acceptable.

## Initial Scores

| Lane | Endpoint | Human | Safety | Access | Assay | Weighted | Current use |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Hydroxyurea | 4 | 4 | 3 | 5 | 4 | 3.95 | affordable clinical comparator |
| Sirolimus | 4 | 3 | 2 | 3 | 4 | 3.20 | HbF repurposing hypothesis |
| Epigenetic HbF targets | 5 | 2 | 1 | 2 | 5 | 3.00 | assay-discovery lane only |
| Hepcidin-ferroportin-`TMPRSS6` | 3 | 3 | 3 | 2 | 3 | 2.85 | iron-axis comparator |
| Thalidomide class | 4 | 3 | 1 | 2 | 3 | 2.75 | high-caution evidence map |
| Curcuminoid analog HbF | 3 | 2 | 2 | 3 | 3 | 2.55 | chemistry-gated screen seed |
| EGCG / green-tea extract | 2 | 3 | 2 | 4 | 3 | 2.65 | adjunct comparator |
| Ginger / 6-shogaol | 1 | 2 | 3 | 3 | 3 | 2.15 | red-cell support hypothesis |
| Propolis | 1 | 1 | 2 | 3 | 2 | 1.60 | low-priority support hypothesis |
| Royal jelly | 1 | 1 | 2 | 3 | 2 | 1.60 | low-priority support hypothesis |
| Melittin / bee venom | 1 | 1 | 0 | 1 | 2 | 0.90 | blocked hazard-first lane |

## Readout

1. Hydroxyurea remains the best affordable comparator because it has direct HbF
   biology, human thalassemia evidence, and realistic access.
2. Sirolimus, thalidomide-class drugs, and epigenetic targets are useful for
   mechanism discovery but have safety or translation blockers.
3. Curcuminoid analogs are not ordinary turmeric/curcumin claims; they require
   exact compound identity and hemolysis gating.
4. EGCG, ginger, propolis, and royal jelly are adjunct/support lanes unless
   future evidence shows HbF or transfusion-burden effects.
5. Melittin/bee venom is blocked from therapeutic framing because the safety
   score is `0`.

## Promotion Rule

A lane can move upward only if it improves at least one field without worsening
safety:

- human thalassemia evidence with numeric outcomes;
- stronger endpoint fit such as HbF protein, transfusion interval, or
  pre-transfusion hemoglobin;
- defined chemistry identity and batch control;
- successful hemolysis and viability screens;
- clinician or domain-expert review.

## Linked Evidence

- [Candidate ranking](2026-04-26-candidate-ranking.md)
- [AI-assisted cancer vaccine method](../findings/2026-04-27-ai-assisted-cancer-vaccine-method.md)
- [Epigenetic HbF screen V0](../assays/2026-04-27-epigenetic-hbf-screen-v0.md)
- [Hepcidin-ferroportin iron-restriction axis](../findings/2026-04-27-hepcidin-ferroportin-iron-restriction-axis.md)
