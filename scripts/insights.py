import streamlit as st

def generate_insights(df, customer_summary):
    st.header("📊 Automated Business Insights")

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = len(df)

    top_segment = customer_summary["Segment"].value_counts().idxmax()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Revenue", f"{df['Revenue'].sum():,.2f}")

    with col2:
        st.metric("Total Profit", f"{df['Profit'].sum():,.2f}")

    with col3:
        st.metric("Total Orders", len(df))

    st.subheader("Key Insight")
    st.write(f"Dominant Customer Segment: **{top_segment}**")

    st.markdown("""
    ### Recommendations
    - Focus marketing on High Value customers  
    - Improve retention for repeat customers  
    - Optimize low-performing segments  
    """)

    