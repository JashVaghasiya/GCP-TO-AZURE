# Databricks notebook source
dbutils.widgets.text("loadId", "")
loadId = dbutils.widgets.get("loadId")

dbutils.widgets.text("source_file_name", "")
source_file_name = dbutils.widgets.get("source_file_name")

dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

dbutils.widgets.text("container", "")
container = dbutils.widgets.get("container")

# COMMAND ----------

adls_source_file_path = f"abfss://{container}@{storage_account_name}.dfs.core.windows.net/{source_file_name}"
adls_archive_file_path = f"abfss://{container}@{storage_account_name}.dfs.core.windows.net/archive/{source_file_name}_{loadId}"

# COMMAND ----------

#move source file to archive location
dbutils.fs.mv(adls_source_file_path,adls_archive_file_path)