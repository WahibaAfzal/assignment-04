import streamlit as st
import pandas as pd
import datetime
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Expense Tracker", page_icon="💰")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# App Title
st.title("💸 Personal Expense Tracker")

# Sidebar - Add New Expense
st.sidebar.header("➕ Add New Expense")
date = st.sidebar.date_input("📅 Date", datetime.date.today())
category = st.sidebar.selectbox("📂 Category", ["Food", "Shopping", "Bills", "Travel", "Entertainment", "Other"])
amount = st.sidebar.number_input("💲 Amount (pkr)", min_value=0.01, step=0.01)
description = st.sidebar.text_input("📝 Description")

# Add Expense Button
if st.sidebar.button("✅ Add Expense"):
    if description:
        st.session_state.expenses.append({"Date": date, "Category": category, "Amount": amount, "Description": description})
        st.sidebar.success("Expense added successfully!")
    else:
        st.sidebar.error("⚠️ Please add a description.")

# Display Expense Data
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.subheader("📋 Expense List")
    st.dataframe(df, use_container_width=True)

    # Summary Metrics
    st.subheader("📊 Summary")
    st.metric("💰 Total Expenses", f"${df['Amount'].sum():.2f}")

    # Expense Pie Chart
    fig = px.pie(df, values="Amount", names="Category", title="Category-wise Expenses", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)

    # Download Button
    st.download_button("📥 Download CSV", df.to_csv(index=False), "expenses.csv", "text/csv")
else:
    st.info("ℹ️ No expenses added yet. Add one from the sidebar!")

