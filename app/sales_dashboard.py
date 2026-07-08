import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

def main():
    # -------------------------
    # CONFIG
    # -------------------------
    st.set_page_config(page_title="Sales Analytics Dashboard", layout="wide")
    st.title("📊 Sales Analytics Dashboard")


    # -------------------------
    # LOAD DATA
    # -------------------------
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATA_PATH = BASE_DIR / "data" / "sales_data.csv"

    @st.cache_data
    def load_data():
        df = pd.read_csv(DATA_PATH)
        df = clean_sales_data(df)
        return df

    df = load_data()        


# -------------------------
# NAVIGATION + FILTERS
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

# Date range filter
    min_date = df["Date"].min()
    max_date = df["Date"].max()

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date)
    )

# Apply filters
    start_date, end_date = date_range

    df = df[
        (df["Region"].isin(region_filter)) &
        (df["Product"].isin(product_filter)) &
        (df["Date"] >= pd.to_datetime(start_date)) &
        (df["Date"] <= pd.to_datetime(end_date))
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

        col1, col2, col3, col4, col5 = st.columns(5)

        total_revenue = df["Revenue"].sum()
        total_profit = df["Profit"].sum()
        profit_margin = (total_profit / total_revenue) * 100
        average_order_value = total_revenue / len(df)


        with col1:
            st.metric("Total Revenue", f"{total_revenue:,.2f}")

        with col2:
            st.metric("Total Profit", f"{total_profit:,.2f}")

        with col3:
            st.metric("Total Orders", len(df))

        with col4:
            st.metric("Profit Margin (%)", f"{profit_margin:.2f}%")

        with col5:
            st.metric("Average Order Value", f"{average_order_value:,.2f}")

    # Download filtered data
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="filtered_sales_data.csv",
            mime="text/csv"
        )

        # -------------------------
        # Top Customers chart
        # -------------------------
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

        st.plotly_chart(
            fig,
            width="stretch",
            key="top_customers_chart"
        )


        # -------------------------
        # Revenue Over Time chart
        # -------------------------
        revenue_over_time = (
            df.groupby("Date")["Revenue"]
            .sum()
            .reset_index()
        )

        fig_time = px.line(
            revenue_over_time,
            x="Date",
            y="Revenue",
            title="Revenue Over Time"
        )

        st.plotly_chart(
            fig_time,
            width="stretch",
            key="revenue_time_chart"
        )
        # -------------------------
        # Profit Over Time chart
        # -------------------------
        profit_over_time = (
            df.groupby("Date")["Profit"]
            .sum()
            .reset_index()
        )

        fig_profit = px.line(
            profit_over_time,
            x="Date",
            y="Profit",
            title="Profit Over Time"
        )

        st.plotly_chart(
            fig_profit,
            width="stretch",
            key="profit_time_chart"
        )

        # -------------------------
        # Revenue vs Profit (Combined)
        # -------------------------
        combined_metrics = (
            df.groupby("Date")[["Revenue", "Profit"]]
            .sum()
            .reset_index()
        )

        fig_combined = px.line(
            combined_metrics,
            x="Date",
            y=["Revenue", "Profit"],
            title="Revenue vs Profit Over Time"
        )

        st.plotly_chart(
            fig_combined,
            width="stretch",
            key="combined_revenue_profit_chart"
        )

        # -------------------------
        # Best Selling Products
        # -------------------------
        top_products = (
            df.groupby("Product")["Revenue"]
            .sum()
            .nlargest(10)
            .reset_index()
        )

        fig_products = px.bar(
            top_products,
            x="Product",
            y="Revenue",
            title="Top 10 Products by Revenue"
        )

        st.plotly_chart(
            fig_products,
            width="stretch",
            key="top_products_chart"
        )
        # -------------------------
        # Top Regions by Revenue
        # -------------------------
        region_sales = (
            df.groupby("Region")["Revenue"]
            .sum()
            .reset_index()
        )

        fig_regions = px.bar(
            region_sales,
            x="Region",
            y="Revenue",
            title="Revenue by Region"
        )

        st.plotly_chart(
            fig_regions,
            width="stretch",
            key="region_revenue_chart"
        )
        # Download filtered data
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="filtered_sales_data.csv",
            mime="text/csv",
            key="download_filtered_csv"
        )
        # Top customers chart
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


    # -------------------------------
    # TOP CUSTOMERS (Plotly - interactive)
    # ------------------------
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

    
if __name__ == "__main__":
    main()
