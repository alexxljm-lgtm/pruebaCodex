-- SQL Server / T-SQL
CREATE TABLE dbo.IncidenciasRaw (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha DATE NULL,
    producto NVARCHAR(100) NOT NULL,
    estado NVARCHAR(30) NOT NULL,
    importe DECIMAL(18,2) NULL
);
GO

CREATE TABLE dbo.IncidenciasCuradas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha DATE NOT NULL,
    producto NVARCHAR(100) NOT NULL,
    estado NVARCHAR(30) NOT NULL,
    importe DECIMAL(18,2) NOT NULL,
    fecha_carga DATETIME2 NOT NULL DEFAULT SYSUTCDATETIME()
);
GO

CREATE VIEW dbo.vw_KPI_Incidencias AS
SELECT
    COUNT(*) AS total_registros,
    SUM(importe) AS importe_total,
    AVG(importe) AS importe_promedio
FROM dbo.IncidenciasCuradas;
GO
