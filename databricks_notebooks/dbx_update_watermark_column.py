# Databricks notebook source
dbutils.widgets.text("job_id", "")
job_id = dbutils.widgets.get("job_id")

dbutils.widgets.text("gcp_file_last_modified_time", "")
gcp_file_last_modified_time = dbutils.widgets.get("gcp_file_last_modified_time")

# COMMAND ----------

#updating the watermark column
spark.sql(f"""
    update metadata_schema.tbl_parameters set watermark_column = '{gcp_file_last_modified_time}' where job_id = '{job_id}'
""")