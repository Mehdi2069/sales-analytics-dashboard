import streamlit as st

def generate_insights(df, customer_summary):
    st.header("📊 Automated Business Insights")

    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_orders = len(df)

    top_segment = customer_summary["Segment"].value_counts().idxmax()

    st.metric("Total Revenue", f"{total_revenue:,.2f}")
    st.metric("Total Profit", f"{total_profit:,.2f}")
    st.metric("Total Orders", total_orders)

    st.subheader("Key Insight")
    st.write(f"Dominant Customer Segment: **{top_segment}**")

    st.markdown("""
    ### Recommendations
    - Focus marketing on High Value customers  
    - Improve retention for repeat customers  
    - Optimize low-performing segments  
    """)
    
    