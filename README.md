E-commerce Order ETL & CRM Insights

This project demonstrates an end-to-end ETL pipeline and customer insights workflow built on real-world e-commerce order data. Multiple raw CSV exports (orders across different dates) were ingested, cleaned, and consolidated into a structured database for downstream analytics and CRM-style insights.

🔑 Key Features

ETL Pipeline: Automated ingestion of multiple CSV exports, data cleaning (deduplication, missing value handling, currency/date normalization), and structured loading into a relational schema (fact tables & dimension tables).

Data Quality & Logging: Built-in checks for duplicates, null values, and abnormal orders, with logs documenting pipeline execution.

CRM Analysis: Implemented RFM (Recency, Frequency, Monetary) segmentation, churn rate calculation, repeat purchase analysis, and customer lifetime value trends.

Business Insights: Identified top-performing products, high-value customers, and refund/return patterns to inform product and marketing strategies.

Dashboarding: Interactive dashboards (Tableau/Power BI) visualize GMV growth, order trends, customer cohorts, and retention metrics.

🛠️ Tech Stack

Languages & Libraries: Python (Pandas, NumPy, logging), SQL (Joins, CTEs, Window Functions)

Data Infrastructure: SQLite / PostgreSQL, CSV ingestion

Visualization: Tableau / Power BI

Workflow: Modular Python scripts for ETL; optional scheduling with Airflow/Prefect
