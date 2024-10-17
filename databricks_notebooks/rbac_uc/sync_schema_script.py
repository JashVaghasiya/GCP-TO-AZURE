# Databricks notebook source
#creating widgets
dbutils.widgets.text("sync_schema_yes_or_no","")
dbutils.widgets.text("env","")

# COMMAND ----------

#creating variables 
sync_schema_yes_or_no= dbutils.widgets.get("sync_schema_yes_or_no")
env= dbutils.widgets.get("env");

# COMMAND ----------

#creating managed schema's in UC 

spark.sql(f"create schema IF NOT EXISTS unitycatalog_telecom.{env}_raw");
spark.sql(f"create schema IF NOT EXISTS unitycatalog_telecom.{env}_intermediate");
spark.sql(f"create schema IF NOT EXISTS unitycatalog_telecom.{env}_curated");
spark.sql(f"create schema IF NOT EXISTS unitycatalog_telecom.metadata_schema");

# COMMAND ----------

#sync schema from hive metatsore to unity catalog

if(f"{sync_schema_yes_or_no}"=='yes'):
    spark.sql(f"sync schema unitycatalog_telecom.{env}_raw from hive_metastore.{env}_raw") 
    spark.sql(f"sync schema unitycatalog_telecom.{env}_intermediate from hive_metastore.{env}_intermediate")
    spark.sql(f"sync schema unitycatalog_telecom.{env}_curated from hive_metastore.{env}_curated")
    spark.sql(f"sync schema unitycatalog_telecom.metadata_schema from hive_metastore.metadata_schema")
    print("Sync Schema completed")
else:
    print("SYNC Schema not executed")   