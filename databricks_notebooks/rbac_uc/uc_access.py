# Databricks notebook source
#creating widget to get parameters from ADF

dbutils.widgets.text("aad_group_name","")
dbutils.widgets.text("env","")
dbutils.widgets.text("access_type","")
dbutils.widgets.text("access_status","")


# COMMAND ----------

#creating varibale

env= dbutils.widgets.get("env")
aad_group_name=dbutils.widgets.get("aad_group_name")
access_type= dbutils.widgets.get("access_type");
access_status= dbutils.widgets.get("access_status");

# COMMAND ----------


#update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status='revoke' where 
 #aad_group_name= 'AAD_TELECOM_REPORT' and env='dev'

# COMMAND ----------

#grant or revoke permissions to the different AAD groups UC access
# UC_ALL_READ = Read access on all the schemas 
if((f"{access_status}"=='grant') and (f"{access_type}"=='UC_ALL_READ')):
    #ON UNITY CATALOG
    #catalog level
    spark.sql(f"grant USE CATALOG on CATALOG unitycatalog_telecom to `{aad_group_name}`")
    #schema level
    spark.sql(f"grant USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_raw to `{aad_group_name}`")
    spark.sql(f"grant REFRESH on SCHEMA unitycatalog_telecom.{env}_raw to `{aad_group_name}`")
    spark.sql(f"grant SELECT on SCHEMA unitycatalog_telecom.{env}_raw to `{aad_group_name}`")
    spark.sql(f"grant USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_intermediate to `{aad_group_name}`")
    spark.sql(f"grant REFRESH on SCHEMA unitycatalog_telecom.{env}_intermediate to `{aad_group_name}`")
    spark.sql(f"grant SELECT on SCHEMA unitycatalog_telecom.{env}_intermediate to `{aad_group_name}`")
    spark.sql(f"grant USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"grant REFRESH on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"grant SELECT on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")
    #updating access status in metadata table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status='granted' where 
    aad_group_name= '{aad_group_name}' and env='{env}' """)

#for revoking access
elif((f"{access_status}"=='revoke') and (f"{access_type}"=='UC_ALL_READ')):
    #catalog level
    spark.sql(f"revoke USE CATALOG on CATALOG unitycatalog_telecom from `{aad_group_name}`")
    #schema level
    spark.sql(f"revoke USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_raw from `{aad_group_name}`")
    spark.sql(f"revoke REFRESH on SCHEMA unitycatalog_telecom.{env}_raw from `{aad_group_name}`")
    spark.sql(f"revoke SELECT on SCHEMA unitycatalog_telecom.{env}_raw from `{aad_group_name}`")
    spark.sql(f"revoke USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_intermediate from `{aad_group_name}`")
    spark.sql(f"revoke REFRESH on SCHEMA unitycatalog_telecom.{env}_intermediate from `{aad_group_name}`")
    spark.sql(f"revoke SELECT on SCHEMA unitycatalog_telecom.{env}_intermediate from `{aad_group_name}`")
    spark.sql(f"REVOKE USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"revoke REFRESH on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"revoke SELECT on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")
    #updating access status in metadata table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status= 'revoked' where 
    aad_group_name='{aad_group_name}' and env='{env}' """)

# COMMAND ----------

#grant & revoke access to diffrent AAD Group Curated limited tables access 
#UC_CUR_READ = Read access on curated schema only
if((f"{access_status}"=='grant') and (f"{access_type}"=='UC_CUR_READ')):
#catalog level
    spark.sql(f"grant USE CATALOG on CATALOG unitycatalog_telecom to `{aad_group_name}`")
#schema level
    spark.sql(f"grant USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"grant REFRESH on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"grant SELECT on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")

#updating in metadata schema table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status= 'granted' where 
    aad_group_name='{aad_group_name}' and env='{env}' """)
elif((f"{access_status}"=='revoke') and (f"{access_type}"=='UC_CUR_READ')):
#catalog level
    spark.sql(f"revoke USE CATALOG on CATALOG unitycatalog_telecom from `{aad_group_name}`")
#schema level
    spark.sql(f"revoke USE SCHEMA on SCHEMA unitycatalog_telecom.{env}_curated from `{aad_group_name}`")
    spark.sql(f"revoke REFRESH on SCHEMA unitycatalog_telecom.{env}_curated from `{aad_group_name}`")
    spark.sql(f"revoke SELECT on SCHEMA unitycatalog_telecom.{env}_curated from `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")  
#updating in metadata schema table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status= 'revoked' where 
    aad_group_name='{aad_group_name}' and env='{env}' """)

# COMMAND ----------

#grant & revoke access to diffrent AAD Group Curated limited tables access 
#UC_CUR_READ = Read access on curated schema only
if((f"{access_status}"=='grant') and (f"{access_type}"=='UC_ALL_PRIVILEGES')):
#catalog level
    spark.sql(f"grant USE CATALOG on CATALOG unitycatalog_telecom to `{aad_group_name}`")
#schema level
    spark.sql(f"grant ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_curated to `{aad_group_name}`")
    spark.sql(f"grant ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_intermediate to `{aad_group_name}`")
    spark.sql(f"grant ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_raw to `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")

#updating in metadata schema table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status= 'granted' where 
    aad_group_name='{aad_group_name}' and env='{env}' """)
elif((f"{access_status}"=='revoke') and (f"{access_type}"=='UC_ALL_PRIVILEGES')):
#catalog level
    spark.sql(f"revoke USE CATALOG on CATALOG unitycatalog_telecom from `{aad_group_name}`")
#schema level
    spark.sql(f"revoke ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_curated from `{aad_group_name}`")
    spark.sql(f"revoke ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_intermediate from `{aad_group_name}`")
    spark.sql(f"revoke ALL PRIVILEGES on SCHEMA unitycatalog_telecom.{env}_raw to `{aad_group_name}`")
    print(f"{access_status} if block is executed [{access_type}]")  
#updating in metadata schema table 
    spark.sql(f"""update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status= 'revoked' where 
    aad_group_name='{aad_group_name}' and env='{env}' """)