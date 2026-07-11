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
- `2026-05-05-case001-owner-response-capture-gate.ipynb` - de-identified
  response-capture gate that reduces owner replies to public-safe labels before
  release.
- `2026-05-06-case001-owner-follow-up-ladder-gate.ipynb` - de-identified
  follow-up ladder that maps unanswered, redirected, or record-requested
  outreach to safe next states.
- `2026-05-07-case001-public-collaborator-intake-gate.ipynb` - de-identified
  public-collaboration gate that maps helper roles to safe intake states.
- `2026-05-08-case001-public-share-kit-gate.ipynb` - de-identified public-share
  gate that checks the post states, role asks, and blocked public content before
  sharing Nakafa Lab publicly.
- `2026-05-09-case001-public-responder-qualification-gate.ipynb` -
  de-identified reply triage gate that routes public responses by role, scope,
  evidence cue, and blocked states.
- `2026-05-10-case001-registry-link-disambiguation-gate.ipynb` -
  de-identified registry-link gate that separates direct TDT context from
  query-adjacent registry records before owner routing.
- `2026-05-11-case001-mitapivat-boundary-access-inquiry-gate.ipynb` -
  de-identified mitapivat gate that separates adult label, adult TDT,
  pediatric TDT, and pediatric NTDT contexts before clinician inquiry.
- `2026-05-12-case001-mitapivat-jurisdiction-access-verification-gate.ipynb` -
  de-identified mitapivat gate that separates foreign approvals, registry hits,
  query-adjacent records, and local access claims before clinician inquiry.
- `2026-05-13-case001-mitapivat-owner-routing-gate.ipynb` -
  de-identified owner-routing gate that splits clinical, pharmacy, regulatory,
  manufacturer, trial, and financial questions before mitapivat outreach.
- `2026-05-14-case001-mitapivat-first-contact-packet-gate.ipynb` -
  de-identified first-contact gate that checks each owner packet for one
  question, public-safe sources, blocked material, escalation condition, and
  safe state.
- `2026-05-15-case001-mitapivat-response-capture-gate.ipynb` -
  de-identified response-capture gate that checks owner replies are reduced to
  labels, public actions, private actions, and next states before repo updates.
- `2026-05-16-case001-mitapivat-evidence-to-action-gate.ipynb` -
  de-identified evidence-to-action gate that keeps adult mitapivat evidence as
  a benchmark, pediatric records as watchlist states, and case action blocked
  until qualified clinician review.
- `2026-05-17-case001-mitapivat-clinician-review-readiness-gate.ipynb` -
  de-identified clinician-review readiness gate that turns the mitapivat lane
  into one hematologist question and six public-safe response labels.
- `2026-05-18-case001-mitapivat-clinician-answer-action-ladder.ipynb` -
  de-identified action ladder that maps each allowed hematologist response
  label to a private action, public action, and next state.
- `2026-05-19-case001-mitapivat-minimum-packet-readiness-gate.ipynb` -
  de-identified readiness gate that checks the seven minimum packet domains
  before asking the May 17 hematologist question.
- `2026-05-20-case001-mitapivat-seven-domain-owner-action-map.ipynb` -
  de-identified owner-action gate that maps each required mitapivat packet
  domain to a clinical owner category, public-safe label, and missing-data
  blocker.
- `2026-05-21-case001-mitapivat-clinician-conversation-sequence-gate.ipynb` -
  de-identified sequence gate that keeps the mitapivat clinician conversation
  ordered from scope and core labels through seven-domain readiness before the
  review-readiness question.
- `2026-05-22-case001-clinician-confirmation-packet-index-gate.ipynb` -
  de-identified packet-index gate that keeps the doctor-facing handoff first,
  private records outside Git, mitapivat downstream, and the main paper
  appendix-only.
- `2026-05-23-case001-clinician-response-label-capture-gate.ipynb` -
  de-identified response-capture gate that turns clinician replies into
  public-safe labels, missing-record categories, owner categories, and next
  gates.
- `2026-05-24-case001-mitapivat-indonesia-access-evidence-gap.ipynb` -
  de-identified access evidence-gap gate that keeps BPOM and trial-geography
  checks as owner-verification labels, not access or import instructions.
- `2026-05-25-case001-asia-curative-trial-geography-gate.ipynb` -
  de-identified registry-geography gate that keeps Asia curative gene-cell
  therapy signals as benchmark evidence, not trial-screening instructions.
- `2026-05-26-case001-advanced-therapy-screening-owner-packet-gate.ipynb` -
  de-identified owner-packet gate that keeps advanced-therapy screening
  dependent on seven owner-labeled domains and privacy-safe output labels.
- `2026-05-27-case001-advanced-therapy-clinician-answer-ladder-gate.ipynb` -
  de-identified answer-ladder gate that reduces doctor or specialist replies
  to safe labels before any advanced-therapy state changes.
- `2026-05-28-case001-advanced-therapy-route-triage-gate.ipynb` -
  de-identified route-triage gate that separates HSCT, gene-cell,
  non-curative drug, stabilization, and registry branches before selection.
- `2026-05-29-case001-curative-affordability-gap-matrix-gate.ipynb` -
  de-identified gap-matrix gate that checks affordability, infrastructure,
  conditioning, monitoring, access, safety, fertility, and assay-feasibility
  blockers before candidate promotion.
- `2026-05-30-case001-affordable-cure-candidate-promotion-gate.ipynb` -
  de-identified promotion gate that checks required candidate fields, decision
  labels, and blocked public content before any affordable-cure lane moves up.
- `2026-05-31-case001-minimum-assay-readiness-gate.ipynb` - de-identified
  assay-readiness gate that checks identity, model, controls, endpoints, stop
  rules, raw-data plan, and privacy boundaries before lab quote.
- `2026-06-01-case001-first-quote-panel-assay-readiness-audit.ipynb` -
  de-identified applied audit of the first quote panel and PubChem identity
  refresh before lab quote.
- `2026-06-02-case001-first-quote-request-table-gate.ipynb` -
  de-identified quote-table gate that checks included items, held items, lab
  capabilities, and blocked public content before any quote outreach.
- `2026-06-04-case001-t-bdmc-material-identity-gate.ipynb` -
  de-identified material gate that keeps `T-BDMC` held until procurement,
  batch, and safety-window requirements pass.
- `2026-06-05-case001-ginger-extract-standardization-gate.ipynb` -
  de-identified material and endpoint gate that keeps standardized
  6-shogaol-rich ginger extract held until marker, batch, matrix-control, and
  support-only red-cell endpoint requirements pass.
- `2026-06-06-case001-t-bdmc-catalog-feasibility-gate.ipynb` -
  de-identified catalog feasibility gate that checks `HY-N11902` is a material
  lead only, with exact stereochemistry and safety-window requirements still
  blocking quote movement.
- `2026-06-07-case001-lab-outreach-approval-gate.ipynb` - de-identified
  approval gate that checks no lab contact occurs without founder approval,
  quote lines stay scoped, held addenda stay excluded, and private or
  patient-specific content stays blocked.
- `2026-06-08-case001-lab-recipient-qualification-gate.ipynb` -
  de-identified recipient gate that separates preclinical quote recipients
  from clinical therapy or trial centers before any approved packet is routed.
- `2026-06-09-hbg-promoter-editing-benchmark-refresh.ipynb` -
  benchmark-refresh gate that classifies HbF-only candidate claims as
  novelty-blocked unless they add affordability, lower infrastructure, and
  multi-endpoint assay value beyond current HBG promoter editing evidence.
- `2026-06-10-case001-first-quote-acceptance-gate.ipynb` -
  de-identified quote-acceptance gate that rejects HbF-only offers, holds
  partial endpoint offers, and passes only complete public-safe preclinical
  quote offers.
- `2026-06-13-case001-first-quote-response-capture-gate.ipynb` -
  de-identified response-capture gate that blocks raw private lab replies and
  classifies public-safe reply labels before quote acceptance.
- `2026-06-14-case001-erythroid-metabolism-endpoint-addendum.ipynb` -
  endpoint addendum gate that keeps ATP/glycolysis and related metabolism
  readouts optional, additive, and blocked from treatment or procurement scope.
- `2026-06-15-case001-first-quote-outbound-packet-gate.ipynb` -
  outbound packet gate that separates founder-review readiness from send
  permission and blocks private or clinical scope.
- `2026-06-16-case001-founder-approval-record-gate.ipynb` -
  approval-record gate that reduces founder approval state to public-safe labels
  while keeping contact blocked until recipient qualification and packet checks
  also pass.
- `2026-06-17-case001-private-send-readiness-gate.ipynb` -
  whole-workflow gate that keeps private send readiness on hold until approval,
  recipient qualification, packet pass, response capture, and private handling
  all pass together.
- `2026-06-18-case001-recipient-evidence-card-gate.ipynb` -
  recipient evidence-card gate that classifies future lab or CRO candidates by
  public capabilities without naming, contacting, or endorsing any organization.
- `2026-06-19-case001-recipient-source-privacy-gate.ipynb` -
  source-privacy gate that keeps raw candidate URLs and identities in a private
  source index while public cards use bundle refs and capability labels.
- `2026-06-20-case001-private-recipient-source-index-readiness-gate.ipynb` -
  private-index readiness gate that checks ignored source rows can support
  public source-bundle labels without leaking raw candidate details.
- `2026-06-21-case001-public-recipient-card-projection-gate.ipynb` -
  projection-gate notebook that smoke-tests synthetic private rows into
  public-safe recipient-card labels without private-field leakage.
- `2026-06-22-current-curative-evidence-radar.ipynb` - route-separation smoke
  test for current curative evidence records, keeping patient-specific action
  blocked.
- `2026-06-24-case001-curative-branch-doctor-question-gate.ipynb` -
  doctor-question gate that checks curative branch outputs remain question
  labels and never patient-specific action labels.
- `2026-06-25-case001-branch-review-minimum-packet-gate.ipynb` - packet gate
  that keeps branch review blocked until all private packet domains are
  label-ready.
- `2026-06-27-case001-branch-review-packet-checker-gate.ipynb` - synthetic
  smoke test for a private branch-review packet checker that emits only
  ready/missing public labels.
- `2026-06-28-case001-branch-review-response-capture-gate.ipynb` - synthetic
  smoke test for reducing future clinician branch replies to public-safe
  labels.
- `2026-06-30-case001-branch-review-handoff-status-gate.ipynb` - synthetic
  smoke test for collapsing packet-checker and response-capture outputs into
  one public-safe handoff label.
- `2026-07-02-case001-branch-review-clinician-brief-gate.ipynb` - synthetic
  sequencing check that keeps the doctor brief packet-first, branch-second,
  and response-label-only.
- `2026-07-04-case001-public-outreach-branch-routing-gate.ipynb` - synthetic
  routing check that keeps public outreach role-bounded, source-backed, and
  blocked from medical-action outputs.
- `2026-07-06-case001-asia-registry-source-radar.ipynb` - compact ranking
  check for Asia-facing public source follow-up without eligibility outputs.
- `2026-07-08-casgevy-source-consistency-gate.ipynb` - consistency check that
  current Casgevy notes use the FDA 2+ benchmark while older JSON and journal
  snapshots remain historical.
- `2026-07-09-bpom-access-refresh-gate.ipynb` - BPOM access refresh gate that
  keeps advanced benchmark therapies in public-registry-not-found status and
  hydroxyurea as a sanity-check product hit only.
- `2026-07-10-case001-active-registry-gate.ipynb` - active registry refresh
  gate that classifies China and CS-101 source snapshots while blocking
  eligibility, referral, trial-screening, and treatment outputs.
- `2026-07-11-case001-country-registry-sweep-gate.ipynb` - country-specific
  ClinicalTrials.gov sweep gate that deduplicates active beta-thalassemia
  source IDs while keeping zero-country results as query labels only.
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
