def analyze_sales(df):
    print("\n--- SALES KPIs ---")

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_customers = df["Customer_ID"].nunique()
    average_order_value = df["Revenue"].mean()

    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Total Orders: {total_orders}")
    print(f"Total Customers: {total_customers}")
    print(f"Average Order Value: ${average_order_value:,.2f}")

    print("\n--- TOP PRODUCTS ---")
    top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
    print(top_products.head())

    print("\n--- REVENUE BY REGION ---")
    revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
    print(revenue_by_region)

    print("\n--- SALES CHANNEL PERFORMANCE ---")
    channel_performance = df.groupby("Sales_Channel")["Revenue"].sum()
    print(channel_performance)
print("Analysis module loaded")