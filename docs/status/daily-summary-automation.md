# Daily Research Summary Automation

Date created: 2026-04-27
Automation id: `nakafa-lab-daily-research-summary`
Status: active

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

- `pnpm check`;
- lightweight syntax or link checks relevant to changed files;
- LaTeX build when the paper changes.

Verified scoped batches should be committed and pushed to `main`.
