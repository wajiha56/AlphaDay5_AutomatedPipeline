"""
Alpha Day 7: End-to-End Automated Data Pipeline + PDF Reporting
Author: Wajiha

Description:
This script builds a complete automated Business Intelligence pipeline that:

1. Reads raw CSV data
2. Cleans missing values and outliers
3. Stores the cleaned data in an SQLite database
4. Queries insights using SQL
5. Generates an automated BI chart
6. Creates a professional PDF business report automatically
"""

# ==========================
# Import Required Libraries
# ==========================
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF


# ==========================
# Pipeline Start Message
# ==========================
print("\n--- Starting Alpha Automated Pipeline ---\n")


# =====================================================
# STEP 1: DATA INGESTION & CLEANING (The Data Surgeon)
# =====================================================
print("1. Ingesting and Cleaning Data...")

# Load the raw CSV dataset
df = pd.read_csv("broken_sales_data.csv")

# ------------------------------
# Handle Missing Sales Values
# ------------------------------
electronics_median = df[df["Category"] == "Electronics"]["Sales"].median()
df["Sales"] = df["Sales"].fillna(electronics_median)

# ------------------------------
# Handle Missing Quantity Values
# ------------------------------
df["Quantity"] = df["Quantity"].fillna(1)

# ------------------------------
# Fix Quantity Outliers
# ------------------------------
office_mean_quantity = df[df["Category"] == "Office"]["Quantity"].mean()
df.loc[df["Quantity"] > 100, "Quantity"] = office_mean_quantity


# ==========================================
# STEP 2: DATABASE STORAGE (The Architect)
# ==========================================
print("2. Pushing Data to SQLite Database...")

# Create SQLite database connection
conn = sqlite3.connect("Alpha_Data_Warehouse.db")

# Store cleaned dataframe into SQL table
df.to_sql(
    "Cleaned_Sales",
    conn,
    if_exists="replace",
    index=False
)


# ===============================================
# STEP 3: QUERY & VISUALIZATION (The Translator)
# ===============================================
print("3. Querying Insights and Generating Report...")

query = """
SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM Cleaned_Sales
GROUP BY Category
"""

profit_df = pd.read_sql_query(query, conn)

conn.close()


# ===============================================
# STEP 4: CREATE EXECUTIVE BUSINESS CHART
# ===============================================

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))

sns.barplot(
    data=profit_df,
    x="Category",
    y="Total_Profit",
    hue="Category",
    palette="magma",
    legend=False
)

plt.title(
    "Automated Report: Total Net Profit by Category",
    fontweight="bold"
)

plt.ylabel("Net Profit (PKR)")

plt.axhline(0, color="black", linewidth=1)


# ===============================================
# STEP 5: SAVE CHART IMAGE
# ===============================================

plt.savefig(
    "Automated_Profit_Report.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Chart saved successfully.")


# ===============================================
# STEP 6: GENERATE PROFESSIONAL PDF REPORT
# ===============================================

def generate_pdf_report(profit_df):

    total_profit = profit_df["Total_Profit"].sum()

    pdf = FPDF()
    pdf.add_page()

    # Report Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(
        200,
        10,
        "Automated Sales Intelligence Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # Key Metric
    pdf.set_font("Arial", size=12)
    pdf.cell(
        200,
        10,
        f"Total Net Profit Across Categories: PKR {round(total_profit,2)}",
        ln=True
    )

    pdf.ln(10)

    # Insert Chart
    pdf.image(
        "Automated_Profit_Report.png",
        x=10,
        y=50,
        w=180
    )

    # Save PDF
    pdf.output("Weekly_Business_Intelligence_Report.pdf")

    print("✔ Professional PDF Report Generated!")


# Call the PDF generation function
generate_pdf_report(profit_df)


# ===============================================
# PIPELINE COMPLETE MESSAGE
# ===============================================

print("\n--- Pipeline Complete! ---")
print("Check your folder for the following outputs:")
print("1. Alpha_Data_Warehouse.db")
print("2. Automated_Profit_Report.png")
print("3. Weekly_Business_Intelligence_Report.pdf\n")