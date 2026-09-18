from pyspark.sql.functions import col
df_result = employees.filter(col("salary") > 55000)
df_result.show()