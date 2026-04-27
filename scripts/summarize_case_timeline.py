"""Summarize a de-identified case timeline CSV for research routing."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
from collections import Counter
from pathlib import Path

REQUIRED_COLUMNS = [
    "case_id",
    "event_date",
    "event_type",
    "value",
    "unit",
    "source_ref",
    "routing_label",
    "confidence",
    "notes_no_phi",
]

BLOCKED_COLUMNS = {
    "address",
    "birth_date",
    "date_of_birth",
    "email",
    "hospital_id",
    "id_number",
    "medical_record_number",
    "mrn",
    "name",
    "nik",
    "phone",
}


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for a case timeline summary."""
    parser = argparse.ArgumentParser(
        description="Summarize a de-identified clinical timeline CSV."
    )
    parser.add_argument("input_csv")
    parser.add_argument(
        "--json", action="store_true", help="Print JSON instead of text."
    )
    return parser.parse_args()


def parse_date(value: str, row_number: int) -> dt.date:
    """Parse an ISO event date from a timeline row."""
    try:
        return dt.date.fromisoformat(value.strip())
    except ValueError as error:
        raise ValueError(
            f"Row {row_number}: `event_date` must use YYYY-MM-DD."
        ) from error


def normalize_fieldnames(fieldnames: list[str] | None) -> list[str]:
    """Validate and return normalized field names."""
    if fieldnames is None:
        raise ValueError("CSV is missing a header row.")

    normalized = [field.strip() for field in fieldnames]
    missing = [column for column in REQUIRED_COLUMNS if column not in normalized]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"CSV is missing required columns: {joined}.")

    blocked = sorted(set(normalized) & BLOCKED_COLUMNS)
    if blocked:
        joined = ", ".join(blocked)
        raise ValueError(f"CSV includes blocked identifier columns: {joined}.")

    return normalized


def load_rows(input_csv: str) -> list[dict[str, str]]:
    """Load non-empty de-identified timeline rows from a CSV file."""
    rows: list[dict[str, str]] = []
    with Path(input_csv).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        normalize_fieldnames(
            list(reader.fieldnames) if reader.fieldnames is not None else None
        )

        for row_number, row in enumerate(reader, start=2):
            normalized = {
                key: (value or "").strip()
                for key, value in row.items()
                if key is not None
            }
            if not any(normalized.values()):
                continue

            parse_date(normalized["event_date"], row_number)
            rows.append(normalized)

    if rows:
        return rows

    raise ValueError("CSV has no timeline rows.")


def summarize_rows(rows: list[dict[str, str]]) -> dict:
    """Return routing-oriented counts and date coverage for timeline rows."""
    event_dates = [dt.date.fromisoformat(row["event_date"]) for row in rows]
    event_types = Counter(row["event_type"] or "unknown" for row in rows)
    routing_labels = Counter(row["routing_label"] or "unlabeled" for row in rows)
    source_refs = Counter(row["source_ref"] or "missing_source_ref" for row in rows)

    return {
        "row_count": len(rows),
        "start_date": min(event_dates).isoformat(),
        "end_date": max(event_dates).isoformat(),
        "event_types": dict(sorted(event_types.items())),
        "routing_labels": dict(sorted(routing_labels.items())),
        "source_ref_count": len(source_refs),
        "missing_source_ref_rows": source_refs.get("missing_source_ref", 0),
    }


def format_summary(summary: dict) -> str:
    """Format a de-identified timeline summary for repo review."""
    lines = [
        "# Case Timeline Summary",
        "",
        f"- Rows: {summary['row_count']}",
        f"- Window: {summary['start_date']} to {summary['end_date']}",
        f"- Source references: {summary['source_ref_count']}",
        f"- Missing source references: {summary['missing_source_ref_rows']}",
        "",
        "## Event Types",
    ]
    lines.extend(
        f"- {event_type}: {count}"
        for event_type, count in summary["event_types"].items()
    )
    lines.extend(["", "## Routing Labels"])
    lines.extend(
        f"- {label}: {count}" for label, count in summary["routing_labels"].items()
    )
    return "\n".join(lines)


def main() -> int:
    """Run the case timeline summarizer."""
    args = parse_args()
    summary = summarize_rows(load_rows(args.input_csv))

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0

    print(format_summary(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
