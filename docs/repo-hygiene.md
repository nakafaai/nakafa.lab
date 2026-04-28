# Repository Hygiene

This repository is public-facing. It should be readable for doctors,
researchers, engineers, and donors without exposing private data or generated
noise.

## Tracked Content

| Area | Purpose |
| --- | --- |
| `README.md` | public project overview and repo map |
| `docs/` | operating protocol, status journals, setup notes, and repo hygiene |
| `research/thalassemia/` | thalassemia findings, hypotheses, assay plans, prioritization, notebooks, and de-identified case context |
| `research/islamic/` | Quran, hadith, tafsir, and Islamic reasoning lane kept separate from biomedical claims |
| `data/` | small reproducible source snapshots, not patient data |
| `paper/` | LaTeX paper source and bibliography |
| `scripts/` | small Python utilities for reproducible fetching and calculations |
| `scripts/manifests/` | line-oriented manifests used by Python checks |
| `templates/` | reusable research, assay, and de-identified clinical-context templates |

The current tracked-file audit is documented in
[repo-traceability-2026-04-27.md](repo-traceability-2026-04-27.md).

## Language Policy

Repository-authored content must be written in English. The policy and source
data boundary are documented in [language-policy.md](language-policy.md).

## Ignored Content

Generated or local-only files should not enter Git:

- `.ruff_cache/`;
- `.ipynb_checkpoints/`;
- `.venv/`;
- `__pycache__/` and `*.pyc`;
- `tmp/` for local extraction, rendering, and scratch outputs;
- `paper/build/` and other LaTeX outputs;
- `.env*`, private keys, credentials, and `private/`.

If a generated file is needed for evidence, save the smallest source-linked
snapshot under `data/` and register it in
`research/thalassemia/references/source-registry.md`.

Do not commit raw `.html` files. If page-level context is unavoidable, commit a
small source-linked text extraction under `data/literature/fulltext/` and cite
it from a finding.

## Public Repo Privacy Rule

Do not commit identifiable patient data:

- no names;
- no exact addresses;
- no hospital record numbers;
- no phone numbers or emails;
- no ID numbers;
- no face photos;
- no exact birth dates.

Case material must stay de-identified and must separate family-reported context,
medical records, lab values, repo interpretation, and questions for clinicians.

Use
[public-case-data-release-checklist.md](../templates/public-case-data-release-checklist.md)
before adding any case-context update. Raw PDFs, scans, photos, source exports,
and local file paths are private working material and should not be tracked.
When a private record contains a fact that should become public case context,
use
[private-to-public-case-extraction-template.md](../templates/private-to-public-case-extraction-template.md)
to document the source class, release class, extracted fact, and omitted
material.

## Private Case Intake Workspace

Use `private/<case-code>/` for local-only medical-record intake. The directory
is intentionally ignored by Git, so it can hold raw PDFs, local source indexes,
and working extraction worksheets without becoming public repo content.

The tracked operating model is:

1. index raw records under `private/<case-code>/` with
   [private-case-intake-index-template.md](../templates/private-case-intake-index-template.md);
2. extract only public-safe facts into a de-identified timeline or worksheet;
3. run `scripts/summarize_case_timeline.py` on any de-identified timeline
   candidate before writing public case prose;
4. use the public release checklist before committing case-context updates.

The timeline summarizer now checks row content for obvious local paths,
contact details, record identifiers, exact birth-date labels, and patient-name
labels before it prints a summary. It also suppresses exact date windows by
default; use `--include-dates` only for ignored private outputs. Day-level
timeline dates require `--private-input`, while public timeline candidates
should use `event_time_precision` values such as `year`, `month`, `relative`,
or `unknown`.

## Security Checks

Before committing hygiene-sensitive changes, run:

```bash
git status --short
uv run ruff check .
uv run ruff format --check .
uv run pyright scripts
uv run python scripts/check_repo.py
uv run python scripts/check_repo_language.py
uv run python scripts/check_public_repo.py
uv run python scripts/selftest_repo_checks.py
git diff --check
```

`scripts/check_public_repo.py` wraps these public-repo checks in one repeatable
command. It scans tracked, staged, and untracked non-ignored files. It fails if
blocked local paths, raw case media, local absolute references, or common secret
patterns are present. It also runs case-context-specific identifier checks for
email-like strings, phone or fax label-value patterns, exact birth-date
label-value patterns, direct record identifiers, and patient-name label-value
patterns.

`scripts/check_repo_language.py` uses the same tracked, staged, and untracked
non-ignored candidate-file scope for repo-authored text.

`scripts/selftest_repo_checks.py` runs dependency-free assertions for the
privacy and language checkers so their core blocks do not regress silently.
