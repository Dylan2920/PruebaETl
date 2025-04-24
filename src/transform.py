from pyspark.sql.functions import col

def clean_data(df):
    return df.filter(
        (col("tpep_pickup_datetime") < col("tpep_dropoff_datetime")) &
        (col("trip_distance") > 0) &
        (col("fare_amount") > 0)
def enrich_data(df, lookup_df):
    return df.join(lookup_df, df.PULocationID == lookup_df.LocationID, "left")