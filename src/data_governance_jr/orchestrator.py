from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from data_governance_jr.config import settings
from data_governance_jr.lineage import build_lineage
from data_governance_jr.quality import metrics_to_dict, validate_dataset
from data_governance_jr.rag import MiniRAG


def ensure_folders() -> None:
    for p in [settings.raw_data_path.parent, settings.rag_docs_path.parent]:
        p.mkdir(parents=True, exist_ok=True)


def _read_input(path: Path) -> pd.DataFrame:
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    return pd.read_csv(path)


def run_pipeline(raw_path: str | Path | None = None) -> dict:
    ensure_folders()
    path = Path(raw_path) if raw_path else settings.raw_data_path
    df = _read_input(path)

    curated, metrics = validate_dataset(df)
    curated.to_csv(settings.curated_data_path, index=False)

    quality_payload = metrics_to_dict(metrics)
    settings.quality_report_path.write_text(json.dumps(quality_payload, indent=2, ensure_ascii=False), encoding="utf-8")

    lineage = build_lineage(str(path), str(settings.curated_data_path), "raw_to_curated_csv")
    settings.lineage_path.write_text(json.dumps(lineage, indent=2, ensure_ascii=False), encoding="utf-8")

    rag = MiniRAG(settings.rag_docs_path)
    rag_preview = rag.ask("¿Qué validaciones de calidad son obligatorias?")

    return {
        "rows_curated": len(curated),
        "quality": quality_payload,
        "lineage": lineage,
        "rag_preview": rag_preview,
    }
