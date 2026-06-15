import matplotlib.pyplot as plt

def visualize_sales(df):
    # Revenue by product
    product_revenue = df.groupby("Product")["Revenue"].sum().sort_values()

    plt.figure(figsize=(10, 6))
    product_revenue.plot(kind="barh")
    plt.title("Revenue by Product")
    plt.xlabel("Revenue")
    plt.ylabel("Product")

    plt.tight_layout()
    plt.savefig("output/charts/revenue_by_product.png")
    plt.show()

    # Revenue by region
    region_revenue = df.groupby("Region")["Revenue"].sum()

    plt.figure(figsize=(8, 6))
    region_revenue.plot(kind="bar")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.savefig("output/charts/revenue_by_region.png")
    plt.show()