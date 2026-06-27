"""Check branch-review private packet readiness without exposing private data."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Final, TypedDict

READY_READINESS_LABEL: Final = "ready_for_private_clinician_review"
NOT_READY_LABEL: Final = "branch_review_packet_not_ready_public_only"
READY_LABEL: Final = "branch_review_packet_ready_for_private_clinician_review"

REQUIRED_DOMAINS: Final = (
    "diagnosis_genotype_phenotype",
    "transfusion_burden_response",
    "blood_bank_immune_history",
    "iron_organ_chelation_status",
    "hct_gene_cell_access_context",
    "consent_ethics_private_owner_review",
)

REQUIRED_COLUMNS: Final = (
    "domain",
    "readiness_label",
    "owner_label",
    "private_record_ref",
    "public_missing_label",
    "public_ready_label",
    "notes_private",
)

PRIVATE_ONLY_COLUMNS: Final = {
    "private_record_ref",
    "notes_private",
}

ALLOWED_READINESS_LABELS: Final = {
    READY_READINESS_LABEL,
    "missing_private_record",
    "needs_private_owner_review",
}

BLOCKED_OUTPUTS: Final = [
    "patient-specific eligibility claim",
    "therapy selection",
    "trial-screening instruction",
    "referral instruction",
    "travel or import plan",
    "purchase or procurement route",
    "dose or treatment recommendation",
    "transfusion or chelation change",
    "sample routing",
    "raw private record",
    "doctor or family private message",
]


class PacketEvaluation(TypedDict):
    """Public-safe readiness projection from private branch-review rows."""

    current_label: str
    ready_domains: list[str]
    missing_domains: list[str]
    public_labels: list[str]
    blocked_outputs: list[str]


def validate_columns(fieldnames: list[str] | None) -> None:
    """Ensure the CSV contains every required packet column."""
    if fieldnames is None:
        raise ValueError("CSV is missing a header row.")

    missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if not missing:
        return

    joined = ", ".join(missing)
    raise ValueError(f"CSV is missing required columns: {joined}.")


def require_value(row: dict[str, str], column: str, row_number: int) -> str:
    """Return one required stripped CSV cell."""
    value = (row.get(column) or "").strip()
    if value:
        return value

    raise ValueError(f"Row {row_number}: missing `{column}`.")


def optional_value(row: dict[str, str], column: str) -> str:
    """Return one optional stripped CSV cell."""
    return (row.get(column) or "").strip()


def expected_public_label(prefix: str, domain: str) -> str:
    """Return the only public label allowed for a domain state."""
    return f"{prefix}_{domain}"


def load_rows(input_csv: str) -> list[dict[str, str]]:
    """Load private packet rows from CSV and validate public label shape."""
    rows: list[dict[str, str]] = []
    with Path(input_csv).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = list(reader.fieldnames) if reader.fieldnames is not None else None
        validate_columns(fieldnames)

        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            domain = require_value(row, "domain", row_number)
            readiness_label = require_value(row, "readiness_label", row_number)
            public_missing_label = require_value(
                row, "public_missing_label", row_number
            )
            public_ready_label = require_value(row, "public_ready_label", row_number)

            if domain not in REQUIRED_DOMAINS:
                raise ValueError(f"Row {row_number}: unknown domain `{domain}`.")
            if readiness_label not in ALLOWED_READINESS_LABELS:
                raise ValueError(
                    f"Row {row_number}: unknown readiness label `{readiness_label}`."
                )
            if public_missing_label != expected_public_label("missing", domain):
                raise ValueError(f"Row {row_number}: invalid public missing label.")
            if public_ready_label != expected_public_label("ready", domain):
                raise ValueError(f"Row {row_number}: invalid public ready label.")

            private_record_ref = optional_value(row, "private_record_ref")
            if readiness_label == READY_READINESS_LABEL and not private_record_ref:
                raise ValueError(
                    f"Row {row_number}: ready domains need `private_record_ref`."
                )

            rows.append(
                {
                    "domain": domain,
                    "readiness_label": readiness_label,
                    "owner_label": require_value(row, "owner_label", row_number),
                    "private_record_ref": private_record_ref,
                    "public_missing_label": public_missing_label,
                    "public_ready_label": public_ready_label,
                    "notes_private": optional_value(row, "notes_private"),
                }
            )

    if rows:
        return rows

    raise ValueError("CSV has no branch-review packet rows.")


def row_by_domain(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    """Index rows by domain while rejecting duplicates and omissions."""
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        domain = row["domain"]
        if domain in indexed:
            raise ValueError(f"Duplicate packet domain `{domain}`.")
        indexed[domain] = row

    missing = [domain for domain in REQUIRED_DOMAINS if domain not in indexed]
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"CSV is missing required packet domains: {joined}.")

    return indexed


def assert_public_output_safe(evaluation: PacketEvaluation) -> None:
    """Fail closed if private-only fields entered the public projection."""
    leaked = PRIVATE_ONLY_COLUMNS.intersection(evaluation)
    if leaked:
        joined = ", ".join(sorted(leaked))
        raise ValueError(f"Public output leaked private fields: {joined}.")


def evaluate_rows(rows: list[dict[str, str]]) -> PacketEvaluation:
    """Project private packet rows into public-safe readiness labels."""
    indexed = row_by_domain(rows)
    ready_domains: list[str] = []
    missing_domains: list[str] = []
    public_labels: list[str] = []

    for domain in REQUIRED_DOMAINS:
        row = indexed[domain]
        if row["readiness_label"] == READY_READINESS_LABEL:
            ready_domains.append(domain)
            public_labels.append(row["public_ready_label"])
            continue

        missing_domains.append(domain)
        public_labels.append(row["public_missing_label"])

    current_label = READY_LABEL if not missing_domains else NOT_READY_LABEL
    evaluation: PacketEvaluation = {
        "current_label": current_label,
        "ready_domains": ready_domains,
        "missing_domains": missing_domains,
        "public_labels": public_labels,
        "blocked_outputs": list(BLOCKED_OUTPUTS),
    }
    assert_public_output_safe(evaluation)
    return evaluation


def main() -> int:
    """Run the packet-readiness checker CLI."""
    parser = argparse.ArgumentParser(
        description="Check branch-review packet readiness with public-safe output."
    )
    parser.add_argument("input_csv")
    args = parser.parse_args()
    evaluation = evaluate_rows(load_rows(args.input_csv))
    print(json.dumps(evaluation, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
