# Lab Outreach Approval Record Template

Status: private worksheet template with public-safe output labels only

Use this outside the public repository to record whether a founder approved a
public-safe lab quote packet. Do not paste raw messages, names, contact details,
exact private timestamps, legal notes, replies, patient records, or sample
details into Git.

## Public Fields

| Field | Allowed public-safe value |
| --- | --- |
| Case code | `case-001` or another de-identified code |
| Packet version | Dated public packet label |
| Approval alias | De-identified label such as `founder-approval-001` |
| Owner category | `founder`, `research_owner`, or `not_recorded` |
| Timing label | `current`, `expired_or_superseded`, or `not_recorded` |
| Scope label | One allowed label below |

## Allowed Labels

- `approval_not_recorded`
- `approval_denied`
- `founder_review_only`
- `approval_scope_public_safe_quote_only`
- `approval_expired_or_superseded`
- `approval_release_blocked`

## Release Check

Before publishing a label, confirm that private identifiers are absent, the
packet version is explicit, scope is only public-safe preclinical quote content,
recipient qualification is still required, response capture is still required,
and the label is not being used as treatment, procurement, trial, import,
sample-transfer, or send permission by itself.

Public output:

`approval_label: <one allowed scope label>`
