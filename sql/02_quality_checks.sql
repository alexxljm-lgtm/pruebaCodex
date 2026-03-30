-- Reglas de calidad para SQL Server
SELECT COUNT(*) AS filas_con_fecha_nula
FROM dbo.IncidenciasRaw
WHERE fecha IS NULL;

SELECT COUNT(*) AS filas_importe_invalido
FROM dbo.IncidenciasRaw
WHERE importe IS NULL OR importe <= 0;

SELECT cliente_id, fecha, producto, estado, importe, COUNT(*) AS repeticiones
FROM dbo.IncidenciasRaw
GROUP BY cliente_id, fecha, producto, estado, importe
HAVING COUNT(*) > 1;
