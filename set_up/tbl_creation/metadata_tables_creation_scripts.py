# Databricks notebook source
dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

# COMMAND ----------

# MAGIC %sql
# MAGIC create database if not exists hive_metastore.metadata_schema

# COMMAND ----------

#tbl_source_control metadata table holds the parameters values for various connections
spark.sql(f"""
create or replace table metadata_schema.tbl_source_control (

    gcp_source_bucket string,
    storage_account string,
    adls_url string,
    container_name string,
    logic_app_url string,
    email_id string
)
location 'abfss://metadata@{storage_account_name}.dfs.core.windows.net/tbl_source_control'
""")

# COMMAND ----------

# tbl_parameters holds the parameter values of DDL
spark.sql(f"""
create or replace table metadata_schema.tbl_parameters (

    job_id int,
    source_file_path string,
    watermark_column timestamp,
    raw_schema string,
    raw_tbl string,
    intermediate_schema string,
    intermediate_tbl string,
    intermediate_query string,
    curated_schema string,
    curated_tbl string,
    curated_query string
)
location 'abfss://metadata@{storage_account_name}.dfs.core.windows.net/tbl_parameters'
""")
