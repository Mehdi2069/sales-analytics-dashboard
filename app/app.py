import pandas as pd
import streamlit as st
import plotly.express as px

from scripts.clean import clean_sales_data
from scripts.customer_segmentation import segment_customers
from scripts.customer_visualize import (
    visualize_customer_segments,
    visualize_clv
)
from scripts.repeat_customers import analyze_repeat_customers
from scripts.customer_lifetime_value import calculate_clv
from scripts.insights import generate_insights


# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")
st.title("📊 Sales Analytics Dashboard")


# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv("data/sales_data.csv")

# Clean data
df = clean_sales_data(df)



# -------------------------
# NAVIGATION
# -------------------------
st.sidebar.title("🔎 Filters")

page = st.sidebar.selectbox(
    "Navigate",
    ["Overview", "Customers", "Insights"]
)

region_filter = st.sidebar.multiselect(
    "Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

product_filter = st.sidebar.multiselect(
    "Product",
    options=df["Product"].unique(),
    default=df["Product"].unique()
)

df = df[
    (df["Region"].isin(region_filter)) &
    (df["Product"].isin(product_filter))
]

# -------------------------
# CUSTOMER PROCESSING
# -------------------------
customer_summary = segment_customers(df)
customer_summary = calculate_clv(customer_summary)


# -------------------------
# OVERVIEW PAGE
# -------------------------
if page == "Overview":
    st.header("Overview Metrics")

    st.metric("Total Revenue", f"{df['Revenue'].sum():,.2f}")
    st.metric("Total Profit", f"{df['Profit'].sum():,.2f}")
    st.metric("Total Orders", len(df))

    # TOP CUSTOMERS (Plotly - interactive)
    top_customers = (
        customer_summary.groupby("Customer_ID")["Total_Revenue"]
        .sum()
        .nlargest(10)
        .reset_index()
    )

    fig = px.bar(
        top_customers,
        x="Customer_ID",
        y="Total_Revenue",
        title="Top 10 Customers by Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# CUSTOMERS PAGE
# -------------------------
elif page == "Customers":
    st.header("Customer Analytics")

    st.dataframe(customer_summary)

    st.subheader("Customer Segments")
    st.pyplot(visualize_customer_segments(customer_summary))

    st.subheader("Customer Lifetime Value")
    st.pyplot(visualize_clv(customer_summary))

    st.subheader("Repeat Customers")
    repeat_customers = analyze_repeat_customers(df)
    st.dataframe(repeat_customers)


# -------------------------
# INSIGHTS PAGE
# -------------------------
elif page == "Insights":
    st.header("📊 Business Insights")

    st.metric("Total Revenue", f"{df['Revenue'].sum():,.2f}")
    st.metric("Total Profit", f"{df['Profit'].sum():,.2f}")
    st.metric("Total Orders", len(df))

    st.write(
        "Dominant Segment:",
        customer_summary["Segment"].value_counts().idxmax()
    )

    st.subheader("Recommendations")
    st.markdown("""
    - Focus on High Value customers  
    - Improve retention strategies  
    - Reduce low-performing segments  
    """)

    # Optional advanced insights function
    generate_insights(df, customer_summary)
