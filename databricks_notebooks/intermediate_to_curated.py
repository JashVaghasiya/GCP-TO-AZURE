# Databricks notebook source
dbutils.widgets.text("intermediate_schema", "")
intermediate_schema = dbutils.widgets.get("intermediate_schema")

dbutils.widgets.text("curated_table", "")
curated_table = dbutils.widgets.get("curated_table")

dbutils.widgets.text("curated_schema", "")
curated_schema = dbutils.widgets.get("curated_schema")

dbutils.widgets.text("curated_query", "")
curated_query = dbutils.widgets.get("curated_query")

dbutils.widgets.text("LoadID", "")
LoadID = dbutils.widgets.get("LoadID")

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog unitycatalog_telecom

# COMMAND ----------

final_query = curated_query.format(intermediate_schema = intermediate_schema, curated_schema = curated_schema, curated_table = curated_table, LoadID = LoadID)
curated_df = spark.sql(final_query)

row_object = curated_df.collect()[0]
upserted_records = row_object.num_affected_rows

# COMMAND ----------

#return records to azure data factory
dbutils.notebook.exit(upserted_records)