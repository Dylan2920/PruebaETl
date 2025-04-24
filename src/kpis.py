from pyspark.sql.functions import hour, avg, count, sum as spark_sum

def demanda_por_hora(df):
    return df.withColumn("hour", hour("tpep_pickup_datetime")).groupBy("hour").agg(
        count("*").alias("viajes"),
        avg("fare_amount").alias("tarifa_promedio")
    )

def eficiencia_por_zona(df):
    return df.groupBy("Zone").agg(
        spark_sum("fare_amount").alias("ingreso_total"),
        spark_sum("trip_distance").alias("distancia_total")
    )