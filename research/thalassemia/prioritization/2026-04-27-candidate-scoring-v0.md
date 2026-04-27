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
This is the biomedical version of the Quran 13:17 benefit-versus-foam
guardrail: noisy signals should not survive scoring just because they look
interesting.

## Initial Scores

These scores prioritize accessible research lanes. Approved or near-curative
high-cost therapies are tracked separately as benchmarks below.

| Lane | Endpoint | Human | Safety | Access | Assay | Weighted | Current use |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Hydroxyurea | 4 | 4 | 3 | 5 | 4 | 3.95 | affordable clinical comparator |
| Sirolimus | 4 | 3 | 2 | 3 | 4 | 3.20 | HbF repurposing hypothesis |
| Epigenetic HbF targets | 5 | 2 | 1 | 2 | 5 | 3.00 | assay-discovery lane only |
| `AMPKB1` / `ULK1` / `NRF2` / autophagy | 4 | 2 | 2 | 2 | 4 | 2.80 | dual HbF and alpha-globin-cleanup target-discovery bridge |
| Hepcidin-ferroportin-`TMPRSS6` | 3 | 3 | 3 | 2 | 3 | 2.85 | iron-axis comparator |
| Thalidomide class | 4 | 3 | 1 | 2 | 3 | 2.75 | high-caution evidence map |
| Curcuminoid analog HbF | 3 | 2 | 2 | 3 | 3 | 2.55 | chemistry-gated screen seed |
| EGCG / green-tea extract | 2 | 3 | 2 | 4 | 3 | 2.65 | adjunct comparator |
| Ginger / 6-shogaol | 1 | 2 | 3 | 3 | 3 | 2.15 | red-cell support hypothesis |
| Propolis | 1 | 1 | 2 | 3 | 2 | 1.60 | low-priority support hypothesis |
| Royal jelly | 1 | 1 | 2 | 3 | 2 | 1.60 | low-priority support hypothesis |
| Melittin / bee venom | 1 | 1 | 0 | 1 | 2 | 0.90 | blocked hazard-first lane |

## Clinical Benchmark Scores

These lanes define what success looks like. Low access scores prevent them from
becoming the main affordability strategy.

| Lane | Endpoint | Human | Safety | Access | Assay | Weighted | Current use |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Luspatercept | 4 | 5 | 3 | 1 | 2 | 3.40 | transfusion-burden benchmark |
| Mitapivat | 4 | 5 | 2 | 1 | 3 | 3.30 | oral disease-modifying benchmark |
| Exa-cel / CRISPR HbF | 5 | 5 | 1 | 0 | 2 | 3.15 | cure-like HbF benchmark |
| Beti-cel / lentiviral beta-globin | 5 | 5 | 1 | 0 | 2 | 3.15 | cure-like gene-addition benchmark |

## Readout

1. Hydroxyurea remains the best affordable comparator because it has direct HbF
   biology, human thalassemia evidence, and realistic access.
2. Sirolimus, `AMPKB1` / `ULK1` / `NRF2` / autophagy, thalidomide-class drugs,
   and epigenetic targets are useful for mechanism discovery but have safety or
   translation blockers.
3. Curcuminoid analogs are not ordinary turmeric/curcumin claims; they require
   exact compound identity and hemolysis gating.
4. EGCG, ginger, propolis, and royal jelly are adjunct/support lanes unless
   future evidence shows HbF or transfusion-burden effects.
5. Melittin/bee venom is blocked from therapeutic framing because the safety
   score is `0`.
6. Gene and cell therapies are the strongest proof that transfusion
   independence is biologically possible, but access and conditioning barriers
   keep them as benchmarks rather than the affordable discovery path.

## Promotion Rule

A lane can move upward only if it improves at least one field without worsening
safety:

- human thalassemia evidence with numeric outcomes;
- stronger endpoint fit such as HbF protein, transfusion interval, or
  pre-transfusion hemoglobin;
- defined chemistry identity and batch control;
- successful hemolysis and viability screens;
- clinician or domain-expert review.

HbF-related lanes also need responder context from
[HbF responder signature V0](2026-04-27-hbf-responder-signature-v0.md), because
the same candidate can look different across `TDT`, `NTDT`,
HbE/beta-thalassemia, baseline HbF, and HbF modifier backgrounds.

For HbF candidates, add the
[HPFH-like signature V0](2026-04-27-hpfh-like-signature-v0.md) label before
promotion. `hpfh_like` can move a candidate upward; `stress_hbf`,
`reporter_only`, or `blocked` overrides the weighted score.

The first applied label map is
[HPFH-like candidate labels V0](2026-04-27-hpfh-like-candidate-labels-v0.md).
The key result is that current small-molecule and natural-product candidates
are still `partial_hbf`, `reporter_only`, `not_hbf_lane`, or `blocked`; only
gene-editing and natural HPFH biology count as true `hpfh_like` benchmarks.

## Linked Evidence

- [Candidate ranking](2026-04-26-candidate-ranking.md)
- [HbF responder signature V0](2026-04-27-hbf-responder-signature-v0.md)
- [HPFH-like signature V0](2026-04-27-hpfh-like-signature-v0.md)
- [HPFH-like candidate labels V0](2026-04-27-hpfh-like-candidate-labels-v0.md)
- [Top clinical lanes numeric extraction](../findings/2026-04-27-top-clinical-lanes-numeric-extraction.md)
- [AMPKB1 autophagy HbF bridge](../findings/2026-04-27-ampkb1-autophagy-hbf-bridge.md)
- [Pyruvate kinase red-cell metabolism benchmark](../findings/2026-04-27-pyruvate-kinase-red-cell-metabolism-benchmark.md)
- [Candidate score sensitivity notebook](../notebooks/2026-04-27-candidate-score-sensitivity.ipynb)
- [AI-assisted cancer vaccine method](../findings/2026-04-27-ai-assisted-cancer-vaccine-method.md)
- [Epigenetic HbF screen V0](../assays/2026-04-27-epigenetic-hbf-screen-v0.md)
- [Hepcidin-ferroportin iron-restriction axis](../findings/2026-04-27-hepcidin-ferroportin-iron-restriction-axis.md)
- [Ar-Ra'd 13:17 benefit-versus-foam guardrail](../../islamic/quran/013-ar-rad/017.md)
