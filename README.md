# NYC Taxi ETL Pipeline

Este proyecto implementa un pipeline ETL utilizando PySpark para procesar datos de taxis amarillos de NYC. El objetivo es aplicar la arquitectura de medallón (Raw → Trusted → Refined), generar KPIs útiles y asegurar observabilidad y manejo de errores.

---

## 📁 Estructura del Proyecto

```
nyc-taxi-etl/
├── data/
│   ├── lookup/              # CSV de zonas (Taxi Zone Lookup)
│   ├── raw/                 # Datos crudos
│   ├── trusted/             # Datos limpios/enriquecidos
│   └── refined/             # Resultados agregados (KPIs)
├── logs/                    # Logs y reporte JSON
├── src/                     # Código fuente del pipeline
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto
```

---

## 🛠️ Requisitos Previos

- Python 3.7+
- PySpark

Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## 📥 Datos de Entrada

1. **Archivo de datos:**
   - [yellow_tripdata_2022-01.parquet](https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.parquet)
   - Guardar en `data/`

2. **Tabla de zonas:**
   - [taxi_zone_lookup.csv](https://www.nyc.gov/assets/tlc/downloads/pdf/taxi_zone_lookup.csv)
   - Guardar en `data/lookup/` como `taxi+_zone_lookup.csv`

---

## 🚀 Cómo ejecutar el pipeline

Desde la raíz del proyecto:

```bash
spark-submit src/main.py
```

---

## 📊 KPIs Generados

- **Demanda por hora:** cantidad de viajes y tarifa promedio por hora del día.
- **Eficiencia por zona:** ingreso total y distancia total recorrida por zona.
- **Impacto de la calidad:** cantidad de registros descartados y tiempo de ejecución total.

---

## 🧾 Archivos de salida

- Datos procesados en `data/raw`, `data/trusted`, `data/refined`
- Logs del pipeline en `logs/etl.log`
- Reporte de ejecución en `logs/reporte.json`

---

## 📌 Observabilidad

- Logs informativos y de error
- Reporte automático en JSON
- Uso de `try/except` para manejo de errores críticos

---

## 📚 Créditos

Fuente de datos: [NYC Taxi and Limousine Commission](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

---

## ✅ Estado del Proyecto

✔️ Implementación completa del pipeline ETL con PySpark y arquitectura de medallón.
✔️ Validación, enriquecimiento, KPIs y logging automático.

