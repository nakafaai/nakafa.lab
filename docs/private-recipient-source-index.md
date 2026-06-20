# Private Recipient Source Index

Status: private workflow template, not contact permission and not medical advice

Use this template when a future helper or founder review identifies a possible
lab or CRO recipient. Do not put completed source indexes in Git.

Recommended private location:

`private/recipient-source-index/recipient-sources.csv`

The `private/` directory is ignored by Git. Keep real organization names, raw
URLs, contacts, quotes, scheduling details, private replies, and business terms
there only.

## Public-Release Rule

Public files may carry:

- recipient alias;
- `source_bundle_ref`;
- source-kind labels;
- source-count label;
- capability labels;
- final decision label.

Public files must not carry:

- raw candidate URLs;
- real organization, person, email, phone, or address details;
- private replies, quotes, pricing, scheduling, or business terms;
- patient records, patient identifiers, or sample identifiers;
- treatment, trial-screening, purchase, import, or procurement language.

## Manual Workflow

1. Copy `templates/private-recipient-source-index-template.csv` into the ignored
   private location.
2. Fill one row per source for a future recipient alias.
3. Map each source to a capability label, such as model, endpoint, raw-data,
   cost, timeline, ethics, biosafety, or material constraints.
4. Publish only the alias, `source_bundle_ref`, source-kind labels, source-count
   label, capability labels, and decision label.
5. Run `uv run python scripts/check_public_repo.py` before any public commit.

## Boundaries

This index does not select a lab, contact anyone, request samples, screen for a
trial, buy or import anything, or recommend treatment.
