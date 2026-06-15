import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

products = {
    "Laptop": ("Electronics", 900, 650),
    "Phone": ("Electronics", 700, 500),
    "Tablet": ("Electronics", 450, 300),
    "Headphones": ("Accessories", 120, 60),
    "Smartwatch": ("Wearables", 250, 140),
    "Monitor": ("Electronics", 300, 180),
    "Keyboard": ("Accessories", 80, 35),
    "Mouse": ("Accessories", 50, 20)
}

regions = ["Europe", "North America", "Asia", "South America"]
channels = ["Online", "Store"]
payments = ["Credit Card", "Cash", "Bank Transfer"]

data = []

for i in range(5000):
    product = random.choice(list(products.keys()))
    category, price, cost = products[product]

    quantity = np.random.randint(1, 6)
    discount = round(np.random.uniform(0, 0.20), 2)

    revenue = quantity * price * (1 - discount)
    total_cost = quantity * cost
    profit = revenue - total_cost

    data.append([
        f"ORD-{10000+i}",
        fake.date_between(start_date="-12M", end_date="today"),
        product,
        category,
        quantity,
        price,
        f"CUST-{np.random.randint(1000, 2000)}",
        random.choice(regions),
        random.choice(channels),
        random.choice(payments),
        discount,
        total_cost,
        revenue,
        profit
    ])

columns = [
    "Order_ID", "Date", "Product", "Category", "Quantity",
    "Unit_Price", "Customer_ID", "Region", "Sales_Channel",
    "Payment_Method", "Discount", "Cost", "Revenue", "Profit"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/sales_data.csv", index=False)

df.head()
print(df.head(10))
df["Date"] = pd.to_datetime(df["Date"])
df.info()
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
