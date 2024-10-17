# Databricks notebook source
dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

dbutils.widgets.text("env", "")
env = dbutils.widgets.get("env")

# COMMAND ----------

spark.sql(f"create database if not exists hive_metastore.{env}_raw")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.dim_cities (

    city_code int,
    city_name string,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string
)
partitioned by (city_code)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/dim_cities'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.dim_date (

    dated string,
    month_name string,
    before_or_after_5g string,
    time_period int,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string
)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/dim_date'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.dim_plan (

    plan string,
    plan_description string,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string
)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/dim_plan'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.fact_metrics_share (

    dated string,
    city_code int,
    company string,
    company_revenue_crores double,
    arpu int,
    active_users_lakhs double,
    unsubscribed_users_lakhs double,
    seq_no int,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string    
)
partitioned by (city_code)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/fact_metrics_share'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.fact_market_share (

    dated string,
    city_code int,
    tmv_city_crores double,
    company string,
    ms_pct double,
    seq_no int,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string
)
partitioned by (city_code)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/fact_market_share'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_raw.fact_plan_revenue (

    dated string,
    city_code int,
    plan string,
    plan_revenue_crores double,
    seq_no int,
    last_inserted_dttm_azure timestamp, 
    last_updated_dttm_gcp string,
    load_id string    
)
partitioned by (city_code)
location 'abfss://raw@{storage_account_name}.dfs.core.windows.net/fact_plan_revenue'
""")
