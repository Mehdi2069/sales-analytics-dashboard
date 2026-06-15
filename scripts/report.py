def generate_report(df):
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_customers = df["Customer_ID"].nunique()
    average_order_value = df["Revenue"].mean()

    top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

    report_text = f"""
SALES ANALYTICS REPORT
=======================

Total Revenue: ${total_revenue:,.2f}
Total Profit: ${total_profit:,.2f}
Total Orders: {total_orders}
Total Customers: {total_customers}
Average Order Value: ${average_order_value:,.2f}

TOP PRODUCTS
------------
{top_products.to_string()}

REVENUE BY REGION
-----------------
{revenue_by_region.to_string()}
"""

    with open("output/reports/sales_report.txt", "w") as file:
        file.write(report_text)

    print("Report generated: output/reports/sales_report.txt")