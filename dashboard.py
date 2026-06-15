# dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

st.title("Sales Analytics Dashboard")

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.2f}")
col3.metric("Total Orders", df["Order_ID"].nunique())

# Filter by Region
st.sidebar.header("Filters")
selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["Region"].unique())
)

if selected_region != "All":
    df = df[df["Region"] == selected_region]

# Revenue by Product
st.subheader("Revenue by Product")

product_revenue = df.groupby("Product")["Revenue"].sum().sort_values()

fig, ax = plt.subplots(figsize=(10, 6))
product_revenue.plot(kind="barh", ax=ax)

st.pyplot(fig)

# Data table
st.subheader("Sales Data")
st.dataframe(df)