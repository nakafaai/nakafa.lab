"""Self-test public recipient card projection without real sources."""

from __future__ import annotations

import csv
import os
import pathlib
import tempfile

import project_recipient_card as projection

FIELDNAMES = [*projection.REQUIRED_COLUMNS, "notes_private"]


def write_csv(rows: list[dict[str, str]]) -> str:
    """Write synthetic rows into a temporary CSV and return the path."""
    descriptor, raw_path = tempfile.mkstemp(suffix=".csv")
    os.close(descriptor)
    path = pathlib.Path(raw_path)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)
    return str(path)


def base_row() -> dict[str, str]:
    """Return one synthetic private row."""
    return {
        "recipient_alias": "recipient-candidate-001",
        "source_bundle_ref": "private-source-bundle-001",
        "raw_source_url": "synthetic-private-source",
        "candidate_identity_private": "synthetic-private-candidate",
        "source_kind_label": "method_page",
        "capability_mapping": "model;endpoint",
        "checked_date": "2026-06-21",
        "public_card_alias": "recipient-candidate-001",
        "public_card_source_bundle_ref": "private-source-bundle-001",
        "privacy_review_label": "public_projection_reviewed",
        "consent_or_terms_label": "terms_review_needed",
        "owner_scope_label": "preclinical_recipient_candidate",
        "notes_private": "synthetic private note",
    }


def test_projection_omits_private_fields() -> None:
    """Check that the projected card has labels but no private fields."""
    second_row = base_row() | {
        "source_kind_label": "publication",
        "capability_mapping": "raw_data;ethics",
    }
    card = projection.project_card(
        projection.load_rows(write_csv([base_row(), second_row]))
    )

    assert card["source_count"] == 2
    assert card["capability_labels"] == ["endpoint", "ethics", "model", "raw_data"]
    assert "raw_source_url" not in card
    assert "candidate_identity_private" not in card


def test_mismatched_public_alias_fails() -> None:
    """Check that rows cannot mix public aliases."""
    mixed_row = base_row() | {"public_card_alias": "recipient-candidate-002"}
    loaded = projection.load_rows(write_csv([base_row(), mixed_row]))
    try:
        projection.project_card(loaded)
    except ValueError as error:
        assert "public_card_alias" in str(error)
        return
    raise AssertionError("Expected mixed public alias failure.")


def main() -> int:
    """Run the recipient-card projection self-tests."""
    test_projection_omits_private_fields()
    test_mismatched_public_alias_fails()
    print("recipient card projection self-tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
