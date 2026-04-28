"""Self-test transfusion burden calculations without private data."""

from __future__ import annotations

import datetime as dt
import pathlib
import tempfile

import calc_transfusion_burden as burden


def assert_close(actual: float | None, expected: float) -> None:
    """Assert that an optional float is close to the expected value."""
    assert actual is not None
    assert abs(actual - expected) < 0.000001


def weekly_synthetic_rows() -> list[burden.TransfusionRow]:
    """Build a synthetic weekly transfusion log."""
    dates = [
        dt.date(2026, 1, 1),
        dt.date(2026, 1, 8),
        dt.date(2026, 1, 15),
        dt.date(2026, 1, 22),
        dt.date(2026, 1, 29),
    ]
    return [
        burden.TransfusionRow(
            date=date,
            body_weight_kg=50.0,
            transfused_volume_ml=250.0,
            red_cell_fraction=0.65,
            pre_hb_g_dl=8.3,
            post_hb_g_dl=10.3,
        )
        for date in dates
    ]


def expect_csv_error(content: str, expected_message: str) -> None:
    """Write temporary CSV content and assert that loading it fails."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = pathlib.Path(tmpdir) / "transfusion-log.csv"
        path.write_text(content, encoding="utf-8")

        try:
            burden.load_rows(str(path))
        except ValueError as error:
            assert expected_message in str(error)
            return

    raise AssertionError(f"Expected CSV error containing: {expected_message}")


def test_weekly_synthetic_summary() -> None:
    """Check the summary math for a synthetic weekly log."""
    rows = weekly_synthetic_rows()
    summary = burden.summarize_rows(rows)

    period_days = 29
    volume_ml_per_kg = 25.0
    pure_red_cell_ml_per_kg = 16.25
    annual_volume = round(volume_ml_per_kg * 365 / period_days, 2)
    annual_pure_red_cell = round(pure_red_cell_ml_per_kg * 365 / period_days, 2)
    daily_iron = round((pure_red_cell_ml_per_kg * 365 / period_days) * 1.08 / 365, 3)

    assert summary["row_count"] == 5
    assert summary["period_days"] == period_days
    assert summary["mean_interval_days"] == 7.0
    assert summary["warnings"] == []
    assert_close(summary["total_volume_ml_per_kg"], volume_ml_per_kg)
    assert_close(summary["annual_volume_ml_per_kg"], annual_volume)
    assert_close(summary["annual_pure_red_cell_ml_per_kg"], annual_pure_red_cell)
    assert_close(summary["daily_iron_loading_mg_per_kg"], daily_iron)


def test_warning_labels() -> None:
    """Check that thin observation windows carry explicit warnings."""
    row = weekly_synthetic_rows()[0]
    summary = burden.summarize_rows([row])

    assert (
        "Only one transfusion row; interval cannot be calculated."
        in summary["warnings"]
    )
    assert (
        "Observation window is under 28 days; annualized values are noisy."
        in (summary["warnings"])
    )


def test_csv_validation() -> None:
    """Check missing columns and invalid numeric inputs."""
    expect_csv_error(
        "date,body_weight_kg,transfused_volume_ml\n2026-01-01,50,250\n",
        "CSV is missing required columns: red_cell_fraction.",
    )
    expect_csv_error(
        "date,body_weight_kg,transfused_volume_ml,red_cell_fraction\n"
        "2026-01-01,50,250,1.20\n",
        "`red_cell_fraction` must be between 0 and 1.",
    )
    expect_csv_error(
        "date,body_weight_kg,transfused_volume_ml,red_cell_fraction\n"
        "2026-01-01,0,250,0.65\n",
        "`body_weight_kg` must be a positive number.",
    )
    expect_csv_error(
        "date,body_weight_kg,transfused_volume_ml,red_cell_fraction\n"
        "2026-01-01,50,0,0.65\n",
        "`transfused_volume_ml` must be a positive number.",
    )


def main() -> int:
    """Run the transfusion burden self-tests."""
    test_weekly_synthetic_summary()
    test_warning_labels()
    test_csv_validation()
    print("transfusion burden self-tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
