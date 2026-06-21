# Public Recipient Card Projection Gate

Date checked: 2026-06-21
Status: synthetic projection tool readiness, not contact permission and not treatment advice

## Direct Answer

June 21 adds a small script and self-test that turn private source-index rows
into public recipient-card labels without emitting private-only fields.

Current operational label:

`case001_public_card_projection_tool_ready_synthetic_only`

## Projection Contract

Public cards may include alias, `source_bundle_ref`, source count,
source-kind labels, capability labels, privacy labels, terms labels, owner
scope labels, and decision label.

Private-only fields such as `raw_source_url`, `candidate_identity_private`, and
`notes_private` must never appear in projected public cards.

## Source Read

The June 21 source check did not change the biomedical boundary. Current
thalassemia, gamma-globin, HUDEP2/HbF, CD34 erythroid, and hemolysis records
support capability labels only. HHS privacy guidance supports reducing public
output to the minimum necessary label set.

## Boundary

Quran 49:6 and 4:58 are process-ethics anchors only, not biomedical evidence.
This gate does not select a lab, contact anyone, request samples, screen for a
trial, buy or import a compound, or recommend treatment.

## Sources

- [Workflow JSON](../../../data/workflows/case-001/2026-06-21-public-recipient-card-projection-gate.json)
- [June 21 source refresh](../../../data/literature/pubmed/2026-06-21-public-recipient-card-projection-refresh.json)
- [Projection script](../../../scripts/project_recipient_card.py)
- [Projection self-test](../../../scripts/selftest_project_recipient_card.py)
- [HHS de-identification guidance](https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html)
- [HHS Privacy Rule summary](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html)
- PubMed PMIDs: [31424735](https://pubmed.ncbi.nlm.nih.gov/31424735/),
  [41411145](https://pubmed.ncbi.nlm.nih.gov/41411145/),
  [39108322](https://pubmed.ncbi.nlm.nih.gov/39108322/),
  [23861885](https://pubmed.ncbi.nlm.nih.gov/23861885/),
  [36769243](https://pubmed.ncbi.nlm.nih.gov/36769243/)
