from __future__ import annotations

from datetime import datetime, UTC


def build_lineage(source: str, target: str, process: str, owner: str = "cto_office") -> dict:
    return {
        "timestamp_utc": datetime.now(UTC).isoformat(),
        "source": source,
        "target": target,
        "process": process,
        "owner": owner,
        "tags": ["data-quality", "data-governance", "junior-showcase"],
    }
