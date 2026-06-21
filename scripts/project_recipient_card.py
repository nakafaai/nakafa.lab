"""Project private recipient source-index rows into a public-safe card."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import TypedDict

REQUIRED_COLUMNS = [
    "recipient_alias",
    "source_bundle_ref",
    "raw_source_url",
    "candidate_identity_private",
    "source_kind_label",
    "capability_mapping",
    "checked_date",
    "public_card_alias",
    "public_card_source_bundle_ref",
    "privacy_review_label",
    "consent_or_terms_label",
    "owner_scope_label",
]

PRIVATE_ONLY_COLUMNS = {
    "raw_source_url",
    "candidate_identity_private",
    "notes_private",
}


class PublicRecipientCard(TypedDict):
    """Public-safe projection from private source-index rows."""

    recipient_alias: str
    source_bundle_ref: str
    source_count: int
    source_kind_labels: list[str]
    capability_labels: list[str]
    privacy_review_labels: list[str]
    consent_or_terms_labels: list[str]
    owner_scope_labels: list[str]
    decision_label: str


def validate_columns(fieldnames: list[str] | None) -> None:
    """Ensure the CSV contains all required columns."""
    if fieldnames is None:
        raise ValueError("CSV is missing a header row.")

    missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if not missing:
        return

    joined = ", ".join(missing)
    raise ValueError(f"CSV is missing required columns: {joined}.")


def require_value(row: dict[str, str], column: str, row_number: int) -> str:
    """Read a required stripped cell value."""
    value = (row.get(column) or "").strip()
    if value:
        return value

    raise ValueError(f"Row {row_number}: missing `{column}`.")


def split_labels(value: str) -> list[str]:
    """Split semicolon-delimited labels while preserving simple CSV input."""
    return [item.strip() for item in value.split(";") if item.strip()]


def unique_labels(rows: list[dict[str, str]], column: str) -> list[str]:
    """Return sorted unique labels from a semicolon-delimited column."""
    labels: set[str] = set()
    for row in rows:
        labels.update(split_labels(row[column]))
    return sorted(labels)


def load_rows(input_csv: str) -> list[dict[str, str]]:
    """Load validated private source-index rows."""
    rows: list[dict[str, str]] = []
    with Path(input_csv).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = list(reader.fieldnames) if reader.fieldnames is not None else None
        validate_columns(fieldnames)

        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            normalized = {
                column: require_value(row, column, row_number)
                for column in REQUIRED_COLUMNS
            }
            rows.append(normalized)

    if rows:
        return rows

    raise ValueError("CSV has no private source-index rows.")


def require_single_value(rows: list[dict[str, str]], column: str) -> str:
    """Return the one expected value for a card-level field."""
    values = {row[column] for row in rows}
    if len(values) == 1:
        return values.pop()

    raise ValueError(f"Rows must share one `{column}` value.")


def assert_public_card_safe(card: PublicRecipientCard) -> None:
    """Fail closed if a private-only field was accidentally projected."""
    leaked = PRIVATE_ONLY_COLUMNS.intersection(card)
    if leaked:
        joined = ", ".join(sorted(leaked))
        raise ValueError(f"Public card leaked private fields: {joined}.")


def project_card(rows: list[dict[str, str]]) -> PublicRecipientCard:
    """Project private rows into one public-safe card."""
    recipient_alias = require_single_value(rows, "public_card_alias")
    source_bundle_ref = require_single_value(rows, "public_card_source_bundle_ref")

    card: PublicRecipientCard = {
        "recipient_alias": recipient_alias,
        "source_bundle_ref": source_bundle_ref,
        "source_count": len(rows),
        "source_kind_labels": unique_labels(rows, "source_kind_label"),
        "capability_labels": unique_labels(rows, "capability_mapping"),
        "privacy_review_labels": unique_labels(rows, "privacy_review_label"),
        "consent_or_terms_labels": unique_labels(rows, "consent_or_terms_label"),
        "owner_scope_labels": unique_labels(rows, "owner_scope_label"),
        "decision_label": "public_recipient_card_projection_ready",
    }
    assert_public_card_safe(card)
    return card


def main() -> int:
    """Run the projection CLI."""
    parser = argparse.ArgumentParser(
        description="Project private recipient source rows into a public-safe card."
    )
    parser.add_argument("input_csv")
    args = parser.parse_args()
    card = project_card(load_rows(args.input_csv))
    print(json.dumps(card, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
