from pyspark.sql.functions import col
df_result = employees.withColumn("bonus", col("salary") * 0.1)

df_result.show()