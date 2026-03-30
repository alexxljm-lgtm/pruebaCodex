from __future__ import annotations

import argparse
import json

from data_governance_jr.orchestrator import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline junior de Data Governance")
    parser.add_argument("--input", required=False, help="Ruta al CSV/Excel de incidencias")
    args = parser.parse_args()

    result = run_pipeline(args.input)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
