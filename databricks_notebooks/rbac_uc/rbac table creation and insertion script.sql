-- Databricks notebook source
--metadata table for AAD groups names 
create table if not exists hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups (aad_group_name string, env string, access_type string, access_status string)
LOCATION 'abfss://raw@csadlsgen2storageacc24.dfs.core.windows.net/tbl_rbac_uc_aad_groups'

-- COMMAND ----------

--TRUNCATE TABLE hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups

-- COMMAND ----------

-- metadata RBAC and UC Insert values  
INSERT INTO hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups values ('AAD_TELECOM_DE','dev','UC_ALL_PRIVILEGES', 'grant');
INSERT INTO hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups values ('AAD_TELECOM_REPORT','dev','UC_CUR_READ', 'grant');
INSERT INTO hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups values ('AAD_TELECOM_TESTING','dev','UC_ALL_READ', 'grant');

-- COMMAND ----------

--DELETE FROM hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups WHERE aad_group_name='Group A'

-- COMMAND ----------

select * from hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups;

-- COMMAND ----------

update hive_metastore.metadata_schema.tbl_rbac_uc_aad_groups set access_status='grant' where aad_group_name='AAD_TELECOM_REPORT'

-- COMMAND ----------

--metadata table for curated tables name
create table hive_metastore.metadata_schema.tbl_rbac_uc_table_names (aad_group_name string, table_name string, access_status string)
USING delta LOCATION 'abfss://raw@csadlsgen2storageacc24.dfs.core.windows.net/tbl_rbac_uc_table_names'

-- COMMAND ----------

-- MAGIC %python
-- MAGIC file_path = 'abfss://landing@csadlsgen2storageacc24.dfs.core.windows.net/rbac_uc_tables/rbac_tables_access_list.csv'
-- MAGIC df = spark.read.load(file_path,format='csv',header='True')
-- MAGIC df.write.mode("overwrite").format("delta").saveAsTable("hive_metastore.metadata_schema.tbl_rbac_uc_table_names")

-- COMMAND ----------

select * from hive_metastore.metadata_schema.tbl_rbac_uc_table_names

-- COMMAND ----------

update hive_metastore.metadata_schema.tbl_rbac_uc_table_names set table_name='dim_cities'