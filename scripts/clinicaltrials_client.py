"""Small ClinicalTrials.gov API v2 client for reproducible research snapshots."""

from __future__ import annotations

import json
import pathlib
import sys
from typing import Any
import urllib.error
import urllib.parse
import urllib.request


API_ROOT = "https://clinicaltrials.gov/api/v2"


def get_object(source: dict[str, Any], key: str) -> dict[str, Any]:
    """Return a nested JSON object, or an empty object when the shape differs."""
    value = source.get(key)
    if isinstance(value, dict):
        return value

    return {}


def get_list(source: dict[str, Any], key: str) -> list[Any]:
    """Return a nested JSON list, or an empty list when the shape differs."""
    value = source.get(key)
    if isinstance(value, list):
        return value

    return []


def collect_strings(items: list[Any], key: str) -> list[str]:
    """Collect string values from a list of ClinicalTrials.gov JSON objects."""
    values: list[str] = []

    for item in items:
        if not isinstance(item, dict):
            continue

        value = item.get(key)
        if isinstance(value, str) and value:
            values.append(value)

    return values


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
    protocol = get_object(study, "protocolSection")
    identification = get_object(protocol, "identificationModule")
    status = get_object(protocol, "statusModule")
    design = get_object(protocol, "designModule")
    interventions = get_object(protocol, "armsInterventionsModule")
    contacts = get_object(protocol, "contactsLocationsModule")
    outcomes = get_object(protocol, "outcomesModule")

    countries = sorted(set(collect_strings(get_list(contacts, "locations"), "country")))
    intervention_names = collect_strings(
        get_list(interventions, "interventions"),
        "name",
    )
    primary_outcomes = collect_strings(
        get_list(outcomes, "primaryOutcomes"),
        "measure",
    )

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
        for study in get_list(payload, "studies"):
            if isinstance(study, dict):
                records.append(compact_study(study))
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
