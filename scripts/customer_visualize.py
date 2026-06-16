import matplotlib.pyplot as plt


def visualize_customer_segments(customer_summary):
    print("Customer visualization started...")
    segment_counts = customer_summary["Segment"].value_counts()

    plt.figure(figsize=(8, 6))
    segment_counts.plot(kind="bar")

    plt.title("Customer Segments")
    plt.xlabel("Segment")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.savefig("output/charts/customer_segments.png")
    plt.show()
def visualize_top_customers(customer_summary):
    top_customers = customer_summary.sort_values(
        by="Total_Revenue",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))
    top_customers["Total_Revenue"].plot(kind="bar")

    plt.title("Top 10 Customers by Revenue")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("output/charts/top_customers.png")
    plt.show()
def visualize_clv(customer_summary):
    top_clv = customer_summary.sort_values(
        by="CLV",
        ascending=False
    ).head(10)

    plt.figure(figsize=(12, 6))
    top_clv["CLV"].plot(kind="bar")

    plt.title("Top 10 Customers by CLV")
    plt.xlabel("Customer ID")
    plt.ylabel("Customer Lifetime Value")

    plt.tight_layout()
    plt.savefig("output/charts/top_clv.png")
    plt.show()