"""Capture branch-review clinician responses as public-safe labels."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Final, TypedDict

CAPTURED_LABEL: Final = "branch_review_response_captured_public_labels_only"
FOLLOWUP_LABEL: Final = "branch_review_response_needs_private_followup"
BLOCKED_LABEL: Final = "branch_review_response_release_blocked_private_material"

REQUIRED_COLUMNS: Final = (
    "response_label",
    "branch_label",
    "packet_domain",
    "reviewer_role_label",
    "private_response_ref",
    "public_summary_label",
    "notes_private",
)

PRIVATE_ONLY_COLUMNS: Final = {
    "private_response_ref",
    "notes_private",
}

ALLOWED_RESPONSE_LABELS: Final = {
    "missing_packet_domain",
    "branch_in_scope_for_private_review",
    "branch_out_of_scope_for_private_review",
    "stabilization_first_private_review",
    "benchmark_only_private_review",
    "cannot_answer_from_packet",
    "release_blocked_private_material",
}

ALLOWED_BRANCH_LABELS: Final = {
    "allogeneic_hct",
    "autologous_gene_cell",
    "noncurative_disease_modification",
    "standard_care_stabilization",
    "benchmark_only_tracking",
    "packet_readiness",
    "none",
}

REQUIRED_PACKET_DOMAINS: Final = {
    "diagnosis_genotype_phenotype",
    "transfusion_burden_response",
    "blood_bank_immune_history",
    "iron_organ_chelation_status",
    "hct_gene_cell_access_context",
    "consent_ethics_private_owner_review",
    "none",
}

BRANCH_RESPONSE_LABELS: Final = {
    "branch_in_scope_for_private_review",
    "branch_out_of_scope_for_private_review",
    "stabilization_first_private_review",
    "benchmark_only_private_review",
}

FOLLOWUP_RESPONSE_LABELS: Final = {
    "missing_packet_domain",
    "cannot_answer_from_packet",
}

BLOCKED_OUTPUTS: Final = [
    "raw clinician message",
    "private response reference",
    "doctor or hospital identity",
    "patient-specific eligibility claim",
    "therapy selection",
    "trial-screening instruction",
    "referral instruction",
    "travel or import plan",
    "purchase or procurement route",
    "dose or treatment recommendation",
    "transfusion or chelation change",
    "sample routing",
]


class ResponseCapture(TypedDict):
    """Public-safe projection from private clinician response rows."""

    current_label: str
    captured_labels: list[str]
    missing_domains: list[str]
    branch_scope_labels: list[str]
    blocked_outputs: list[str]


def validate_columns(fieldnames: list[str] | None) -> None:
    """Ensure the response-capture CSV has the required columns."""
    if fieldnames is None:
        raise ValueError("CSV is missing a header row.")

    missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if not missing:
        return

    joined = ", ".join(missing)
    raise ValueError(f"CSV is missing required columns: {joined}.")


def require_value(row: dict[str, str], column: str, row_number: int) -> str:
    """Return one required stripped CSV value."""
    value = (row.get(column) or "").strip()
    if value:
        return value

    raise ValueError(f"Row {row_number}: missing `{column}`.")


def optional_value(row: dict[str, str], column: str) -> str:
    """Return one optional stripped CSV value."""
    return (row.get(column) or "").strip()


def expected_public_label(response_label: str, branch_label: str) -> str:
    """Return the expected public summary label for a response row."""
    if response_label in BRANCH_RESPONSE_LABELS:
        return f"{response_label}_{branch_label}"
    return response_label


def load_rows(input_csv: str) -> list[dict[str, str]]:
    """Load private response rows and validate label-only shape."""
    rows: list[dict[str, str]] = []
    with Path(input_csv).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = list(reader.fieldnames) if reader.fieldnames is not None else None
        validate_columns(fieldnames)

        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            response_label = require_value(row, "response_label", row_number)
            branch_label = require_value(row, "branch_label", row_number)
            packet_domain = require_value(row, "packet_domain", row_number)
            public_summary_label = require_value(
                row, "public_summary_label", row_number
            )

            if response_label not in ALLOWED_RESPONSE_LABELS:
                raise ValueError(f"Row {row_number}: unknown response label.")
            if branch_label not in ALLOWED_BRANCH_LABELS:
                raise ValueError(f"Row {row_number}: unknown branch label.")
            if packet_domain not in REQUIRED_PACKET_DOMAINS:
                raise ValueError(f"Row {row_number}: unknown packet domain.")
            if public_summary_label != expected_public_label(
                response_label, branch_label
            ):
                raise ValueError(f"Row {row_number}: invalid public summary label.")
            if response_label in BRANCH_RESPONSE_LABELS and branch_label == "none":
                raise ValueError(f"Row {row_number}: branch response needs a branch.")
            if response_label not in BRANCH_RESPONSE_LABELS and branch_label != "none":
                raise ValueError(f"Row {row_number}: non-branch response uses branch.")
            if response_label == "missing_packet_domain" and packet_domain == "none":
                raise ValueError(
                    f"Row {row_number}: missing domain response needs domain."
                )
            if response_label != "missing_packet_domain" and packet_domain != "none":
                raise ValueError(f"Row {row_number}: non-missing response uses domain.")

            rows.append(
                {
                    "response_label": response_label,
                    "branch_label": branch_label,
                    "packet_domain": packet_domain,
                    "reviewer_role_label": require_value(
                        row, "reviewer_role_label", row_number
                    ),
                    "private_response_ref": require_value(
                        row, "private_response_ref", row_number
                    ),
                    "public_summary_label": public_summary_label,
                    "notes_private": optional_value(row, "notes_private"),
                }
            )

    if rows:
        return rows

    raise ValueError("CSV has no branch-review response rows.")


def unique_sorted(values: list[str]) -> list[str]:
    """Return stable unique labels without empty or none placeholders."""
    return sorted({value for value in values if value and value != "none"})


def assert_public_output_safe(capture: ResponseCapture) -> None:
    """Fail closed if private-only fields entered public output."""
    leaked = PRIVATE_ONLY_COLUMNS.intersection(capture)
    if leaked:
        joined = ", ".join(sorted(leaked))
        raise ValueError(f"Public output leaked private fields: {joined}.")


def capture_rows(rows: list[dict[str, str]]) -> ResponseCapture:
    """Project private clinician response rows into public-safe labels."""
    response_labels = [row["response_label"] for row in rows]
    branch_labels = [
        row["public_summary_label"]
        for row in rows
        if row["response_label"] in BRANCH_RESPONSE_LABELS
    ]
    missing_domains = [
        row["packet_domain"]
        for row in rows
        if row["response_label"] == "missing_packet_domain"
    ]

    if "release_blocked_private_material" in response_labels:
        current_label = BLOCKED_LABEL
    elif any(label in FOLLOWUP_RESPONSE_LABELS for label in response_labels):
        current_label = FOLLOWUP_LABEL
    else:
        current_label = CAPTURED_LABEL

    capture: ResponseCapture = {
        "current_label": current_label,
        "captured_labels": unique_sorted([row["public_summary_label"] for row in rows]),
        "missing_domains": unique_sorted(missing_domains),
        "branch_scope_labels": unique_sorted(branch_labels),
        "blocked_outputs": list(BLOCKED_OUTPUTS),
    }
    assert_public_output_safe(capture)
    return capture


def main() -> int:
    """Run the response-capture CLI."""
    parser = argparse.ArgumentParser(
        description="Capture branch-review clinician responses as public labels."
    )
    parser.add_argument("input_csv")
    args = parser.parse_args()
    capture = capture_rows(load_rows(args.input_csv))
    print(json.dumps(capture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
