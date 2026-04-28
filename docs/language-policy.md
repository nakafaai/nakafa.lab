# Repository Language Policy

Nakafa Lab repository-authored content is written in English.

This applies to:

- documentation;
- research findings and hypotheses;
- status journals;
- templates;
- scripts, comments, and docstrings;
- notebooks;
- LaTeX manuscript text.

Conversations with the founder may happen in Indonesian, but committed repo
content should be English so doctors, researchers, engineers, and collaborators
can review it consistently.

## Source Data Boundary

Raw source snapshots in `data/` may contain source-language text because they
preserve evidence from public databases, registries, or publications. Do not
rewrite raw snapshots for style. Instead, write English summaries in `research/`,
`docs/`, or `paper/` and cite the source snapshot.

URLs, organization names, product names, gene symbols, author names, and exact
source titles may preserve their original spelling when needed for traceability.

## Check

Run this language-policy check before committing prose-heavy changes:

```bash
uv run python scripts/check_repo_language.py
```

The check scans tracked, staged, and untracked non-ignored repo-authored text so
new files are checked before they are committed.
