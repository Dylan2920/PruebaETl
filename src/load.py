def save_data(df, path):
    df.write.mode("overwrite").parquet(path)