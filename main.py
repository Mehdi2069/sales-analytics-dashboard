import pandas as pd
from scripts.audit import audit_data
from scripts.clean import clean_sales_data
from scripts.analysis import analyze_sales
from scripts.visualize import visualize_sales
from scripts.report import generate_report
from scripts.customer_segmentation import segment_customers
from scripts.repeat_customers import analyze_repeat_customers
from scripts.customer_lifetime_value import calculate_clv
from scripts.customer_visualize import (visualize_customer_segments, visualize_top_customers, visualize_clv)
from scripts.insights import generate_insights

# Load data
df = pd.read_csv("data/sales_data.csv")
print("DATE DEBUG")
print(df["Date"].dtype)
print(df["Date"].head())

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

# Segment customers
customer_summary = segment_customers(df)

# Visualize customer segments
visualize_customer_segments(customer_summary)
# Visualize top customers
visualize_top_customers(customer_summary)

# Analyze repeat customers
repeat_customers = analyze_repeat_customers(df)

# Calculate customer lifetime value
customer_summary = calculate_clv(customer_summary)

# Visualize top customers by CLV
visualize_clv(customer_summary)

# Generate business insights
generate_insights(df, customer_summary)

# print("Reached end of main.py")
