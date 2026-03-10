# Automated Sales Intelligence Pipeline

**Author:** Wajiha Arshad  
**Role:** Junior Data Analyst | Business Intelligence Specialist  

---

## 📌 Project Overview

This project demonstrates a **complete end-to-end automated Business Intelligence (BI) pipeline** using Python and SQLite. The pipeline takes **raw, messy sales data**, cleans it, stores it in a **SQL data warehouse**, generates business insights, visualizes profit trends, and automatically produces a **client-ready PDF report**.

**Key Features:**
- Fully automated data pipeline from raw CSV to professional PDF
- Intelligent handling of missing values and outliers
- SQL database storage and queries for business insights
- Automated visualization using Seaborn
- PDF executive reporting for client delivery

---

## 🗂️ Folder Structure

```text
AlphaDay5_EndToEnd_Pipeline
│
├── broken_sales_data.csv            # Raw sales dataset
├── Alpha_Data_Warehouse.db          # Cleaned data stored in SQLite
├── Automated_Profit_Report.png      # Automated profit bar chart
├── Weekly_Business_Intelligence_Report.pdf  # Client-ready PDF report
├── alpha_day5_master_pipeline.py    # End-to-end Python pipeline
├── README.md                        # Project documentation

```
##⚙️ Technologies & Libraries
```
Python: Data processing & automation
Pandas: Data cleaning & manipulation
SQLite: Data warehouse & query execution
Seaborn / Matplotlib: Data visualization
FPDF: Automated PDF report generation
```
##📝 Pipeline Workflow
```
Raw CSV Data
       ↓
Data Cleaning (Python)
       ↓
SQLite Data Warehouse
       ↓
SQL Query for Insights
       ↓
Seaborn Visualization (Chart)
       ↓
Automated PDF Executive Report
```
##Workflow Highlights
```
- Missing Sales & Quantity handled intelligently
- Quantity outliers corrected
- Total profit calculated per category
- Bar chart generated automatically
- PDF includes:
  - Report Title
  - Total Profit Metric
  - Chart visualization
```
##🚀 How to Run
```
# 1. Clone the repository
git clone <your-github-repo-link>

# 2. Install required libraries
pip install pandas matplotlib seaborn fpdf sqlite3

# 3. Run the pipeline
python alpha_day5_master_pipeline.py


