def analyze_repeat_customers(df):
    print("\n--- REPEAT CUSTOMER ANALYSIS ---")

    customer_orders = df.groupby("Customer_ID")["Order_ID"].count()

    repeat_customers = customer_orders[customer_orders > 1]

    print(f"Total repeat customers: {len(repeat_customers)}")
    print(repeat_customers.head(10))

    return repeat_customers