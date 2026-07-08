import matplotlib.pyplot as plt


def visualize_customer_segments(customer_summary):
    print("Customer visualization started...")
    segment_counts = customer_summary["Segment"].value_counts()

    fig, ax = plt.subplots(figsize=(8, 6))
    segment_counts.plot(kind="bar", ax=ax)

    ax.set_title("Customer Segments")
    ax.set_xlabel("Segment")
    ax.set_ylabel("Number of Customers")

    fig.tight_layout()
    fig.savefig("output/charts/customer_segments.png")
    return fig


def visualize_top_customers(customer_summary):
    top_customers = customer_summary.sort_values(
        by="Total_Revenue",
        ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    top_customers["Total_Revenue"].plot(kind="bar", ax=ax)

    ax.set_title("Top 10 Customers by Revenue")
    ax.set_xlabel("Customer ID")
    ax.set_ylabel("Revenue")

    fig.tight_layout()
    fig.savefig("output/charts/top_customers.png")
    return fig


def visualize_clv(customer_summary):
    top_clv = customer_summary.sort_values(
        by="CLV",
        ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    top_clv["CLV"].plot(kind="bar", ax=ax)

    ax.set_title("Top 10 Customers by CLV")
    ax.set_xlabel("Customer ID")
    ax.set_ylabel("Customer Lifetime Value")

    fig.tight_layout()
    fig.savefig("output/charts/top_clv.png")
    return fig