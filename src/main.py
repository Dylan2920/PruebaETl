import time
import json
from pyspark.sql import SparkSession
from src.extract import extract_data, load_lookup_table
from src.transform import clean_data, enrich_data
from src.load import save_data
from src.kpis import demanda_por_hora, eficiencia_por_zona
from src.observability import init_logger, log_event

if __name__ == "__main__":
    spark = SparkSession.builder.appName("NYC Taxi ETL").getOrCreate()
    logger = init_logger()
    start_time = time.time()

    try:
        # Rutas
        raw_path = "data/yellow_tripdata_2022-01.parquet"
        lookup_path = "data/lookup/taxi+_zone_lookup.csv"

        # Extracción
        df_raw = extract_data(spark, raw_path)
        df_lookup = load_lookup_table(spark, lookup_path)

        log_event(logger, f"Registros extraídos: {df_raw.count()}")

        # Transformación
        df_clean = clean_data(df_raw)
        df_enriched = enrich_data(df_clean, df_lookup)

        log_event(logger, f"Registros después de limpieza: {df_clean.count()}")

        # Carga intermedia
        save_data(df_raw, "data/raw")
        save_data(df_enriched, "data/trusted")

        # KPIs
        df_demand = demanda_por_hora(df_enriched)
        df_efficiency = eficiencia_por_zona(df_enriched)

        save_data(df_demand, "data/refined/demanda")
        save_data(df_efficiency, "data/refined/eficiencia")

        # Reporte
        report = {
            "registros_originales": df_raw.count(),
            "registros_limpios": df_clean.count(),
            "descartados": df_raw.count() - df_clean.count(),
            "tiempo_ejecucion": round(time.time() - start_time, 2)
        }
        with open("logs/reporte.json", "w") as f:
            json.dump(report, f, indent=4)

        log_event(logger, "Ejecución finalizada correctamente")

    except Exception as e:
        logger.error(f"Error durante el pipeline: {str(e)}")
