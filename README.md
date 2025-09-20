# E-commerce Order ETL & CRM Insights

A complete **ETL pipeline + analytics project** built from raw e-commerce order data.  
This project simulates how data engineers and analysts work together to process raw data, build a clean star schema, and generate CRM-driven insights for business decision-making.  

---

## 🚀 Features
- **ETL Pipeline (Python + Pandas)**: Extract raw CSV orders, clean & standardize schema, load into database.  
- **Data Warehouse Modeling**: Designed fact & dimension tables (Star Schema).  
- **SQL Analytics**: Built queries for revenue, customer segmentation, and retention metrics.  
- **CRM Insights (RFM Model)**: Identified high-value customers and churn risk.  
- **Dashboarding**: Interactive insights in **Tableau / Power BI**.  

---

## 📂 Project Structure

```plaintext
ecommerce-etl-crm-insights/
├── data/                     # Raw & processed data
│   ├── raw_data/             # Input CSVs
│   └── processed/            # Cleaned data
├── src/                      # ETL scripts
│   ├── extract.py            # Extract raw CSVs
│   ├── transform.py          # Clean & standardize
│   ├── load.py               # Load into SQL DB
│   └── pipeline.py           # Orchestrate ETL
├── sql/                      # SQL schema & queries
│   ├── schema.sql            # Fact & dimension tables (star schema)
│   └── queries.sql           # Business queries
├── notebooks/                # Analysis & CRM
│   └── crm_analysis.ipynb    # RFM & user insights
├── dashboard/                # Dashboards
│   ├── tableau.twbx          # Tableau dashboard
│   └── powerbi.pbix          # Power BI dashboard
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation

---
⚙️ Setup Instructions
1. Create Environment
```bash
conda create -n ecommerce-etl-env python=3.10 -y
conda activate ecommerce-etl-env
pip install -r requirements.txt
2. Run ETL Pipeline
python src/pipeline.py

---
📊 Example Queries

Revenue by month & category

Repeat purchase rate

RFM segmentation (Recency, Frequency, Monetary)

High-return SKUs

🛠️ Tech Stack

Python (pandas, numpy, sqlalchemy, scikit-learn)

SQL (schema design, queries)

Visualization: Tableau, Power BI, matplotlib, seaborn, plotly

Jupyter for CRM analysis

🌟 Skills Highlighted

End-to-end ETL pipeline design

SQL data modeling (Star Schema, Fact & Dimension tables)

CRM customer segmentation (RFM)

Dashboard building & storytelling with data


