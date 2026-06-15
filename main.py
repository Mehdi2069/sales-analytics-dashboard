import pandas as pd
from scripts.audit import audit_data
from scripts.clean import clean_sales_data
from scripts.analysis import analyze_sales
from scripts.visualize import visualize_sales
from scripts.report import generate_report


# Load data
df = pd.read_csv("data/sales_data.csv")

# Audit raw data
audit_data(df)

# Clean data
df = clean_sales_data(df)

# Analyze cleaned data
analyze_sales(df)

# Audit cleaned data
print("\n--- CLEANED DATA SAMPLE ---")
print(df.head())
print(df.info())

# Visualize sales data
visualize_sales(df)

# Generate sales report
generate_report(df)