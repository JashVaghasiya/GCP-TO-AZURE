# Databricks notebook source
dbutils.widgets.text("storage_account_name", "")
storage_account_name = dbutils.widgets.get("storage_account_name")

dbutils.widgets.text("env", "")
env = dbutils.widgets.get("env")

# COMMAND ----------

spark.sql(f"create database if not exists hive_metastore.{env}_curated")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_curated.metrics_share (
    
    before_or_after_5g string,
    city_name string,
    month_name string,
    time_period int,
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
location 'abfss://curated@{storage_account_name}.dfs.core.windows.net/metrics_share'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_curated.market_share (

    before_or_after_5g string,
    city_name string,
    month_name string,
    time_period int,
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
location 'abfss://curated@{storage_account_name}.dfs.core.windows.net/market_share'
""")

# COMMAND ----------

spark.sql(f"""
create or replace table {env}_curated.plan_revenue (

    before_or_after_5g string,
    city_name string,
    month_name string,
    time_period int,
    plan_description string,
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
location 'abfss://curated@{storage_account_name}.dfs.core.windows.net/plan_revenue'
""")
