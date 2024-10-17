---

# **Data Engineering Project: Cloud Data Pipeline between Google Cloud and Azure**

![architecture](https://github.com/user-attachments/assets/f56c8e56-1a51-45a1-ade9-66e05024ff5b)


## Project Overview

This project involves building large-scale data pipelines to migrate, process, and govern data between **Google Cloud** and **Azure**. The solution utilizes:

- **Azure Data Factory (ADF)**
- **Databricks**
- **Azure Blob Storage**
- **Self-hosted Integration Runtime (SHIR)**
- **Azure Key Vault**

This project incorporates robust **logging mechanisms**, **parameterization**, **role-based access control (RBAC)** with **Unity Catalog**, and secure credential management.

## 🚀 Key Features

- **Scalable Pipelines**: Parameterized for dynamic management of various data sources and tables.
- **Data Security & Governance**: Integrated RBAC using **Unity Catalog** connected to **Azure Active Directory (AAD)** for seamless access control.
- **Robust Logging**: Real-time logging and monitoring to track every step of the pipeline.
- **End-to-End Automation**: Automates data migration, transformation, and access management between Google Cloud and Azure.
- **Watermark Column Usage**: The **watermark_column** is crucial for incremental data loading, allowing the system to track the latest processed timestamp and ensuring that only new or updated data is processed. This minimizes data duplication and optimizes data transfer efficiency.

---

## 📋 Main Pipelines

### 1. Dimensional Data Pipelines

![Screenshot 2024-10-17 160144](https://github.com/user-attachments/assets/c9116281-5b21-4ce0-83bd-e4b0aabd78e0)


#### **Pipeline 1: `1a_pl_dim_gcp_to_azure_full_load`**
- **Activities**:
  - **Lookup Metadata**: Fetches parameters and control data for the job.
  - **Get Metadata**: Retrieves file metadata from a Google Cloud Storage (GCP) bucket.
  - **File Count Check**: Verifies if there are files to process.
  - **Format Validation**: Filters files based on their names (must start with "telecom_dim" and end with ".csv").
  - **Watermark Column**: Utilizes the **watermark_column** to manage incremental loading, ensuring only new or updated data is processed.
  - **File Processing Loop**: Loops through valid files, copying them to Azure Blob Storage.
  - **Logging and Alerts**: Logs success or failure during each step and sends email alerts.

![for_each_loop](https://github.com/user-attachments/assets/3df44531-0103-4cd9-8500-901b2b659c02)


#### **Pipeline 2: `1b_pl_dim_sub_landing_to_raw_full_load`**
- **Activities**:
  - **Data Processing**: Executes a Databricks notebook to move data from the landing zone in Azure to the raw layer.
  - **Watermark Column**: Ensures data is processed incrementally by tracking the latest processed timestamp.
  - **Logging**: Logs the success or failure of the data movement.
  - **Failure Alerts**: Sends email alerts if the data processing fails.

![landing_to_raw](https://github.com/user-attachments/assets/222249ba-17f9-4fd5-acd7-a3e725d6da7e)


#### **Pipeline 3: `1c_pl_dim_raw_to_intermediate`**
- **Activities**:
  - **Data Processing**: Executes a Databricks notebook to transfer data from the raw layer to the intermediate layer.
  - **Logging**: Logs the success or failure of data processing.
  - **Failure Alerts**: Sends email notifications if there is a failure during the processing.

![raw_to_intermediate](https://github.com/user-attachments/assets/131d5115-3568-4f8b-bf2d-3fdfc8ad272d)


---

### 2. Fact Data Pipelines

The same structure is applied to fact tables, with adjustments for delta loading in notebook and if condition in pipeline.

#### **Pipeline 1: `2a_pl_fact_gcp_to_azure_delta_load`**
- **Activities**:
  - **Lookup Metadata**: Fetches parameters specific to fact tables.
  - **Get Metadata**: Retrieves file metadata from the GCP bucket where fact tables are stored.
  - **File Count Check**: Verifies if any fact table files are available to process.
  - **File Format Validation**: Ensures fact table files have the correct format (e.g., "fact_*" and CSV or Parquet).
  - **Watermark Column**: Utilizes the **watermark_column** for managing incremental data loading specific to fact tables.
  - **File Processing Loop**: Iterates through the files and copies them from GCP to Azure Blob Storage.
  - **Logging**: Logs the success or failure of each file transfer and processing step.
  - **Email Alerts**: Notifies on pipeline status.

#### **Pipeline 2: `2b_pl_fact_landing_to_raw_delta_load`**
- **Activities**:
  - **Data Processing**: Executes a Databricks notebook to load fact table data from the landing zone to the raw data layer.
  - **Logging**: Logs details of the records processed and any failures.
  - **Failure Alerts**: Sends email alerts if the loading process encounters an issue.

#### **Pipeline 3: `2c_pl_fact_raw_to_intermediate_delta_load`**
- **Activities**:
  - **Data Processing**: Processes fact table data from the raw layer to the intermediate layer using a Databricks notebook.
  - **Logging**: Records details of the inserted records and captures any errors during the process.
  - **Email Alerts**: Notifies the team if the pipeline fails or succeeds.

---

### 3. Curated Data Pipelines

#### **Pipeline: `3_pl_intermediate_to_curated`**
- **Activities**:
  - **Metadata Lookup**: Retrieves job metadata using a SQL query.
  - **Intermediate to Curated Ingestion**: Executes a Databricks notebook to handle the data transfer from the intermediate to the curated layer.
  - **Success Logging**: Logs the success of the ingestion.
  - **Failure Logging**: Captures any error messages if the ingestion fails.

![intermediate_to_curated](https://github.com/user-attachments/assets/724fa1ba-dd6e-4250-b97f-b7035d0e4506)

---

## 📋 Metadata Tables Explanation

### 1. **tbl_parameters**
   - Stores configuration parameters for pipeline management, including job IDs, file paths, schema names, and queries for each layer.
   - **watermark_column**: Important for incremental loading, allowing the system to track processed timestamps.
     
### 2. **source_control**
   - Holds metadata that controls external sources and storage locations, including GCP bucket names and Azure Data Lake URLs.

### 3. **tbl_rbac_uc_aad_groups**
   - Manages group permissions for AAD, detailing access types and statuses for data governance.

### 4. **log_record_tbl**
   - Used for logging pipeline activities, capturing events, statuses, and timestamps for tracking execution.

---

## 🛠 Technologies Used

- **Azure Data Factory (ADF)**
- **Azure Databricks**
- **Azure Blob Storage**
- **Azure Data Lake Storage (ADLS)**
- **Self-hosted Integration Runtime (SHIR)**
- **Azure Key Vault**
- **Azure Logic Apps**
- **Azure Active Directory (AAD)**
- **Unity Catalog**
- **Google Cloud Storage (GCP)**

---

## 📈 Summary

This project showcases the ability to design and implement **large-scale, secure, and automated data pipelines** that handle both dimensional and fact tables. By integrating Azure Services, the solution ensures strong data governance, security, and seamless cross-platform connectivity. 

The **watermark_column** is pivotal in managing incremental data loads, optimizing data transfer efficiency, and preventing duplication.

Feel free to reach out if you have any questions or would like to learn more about this project!

--- 
