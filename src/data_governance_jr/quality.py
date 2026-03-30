from __future__ import annotations

from dataclasses import dataclass, asdict

import pandas as pd


REQUIRED_COLUMNS = ["cliente_id", "fecha", "producto", "estado", "importe"]


@dataclass
class QualityMetrics:
    total_rows: int
    missing_required_values: int
    duplicated_rows: int
    invalid_amount_rows: int


def validate_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, QualityMetrics]:
    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Faltan columnas requeridas: {missing_columns}")

    cleaned = df.copy()
    cleaned["importe"] = pd.to_numeric(cleaned["importe"], errors="coerce")
    cleaned["fecha"] = pd.to_datetime(cleaned["fecha"], errors="coerce")

    missing_required_values = int(cleaned[REQUIRED_COLUMNS].isna().sum().sum())
    duplicated_rows = int(cleaned.duplicated().sum())
    invalid_amount_rows = int((cleaned["importe"].isna() | (cleaned["importe"] <= 0)).sum())

    curated = cleaned.drop_duplicates().dropna(subset=REQUIRED_COLUMNS)
    curated = curated[curated["importe"] > 0]

    metrics = QualityMetrics(
        total_rows=int(len(df)),
        missing_required_values=missing_required_values,
        duplicated_rows=duplicated_rows,
        invalid_amount_rows=invalid_amount_rows,
    )
    return curated, metrics


def metrics_to_dict(metrics: QualityMetrics) -> dict:
    return asdict(metrics)
