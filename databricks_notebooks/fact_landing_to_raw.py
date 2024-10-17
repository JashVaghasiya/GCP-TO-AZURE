# Databricks notebook source
dbutils.widgets.text("raw_table", "")
raw_table = dbutils.widgets.get("raw_table")

dbutils.widgets.text("raw_schema", "")
raw_schema = dbutils.widgets.get("raw_schema")

dbutils.widgets.text("source_file_name", "")
source_file_name = dbutils.widgets.get("source_file_name")

dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

dbutils.widgets.text("LoadID", "")
LoadID = dbutils.widgets.get("LoadID")

dbutils.widgets.text("container", "")
container = dbutils.widgets.get("container")

dbutils.widgets.text("gcp_file_last_modified_time", "")
gcp_file_last_modified_time = dbutils.widgets.get("gcp_file_last_modified_time")

# COMMAND ----------

# MAGIC %sql
# MAGIC use catalog unitycatalog_telecom

# COMMAND ----------

#extracting schema from the raw table
table_schema = ""
df = spark.sql(f"describe {raw_schema}.{raw_table}").collect()

for i in range(0, len(df)):
    col_name = df[i]['col_name']
    col_data_type = df[i]['data_type']
    
    if(col_name == "last_inserted_dttm_azure"):
        break
    
    table_schema = table_schema + col_name +" " + col_data_type + ","
    
table_schema = table_schema[:-1]

# COMMAND ----------

#storing source_file data in a dataframe
file_path = f"abfss://{container}@{storage_account_name}.dfs.core.windows.net/{source_file_name}"

df = spark.read.format("csv").\
     option("header","true").\
     option("mode","permissive").\
     schema(table_schema).\
     load(file_path)

#dropping rows that contains all null records
df_no_null = df.na.drop("all")

#dropping duplicate rows
df_no_null_no_duplicates = df_no_null.dropDuplicates()

source_file_records_count = df.count()

#creating temporary view from the df dataframe
df_no_null_no_duplicates.createOrReplaceTempView('temp_view')

# COMMAND ----------

#insert records into raw layer table
spark.sql(f"""
          
    insert overwrite {raw_schema}.{raw_table} select *, from_utc_timestamp(now(), 'IST'), '{gcp_file_last_modified_time}','{LoadID}' from temp_view;
""")

# COMMAND ----------

raw_tbl_count = spark.sql(f"select * from {raw_schema}.{raw_table}").count()

# COMMAND ----------

#return records to azure data factory
dbutils.notebook.exit([source_file_records_count, raw_tbl_count])