def segment_customers(df):
    print("\n--- CUSTOMER SEGMENTATION ---")

    customer_summary = df.groupby("Customer_ID").agg({
        "Revenue": "sum",
        "Profit": "sum",
        "Order_ID": "count"
    })

    customer_summary.columns = [
        "Total_Revenue",
        "Total_Profit",
        "Total_Orders"
    ]

    # Default segment
    customer_summary["Segment"] = "Low Value"

    # Medium-value customers
    customer_summary.loc[
        customer_summary["Total_Revenue"] > 3000,
        "Segment"
    ] = "Medium Value"

    # High-value customers
    customer_summary.loc[
        customer_summary["Total_Revenue"] > 7000,
        "Segment"
    ] = "High Value"

    print(customer_summary.head(10))
    
    top_customers = customer_summary.sort_values(by="Total_Revenue", ascending=False).head(10)
    print("\n--- TOP 10 CUSTOMERS ---")
    print(top_customers)

    return customer_summary