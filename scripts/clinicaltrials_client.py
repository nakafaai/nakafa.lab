"""Small ClinicalTrials.gov API v2 client for reproducible research snapshots."""

from __future__ import annotations

import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


API_ROOT = "https://clinicaltrials.gov/api/v2"
STUDY_FIELDS = (
    "NCTId",
    "BriefTitle",
    "OverallStatus",
    "LastUpdatePostDate",
    "Phase",
    "InterventionName",
    "LocationCountry",
)


def read_request() -> dict[str, Any]:
    """Read one JSON request object from standard input."""
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON input: {error}") from error

    if not isinstance(payload, dict):
        raise ValueError("Input must be a JSON object.")

    return payload


def build_url(path: str, params: dict[str, Any] | None = None) -> str:
    """Build a ClinicalTrials.gov API URL with encoded query parameters."""
    url = f"{API_ROOT}/{path.lstrip('/')}"
    if not params:
        return url

    query = urllib.parse.urlencode(
        {key: value for key, value in params.items() if value not in (None, "")}
    )
    return f"{url}?{query}" if query else url


def fetch_json(url: str, timeout_sec: int) -> dict[str, Any]:
    """Fetch a JSON response from ClinicalTrials.gov."""
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "nakafa.lab/0.1"},
    )

    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        payload = json.load(response)

    if not isinstance(payload, dict):
        raise ValueError("ClinicalTrials.gov response was not a JSON object.")

    return payload


def compact_study(study: dict[str, Any]) -> dict[str, Any]:
    """Convert one full study payload into the fields used by research notes."""
    protocol = study.get("protocolSection", {})
    identification = protocol.get("identificationModule", {})
    status = protocol.get("statusModule", {})
    design = protocol.get("designModule", {})
    interventions = protocol.get("armsInterventionsModule", {})
    contacts = protocol.get("contactsLocationsModule", {})
    outcomes = protocol.get("outcomesModule", {})

    locations = contacts.get("locations", [])
    countries = sorted(
        {
            location.get("country")
            for location in locations
            if isinstance(location, dict) and location.get("country")
        }
    )
    intervention_names = [
        item.get("name")
        for item in interventions.get("interventions", [])
        if isinstance(item, dict) and item.get("name")
    ]
    primary_outcomes = [
        item.get("measure")
        for item in outcomes.get("primaryOutcomes", [])
        if isinstance(item, dict) and item.get("measure")
    ]

    return {
        "nct_id": identification.get("nctId"),
        "title": identification.get("briefTitle"),
        "status": status.get("overallStatus"),
        "last_update": status.get("lastUpdatePostDateStruct", {}).get("date"),
        "phases": design.get("phases", []),
        "interventions": intervention_names,
        "countries": countries,
        "primary_outcomes": primary_outcomes,
    }


def studies_response(request: dict[str, Any]) -> dict[str, Any]:
    """Fetch one or more compact study-search pages."""
    params = dict(request.get("params", {}))
    max_items = int(request.get("max_items", 10))
    max_pages = int(request.get("max_pages", 1))
    timeout_sec = int(request.get("timeout_sec", 30))
    records: list[dict[str, Any]] = []
    pages_fetched = 0
    next_page_token = None
    total_count = None
    payload: dict[str, Any] = {}

    for _ in range(max_pages):
        url = build_url("studies", params)
        payload = fetch_json(url, timeout_sec)
        pages_fetched += 1
        if total_count is None:
            total_count = payload.get("totalCount")
        records.extend(compact_study(study) for study in payload.get("studies", []))
        next_page_token = payload.get("nextPageToken")

        if not next_page_token or len(records) >= max_items:
            break

        params["pageToken"] = next_page_token

    return {
        "ok": True,
        "query_url": build_url("studies", request.get("params", {})),
        "pages_fetched": pages_fetched,
        "next_page_token": next_page_token,
        "total_count": total_count,
        "records": records[:max_items],
    }


def request_response(request: dict[str, Any]) -> dict[str, Any]:
    """Fetch an arbitrary API path for targeted metadata or study details."""
    path = str(request.get("path", "")).strip()
    if not path:
        raise ValueError("action=request requires a non-empty path.")

    timeout_sec = int(request.get("timeout_sec", 30))
    return {
        "ok": True,
        "query_url": build_url(path, request.get("params", {})),
        "payload": fetch_json(build_url(path, request.get("params", {})), timeout_sec),
    }


def write_output(response: dict[str, Any], request: dict[str, Any]) -> None:
    """Write JSON to stdout and optionally save the same payload to disk."""
    if request.get("save_raw"):
        raw_output_path = request.get("raw_output_path")
        if not raw_output_path:
            raise ValueError("save_raw=true requires raw_output_path.")

        output_path = pathlib.Path(str(raw_output_path))
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            f"{json.dumps(response, indent=2, sort_keys=True)}\n",
            encoding="utf-8",
        )

    print(json.dumps(response, indent=2, sort_keys=True))


def run(request: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a supported ClinicalTrials.gov request action."""
    action = request.get("action")

    if action == "studies":
        return studies_response(request)

    if action in {"metadata", "search_areas", "enums"}:
        path = {"metadata": "studies/metadata"}.get(action, str(action))
        return request_response({"action": "request", "path": path, **request})

    if action == "request":
        return request_response(request)

    raise ValueError(f"Unsupported action: {action!r}")


def main() -> int:
    """Run the command-line client."""
    try:
        request = read_request()
        write_output(run(request), request)
    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print(json.dumps({"ok": False, "error": str(error)}, indent=2), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
