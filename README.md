# Proyecto Junior Data Governance (Portfolio)

Proyecto desde cero orientado a una vacante de **Técnico Junior Data** con foco en:

- **T-SQL / SQL Server**
- **Python** para pipelines
- **Excel/CSV** como fuente operativa
- **Power BI** (consumo de tabla curada)
- **IA Generativa + RAG** (mini demo)
- **IA Agéntica / orquestación de flujos**
- **Data Quality + Data Lineage**

## 1) Arquitectura propuesta

1. Ingesta de incidencias desde CSV o Excel (por defecto `data/incidencias_sample.csv`).
2. Validación de calidad de datos (campos obligatorios, importes, duplicados).
3. Publicación de dataset curado (`data/incidencias_curadas.csv`).
4. Registro de Data Lineage (`data/lineage.json`).
5. Consulta a mini-RAG para soporte funcional (`docs/knowledge_base.md`).

## 2) Estructura

- `src/data_governance_jr/quality.py`: reglas de calidad.
- `src/data_governance_jr/lineage.py`: metadatos de linaje.
- `src/data_governance_jr/rag.py`: RAG lightweight.
- `src/data_governance_jr/orchestrator.py`: flujo agéntico principal.
- `sql/01_schema_tsql.sql`: esquema SQL Server.
- `sql/02_quality_checks.sql`: checks de calidad en T-SQL.

## 3) Ejecutar

```bash
python -m pip install -e .
python -m data_governance_jr.cli --input data/incidencias_sample.csv
```

> También acepta `.xlsx` o `.xls` si quieres cargar un Excel real.

## 4) Resultado esperado

- `data/incidencias_curadas.csv`
- `data/quality_report.json`
- `data/lineage.json`
- salida en consola con `rag_preview`

## 5) Extensiones para entrevista

- Sustituir CSV por carga directa a SQL Server (`pyodbc`).
- Publicar un dashboard de Power BI con `vw_KPI_Incidencias`.
- Añadir motor LLM real (Azure OpenAI + embeddings + vector DB).
- Incorporar script VB.NET para extracción legacy en ecosistema Microsoft.
