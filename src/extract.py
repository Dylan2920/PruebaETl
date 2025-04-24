from pyspark.sql import SparkSession

def extract_data(spark, input_path):
    return spark.read.parquet(input_path)

def load_lookup_table(spark, csv_path):
    return spark.read.csv(csv_path, header=True, inferSchema=True)