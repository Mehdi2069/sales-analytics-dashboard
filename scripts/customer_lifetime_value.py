def calculate_clv(customer_summary):
    print("\n--- CUSTOMER LIFETIME VALUE ---")

    customer_summary["CLV"] = (
        customer_summary["Total_Revenue"] /
        customer_summary["Total_Orders"]
    )

    print(customer_summary[["CLV"]].head(10))

    return customer_summary