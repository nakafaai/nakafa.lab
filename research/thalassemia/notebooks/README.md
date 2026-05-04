# Research Notebooks

This folder stores small reproducible experiments that are easier to inspect as
notebooks than as prose-only notes.

Rules:

- keep notebooks source-backed and small;
- do not commit private patient data or raw clinical records;
- clear large outputs before commit;
- move durable conclusions into `findings/`, `prioritization/`, or the paper;
- run the notebook top-to-bottom when the environment allows.

Current notebooks:

- `2026-04-27-ahsp-buffer-gate.ipynb` - computational evidence gate that keeps
  `AHSP` as an optional alpha-globin-buffer readout, not a standalone therapy
  lead.
- `2026-04-27-alpha-globin-rebalancing-gate.ipynb` - computational evidence
  gate that promotes direct alpha-globin reduction as a chain-balance benchmark
  and assay gate, not a first affordable treatment lead.
- `2026-04-27-ampk-nrf2-expansion-gate.ipynb` - computational evidence gate
  for the `AMPKB1` / `NRF2` expansion lane, including metformin as a
  translational warning comparator.
- `2026-04-27-candidate-score-sensitivity.ipynb` - stress test for the first
  candidate scoring table.
- `2026-04-27-delta-globin-hba2-gate.ipynb` - computational evidence gate that
  keeps `HBD` / delta-globin / HbA2 induction as an advanced compensation
  benchmark and assay expansion gate, not a first treatment lead.
- `2026-04-27-dual-readout-panel-prioritizer.ipynb` - computational experiment
  that re-checks the first lab-quote panel against dual HbF plus
  alpha-globin/autophagy readouts.
- `2026-04-27-expansion-lane-decision-gate.ipynb` - computational evidence
  gate that ranks expansion lanes after the fixed quote panel and promotes
  `AMPKB1` / `NRF2` / `ULK1` / autophagy as assay-probe biology, not treatment
  advice.
- `2026-04-27-pf-06409577-probe-material-gate.ipynb` - computational material
  gate that pins the `AMPKB1` expansion lane to exact PF-06409577 identity,
  ChEMBL activity, and PubMed bridge evidence while blocking patient-use
  framing.
- `2026-04-28-post-cs101-non-editing-gap-rank.ipynb` - computational pressure
  test after `CS-101`, keeping editing and luspatercept plus thalidomide as
  benchmarks while preserving PF-06409577 as the first expansion assay probe.
- `2026-04-28-case001-high-hbf-genotype-evidence-gap.ipynb` - de-identified
  case gate that ranks missing `HBB`, `HBA1/HBA2`, and HPFH/HBG-modifier
  records before interpreting historical high HbF.
- `2026-04-28-case001-molecular-test-escalation-gate.ipynb` - de-identified
  case gate that turns the `phenotype_only` label into a ranked molecular-
  record request sequence.
- `2026-04-28-case001-transfusion-burden-quantification-gate.ipynb` -
  de-identified case gate that keeps weekly transfusion as
  `transfusion_dependent_burden_unquantified` until annual volume, pure red-cell
  volume, Hb response, and iron input are quantified.
- `2026-04-28-case001-immune-transfusion-record-gate.ipynb` - de-identified
  case gate that ranks missing antibody, DAT, matching, reaction, spleen, and
  transfusion volume records before interpreting weekly transfusion.
- `2026-04-28-case001-iron-chelation-organ-risk-record-gate.ipynb` -
  de-identified case gate that ranks missing ferritin trend, LIC, cardiac
  `T2*`, chelation, toxicity, and organ-risk records.
- `2026-04-28-case001-minimum-hematologist-packet-gate.ipynb` -
  de-identified integration gate that ranks the minimum doctor packet across
  diagnosis, transfusion burden, immune, iron, organ, and referral records.
- `2026-04-28-case001-advanced-therapy-referral-readiness-gate.ipynb` -
  de-identified gate that keeps HSCT, gene-cell therapy, disease-modifying
  drugs, and trials as specialist-screening questions until the referral packet
  is complete enough for clinician review.
- `2026-05-02-case001-doctor-response-triage-gate.ipynb` - de-identified
  triage gate that maps doctor replies into confirmed, corrected,
  missing-record, not-applicable, or specialist-review outcomes without raw
  message text.
- `2026-05-03-case001-specialist-owner-routing-gate.ipynb` - de-identified
  routing gate that maps unresolved domains to likely clinical owners while
  keeping patient-specific claims blocked.
- `2026-05-04-case001-owner-outreach-packet-gate.ipynb` - de-identified
  outreach gate that converts owner routes into one narrow ask per clinical
  owner while keeping private responses out of the public repo.
- `2026-04-28-public-case-data-release-gate.ipynb` - privacy and public-release
  gate that blocks raw records, identifiers, local paths, and patient-specific
  treatment claims before case data enters the public repo.
- `2026-04-28-private-to-public-case-extraction-gate.ipynb` - privacy gate that
  models private-source to public-summary release decisions without raw records
  or identifiers.
- `2026-04-28-case001-private-intake-priority-gate.ipynb` - private-workspace
  intake gate that ranks which ignored case-record domains should be indexed
  first before public-safe extraction.
- `2026-04-27-first-wet-lab-panel-optimizer.ipynb` - computational experiment
  that chooses a small first lab-panel candidate set by required assay coverage.
- `2026-04-27-mechanism-gap-matrix.ipynb` - computational literature-mapping
  experiment comparing broad component evidence with the fully integrated
  Nakafa Lab research gap.
