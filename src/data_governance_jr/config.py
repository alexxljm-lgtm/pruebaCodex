from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    project_root: Path = Path(__file__).resolve().parents[2]
    raw_data_path: Path = project_root / "data" / "incidencias_sample.csv"
    curated_data_path: Path = project_root / "data" / "incidencias_curadas.csv"
    quality_report_path: Path = project_root / "data" / "quality_report.json"
    lineage_path: Path = project_root / "data" / "lineage.json"
    rag_docs_path: Path = project_root / "docs" / "knowledge_base.md"


settings = Settings()
