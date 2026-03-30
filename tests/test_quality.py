import pandas as pd

from data_governance_jr.quality import validate_dataset


def test_validate_dataset_filters_invalid_rows():
    df = pd.DataFrame(
        [
            {"cliente_id": 1, "fecha": "2026-01-01", "producto": "A", "estado": "ok", "importe": 10},
            {"cliente_id": 1, "fecha": "2026-01-01", "producto": "A", "estado": "ok", "importe": 10},
            {"cliente_id": 2, "fecha": None, "producto": "B", "estado": "ok", "importe": 5},
            {"cliente_id": 3, "fecha": "2026-01-02", "producto": "C", "estado": "ok", "importe": -1},
        ]
    )

    curated, metrics = validate_dataset(df)

    assert len(curated) == 1
    assert metrics.duplicated_rows == 1
    assert metrics.invalid_amount_rows == 1
