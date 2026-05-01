# Finding: No-Lab Execution Ladder

Date checked: 2026-04-29
Evidence label: no-lab execution gate, not treatment advice

## Direct Answer

Without a lab partner, Nakafa Lab cannot prove a new cure or validate a new
candidate. The highest-value no-lab work is still actionable:

> build a specialist-readable packet, quantify the current clinical blockers,
> refresh standard-care and referral gates, and reject weak candidate claims
> before money is spent.

This is not a retreat from cure-oriented research. It is the fastest way to
avoid false hope, false rejection, and bad lab spending.

## Ranked No-Lab Ladder

| Rank | Action | Why it comes first | Output |
| --- | --- | --- | --- |
| 1 | Minimum hematologist packet | Case relevance is blocked until subtype, transfusion, immune, iron, organ, and access records are organized. | One doctor-readable packet with current labels and missing records. |
| 2 | Private record index | Raw records are useful only if they are indexed without leaking identifiers into the public repo. | Ignored `private/<case-code>/` index and extraction worksheets. |
| 3 | Transfusion-burden calculation | Weekly transfusion is not interpretable without `ml/kg/year`, pure red-cell volume, Hb increment, and iron input. | De-identified calculation from private logs. |
| 4 | Iron/chelation organ-risk packet | Ferritin alone is not enough to judge organ risk or chelation context. | Ferritin trend, LIC MRI, cardiac `T2*`, chelator identity, toxicity monitoring, and organ screen. |
| 5 | Immune and blood-bank packet | High transfusion burden can be amplified by alloimmunization, autoantibodies, DAT positivity, matching issues, or shortened donor RBC survival. | Antibody screen, named antibodies, DAT specificity, matching policy, phenotype/genotype, reactions, and hemolysis workup. |
| 6 | Advanced-therapy referral readiness | HSCT, gene therapy, CRISPR therapy, luspatercept, mitapivat, hydroxyurea, and trials are real categories, but eligibility cannot be inferred by the repo. | Specialist-screening readiness label, not an eligibility claim. |
| 7 | Registry and guideline refresh | Active trials and approvals can change quickly. | Updated benchmark map and doctor-facing questions. |
| 8 | Computational candidate rerank | Dry-lab ranking can reject bad ideas, but cannot prove benefit. | Candidate labels such as `hold`, `benchmark_only`, `novelty_blocked`, or `lab_quote_ready`. |
| 9 | Lab quote package | Useful only after the first packet and benchmark gates are stable. | Small assay package with controls and stop rules. |
| 10 | New candidate claim | Lowest priority without lab evidence and clinician context. | Keep blocked. |

## Why This Is The Strongest No-Lab Path

The current evidence map says several existing options are real categories:
HSCT, gene addition, gene editing, luspatercept, mitapivat, hydroxyurea, and
clinical trials. But each option depends on subtype, transfusion burden, immune
risk, organ risk, monitoring capacity, and access. A repo cannot safely decide
those. A hematologist can only screen them well if the record packet is legible.

Therefore, the no-lab work should answer:

1. What is the exact diagnosis and molecular context?
2. Why is transfusion weekly: disease severity, volume policy, poor increment,
   immune loss, spleen context, or another factor?
3. What is the iron and organ-risk status?
4. Are existing therapies or referral pathways screenable, blocked, or still
   data-missing?
5. Which future lab assays would answer a real unresolved question?

## Operational Rules

- Do not add raw records, exact identifiers, local paths, contact details, or
  patient-specific treatment instructions to the public repo.
- Keep filled private worksheets under ignored `private/` paths.
- Convert private facts into public material only through the release
  checklist and de-identified extraction template.
- Write doctor-facing material as questions and record requests, not treatment
  requests.
- Treat Quran 16:43 and 55:7-9 as ethical-method anchors for expert
  consultation and measurement, not biomedical evidence for any therapy.

## Current Decision

Current label: `no_lab_execution_ladder_active`.

Case-001 remains:

- `patient_relevance_blocked`;
- `phenotype_only`;
- `transfusion_dependent_burden_unquantified`;
- `immune_transfusion_packet_missing`;
- `iron_packet_missing`;
- `advanced_therapy_referral_packet_missing`.

The next public-safe output is not a new therapy claim. It is a cleaner packet
and action log that a hematologist can review.

## Sources

- [No-lab research lane](2026-04-27-no-lab-research-lane.md)
- [Case-001 minimum hematologist packet](../case-context/case-001-minimum-hematologist-packet.md)
- [Case-001 minimum hematologist packet gate](2026-04-28-case001-minimum-hematologist-packet-gate.md)
- [Case-001 advanced therapy referral readiness gate](2026-04-28-case001-advanced-therapy-referral-readiness-gate.md)
- [Private case intake threat model](../../../docs/private-case-intake-threat-model.md)
- [TIF 2025 TDT guideline](https://www.ncbi.nlm.nih.gov/books/NBK614251/)
- [TIF 2025 blood transfusion chapter](https://www.ncbi.nlm.nih.gov/books/NBK614240/)
- [TIF 2025 iron overload chapter](https://www.ncbi.nlm.nih.gov/books/NBK614244/)
- [TIF 2025 monitoring recommendations](https://www.ncbi.nlm.nih.gov/books/NBK614248/)
- [GeneReviews beta-thalassemia](https://www.ncbi.nlm.nih.gov/books/NBK1426/)
- [FDA Casgevy](https://www.fda.gov/vaccines-blood-biologics/casgevy)
- [FDA Zynteglo](https://www.fda.gov/vaccines-blood-biologics/zynteglo)
- [FDA Aqvesme / mitapivat approval](https://www.fda.gov/drugs/news-events-human-drugs/fda-approves-first-oral-treatment-anemia-thalassemia-inherited-blood-disorder)
- [NICE exagamglogene autotemcel appraisal](https://www.ncbi.nlm.nih.gov/books/NBK610907/)
- [Quran 16:43 expert-consultation anchor](../../islamic/quran/016-an-nahl/043.md)
- [Quran 55:7-9 mizan anchor](../../islamic/quran/055-ar-rahman/007-009.md)
- [No-lab execution ladder notebook](../notebooks/2026-04-29-no-lab-execution-ladder.ipynb)
