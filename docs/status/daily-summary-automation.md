# Daily Research Summary Automation Runbook

Date created: 2026-04-27
Automation id: `nakafa-lab-daily-research-summary`
Status: active

## Why This File Exists

This is not a leftover note. It is the repository-side runbook for the active
Codex automation with id `nakafa-lab-daily-research-summary`.

The automation itself lives outside the repository in Codex app automation
state. This file exists so the repo still explains:

- why dated status journals exist;
- what each daily summary should contain;
- what boundaries the automation must respect;
- what verification should run before a summary batch is committed.

Without this runbook, the repo would contain dated summaries but no local
explanation of the process that creates them.

## Purpose

Create a dated daily research summary in this folder so progress does not get
lost in chat history.

Each run should write or update a file named:

```text
docs/status/YYYY-MM-DD.md
```

## Expected Summary Shape

Keep each daily summary easy for an engineer-founder to scan:

- what changed since the latest status journal;
- current strongest findings;
- current blockers;
- strongest research lanes;
- patient-context data still needed;
- next evidence tasks.

## Boundaries

- Do not present the summary as a final paper or final conclusion.
- Keep biomedical claims separate from Islamic motivation.
- Do not recommend changing transfusion, chelation, immune medicine, or any
  supplement.
- Put detailed evidence in `research/**/findings/`, `data/`, or the paper, not
  inside the status journal.

## Verification

Before committing, the automation should run:

- `uv run python scripts/check_repo.py`;
- lightweight syntax or link checks relevant to changed files;
- LaTeX build when the paper changes.

Verified scoped batches should be committed and pushed to `main`.

## Cohesion Check

Keep this file only while the `nakafa-lab-daily-research-summary` automation is
active. If that automation is deleted or renamed, update this runbook and
[README.md](README.md) in the same commit.
