"""Calculate de-identified transfusion burden from a CSV log."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict

REQUIRED_COLUMNS = [
    "date",
    "body_weight_kg",
    "transfused_volume_ml",
    "red_cell_fraction",
]


class TransfusionSummary(TypedDict):
    """Human-readable transfusion burden summary."""

    row_count: int
    start_date: str
    end_date: str
    period_days: int
    mean_interval_days: float | None
    total_transfused_volume_ml: float | None
    total_volume_ml_per_kg: float | None
    annual_volume_ml_per_kg: float | None
    annual_pure_red_cell_ml_per_kg: float | None
    daily_iron_loading_mg_per_kg: float | None
    mean_pre_hb_g_dl: float | None
    mean_post_hb_g_dl: float | None
    warnings: list[str]


@dataclass(frozen=True)
class TransfusionRow:
    """Normalized de-identified transfusion row with explicit field types."""

    date: dt.date
    body_weight_kg: float
    transfused_volume_ml: float
    red_cell_fraction: float
    pre_hb_g_dl: float | None
    post_hb_g_dl: float | None


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for the transfusion burden calculator."""
    parser = argparse.ArgumentParser(
        description="Calculate transfusion burden from a de-identified CSV log."
    )
    parser.add_argument("input_csv")
    parser.add_argument(
        "--json", action="store_true", help="Print JSON instead of text."
    )
    return parser.parse_args()


def parse_date(value: str) -> dt.date:
    """Parse an ISO date string."""
    return dt.date.fromisoformat(value.strip())


def parse_optional_float(value: str | None) -> float | None:
    """Parse an optional numeric value."""
    if value is None:
        return None

    stripped = value.strip()
    if not stripped:
        return None

    return float(stripped)


def require_float(row: dict[str, str], column: str, row_number: int) -> float:
    """Read a required float from a CSV row."""
    value = row.get(column)
    if value is None or not value.strip():
        raise ValueError(f"Row {row_number}: missing required column `{column}`.")

    return float(value)


def require_positive_float(row: dict[str, str], column: str, row_number: int) -> float:
    """Read a required positive finite float from a CSV row."""
    value = require_float(row, column, row_number)
    if math.isfinite(value) and value > 0:
        return value

    raise ValueError(f"Row {row_number}: `{column}` must be a positive number.")


def validate_columns(fieldnames: list[str] | None) -> None:
    """Ensure the CSV contains the required columns."""
    if fieldnames is None:
        raise ValueError("CSV is missing a header row.")

    missing = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
    if not missing:
        return

    joined = ", ".join(missing)
    raise ValueError(f"CSV is missing required columns: {joined}.")


def load_rows(input_csv: str) -> list[TransfusionRow]:
    """Load and normalize transfusion rows from a CSV file."""
    rows: list[TransfusionRow] = []
    with Path(input_csv).open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = list(reader.fieldnames) if reader.fieldnames is not None else None
        validate_columns(fieldnames)

        for row_number, row in enumerate(reader, start=2):
            if not any((value or "").strip() for value in row.values()):
                continue

            red_cell_fraction = require_float(row, "red_cell_fraction", row_number)
            if not math.isfinite(red_cell_fraction) or not 0 < red_cell_fraction <= 1:
                raise ValueError(
                    f"Row {row_number}: `red_cell_fraction` must be between 0 and 1."
                )

            body_weight_kg = require_positive_float(row, "body_weight_kg", row_number)
            transfused_volume_ml = require_positive_float(
                row, "transfused_volume_ml", row_number
            )

            rows.append(
                TransfusionRow(
                    date=parse_date(row["date"]),
                    body_weight_kg=body_weight_kg,
                    transfused_volume_ml=transfused_volume_ml,
                    red_cell_fraction=red_cell_fraction,
                    pre_hb_g_dl=parse_optional_float(row.get("pre_hb_g_dl")),
                    post_hb_g_dl=parse_optional_float(row.get("post_hb_g_dl")),
                )
            )

    if rows:
        return sorted(rows, key=lambda row: row.date)

    raise ValueError("CSV has no transfusion rows.")


def mean(values: list[float]) -> float | None:
    """Return the arithmetic mean for non-empty numeric values."""
    if not values:
        return None

    return sum(values) / len(values)


def rounded(value: float | None, digits: int = 2) -> float | None:
    """Round a value while preserving nulls."""
    if value is None:
        return None

    return round(value, digits)


def summarize_rows(rows: list[TransfusionRow]) -> TransfusionSummary:
    """Summarize transfusion burden from normalized rows."""
    if not rows:
        raise ValueError("At least one transfusion row is required.")

    start_date = rows[0].date
    end_date = rows[-1].date
    period_days = (end_date - start_date).days + 1
    transfusion_intervals = [
        float((rows[index].date - rows[index - 1].date).days)
        for index in range(1, len(rows))
    ]
    volume_ml_per_kg = sum(
        row.transfused_volume_ml / row.body_weight_kg for row in rows
    )
    pure_red_cell_ml_per_kg = sum(
        row.transfused_volume_ml * row.red_cell_fraction / row.body_weight_kg
        for row in rows
    )
    annual_factor = 365 / period_days
    pre_hb_values = [row.pre_hb_g_dl for row in rows if row.pre_hb_g_dl is not None]
    post_hb_values = [row.post_hb_g_dl for row in rows if row.post_hb_g_dl is not None]

    annual_pure_red_cell_ml_per_kg = pure_red_cell_ml_per_kg * annual_factor
    warnings: list[str] = []
    if len(rows) < 2:
        warnings.append("Only one transfusion row; interval cannot be calculated.")
    if period_days < 28:
        warnings.append(
            "Observation window is under 28 days; annualized values are noisy."
        )

    return {
        "row_count": len(rows),
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "period_days": period_days,
        "mean_interval_days": rounded(mean(transfusion_intervals)),
        "total_transfused_volume_ml": rounded(
            sum(row.transfused_volume_ml for row in rows)
        ),
        "total_volume_ml_per_kg": rounded(volume_ml_per_kg),
        "annual_volume_ml_per_kg": rounded(volume_ml_per_kg * annual_factor),
        "annual_pure_red_cell_ml_per_kg": rounded(annual_pure_red_cell_ml_per_kg),
        "daily_iron_loading_mg_per_kg": rounded(
            annual_pure_red_cell_ml_per_kg * 1.08 / 365, 3
        ),
        "mean_pre_hb_g_dl": rounded(mean(pre_hb_values)),
        "mean_post_hb_g_dl": rounded(mean(post_hb_values)),
        "warnings": warnings,
    }


def format_summary(summary: TransfusionSummary) -> str:
    """Format a transfusion burden summary for humans."""
    lines = [
        "# Transfusion Burden Summary",
        "",
        f"- Rows: {summary['row_count']}",
        f"- Window: {summary['start_date']} to {summary['end_date']}",
        f"- Period days: {summary['period_days']}",
        f"- Mean interval days: {summary['mean_interval_days']}",
        f"- Total transfused volume ml: {summary['total_transfused_volume_ml']}",
        f"- Total volume ml/kg: {summary['total_volume_ml_per_kg']}",
        f"- Annualized volume ml/kg/year: {summary['annual_volume_ml_per_kg']}",
        "- Annualized pure red-cell volume ml/kg/year: "
        f"{summary['annual_pure_red_cell_ml_per_kg']}",
        "- Estimated daily iron loading mg/kg/day: "
        f"{summary['daily_iron_loading_mg_per_kg']}",
        f"- Mean pre-transfusion Hb g/dL: {summary['mean_pre_hb_g_dl']}",
        f"- Mean post-transfusion Hb g/dL: {summary['mean_post_hb_g_dl']}",
    ]

    if not summary["warnings"]:
        return "\n".join(lines)

    lines.extend(["", "## Warnings"])
    lines.extend(f"- {warning}" for warning in summary["warnings"])
    return "\n".join(lines)


def main() -> int:
    """Run the transfusion burden calculator."""
    args = parse_args()
    summary = summarize_rows(load_rows(args.input_csv))

    if args.json:
        print(json.dumps(summary, indent=2, sort_keys=True))
        return 0

    print(format_summary(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
