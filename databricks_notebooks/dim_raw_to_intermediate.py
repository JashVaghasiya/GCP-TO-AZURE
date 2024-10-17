# Databricks notebook source
dbutils.widgets.text("raw_table", "")
raw_table = dbutils.widgets.get("raw_table")

dbutils.widgets.text("raw_schema", "")
raw_schema = dbutils.widgets.get("raw_schema")

dbutils.widgets.text("intermediate_table", "")
intermediate_table = dbutils.widgets.get("intermediate_table")

dbutils.widgets.text("intermediate_schema", "")
intermediate_schema = dbutils.widgets.get("intermediate_schema")

dbutils.widgets.text("gcp_file_last_modified_time", "")
gcp_file_last_modified_time = dbutils.widgets.get("gcp_file_last_modified_time")

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog unitycatalog_telecom

# COMMAND ----------

raw_df = spark.sql(f"select * from {raw_schema}.{raw_table}")
raw_table_records_count = raw_df.count()

#creating temporary view from the raw_df dataframe
raw_df.createOrReplaceTempView('temp_view')

# COMMAND ----------

#insert records into intermediate layer table
intermediate_df = spark.sql(f"""
          
    insert overwrite {intermediate_schema}.{intermediate_table} select * from temp_view;
""")

row_object = intermediate_df.collect()[0]
intermediate_tbl_records_count = row_object.num_affected_rows

# COMMAND ----------

#return records to azure data factory
dbutils.notebook.exit([raw_table_records_count, intermediate_tbl_records_count])