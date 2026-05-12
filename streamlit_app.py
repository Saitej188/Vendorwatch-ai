import sys
import os
import streamlit as st
import pandas as pd

# ==============================
# SAFE ROOT PATH (HF FIX)
# ==============================
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

# ==============================
# IMPORTS (SAFE WRAPPED)
# ==============================
try:
    from database.db import engine, init_db
    from ml.insights import generate_insights
    from ml.report import generate_report
except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()

# ==============================
# UI CONFIG
# ==============================
st.set_page_config(page_title="VendorWatch AI", layout="wide")
st.title("📊 VendorWatch AI – Job Intelligence Dashboard")

# ==============================
# INIT DB (SAFE)
# ==============================
try:
    init_db()
except Exception as e:
    st.warning(f"DB init warning: {e}")

# ==============================
# LOAD DATA (SAFE)
# ==============================
try:
    df = pd.read_sql("jobs", engine)
except Exception as e:
    st.error(f"Database error: {e}")
    st.info("Run pipeline first or ensure DB exists.")
    st.stop()

# ==============================
# EMPTY DATA HANDLING
# ==============================
if df is None or df.empty:
    st.warning("No data found in database.")
    st.stop()

# ==============================
# CLEAN DATA
# ==============================
df["company"] = df["company"].fillna("Unknown")
df["title"] = df["title"].fillna("Unknown")

# ==============================
# KPIs
# ==============================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Jobs", len(df))
col2.metric("Remote Jobs", int(df["is_remote"].sum()))
col3.metric("Senior Roles", int(df["is_senior"].sum()))

st.divider()

# ==============================
# FILTERS
# ==============================
st.subheader("🔎 Filters")

company_filter = st.selectbox("Company", ["All"] + sorted(df["company"].unique()))

remote_filter = st.radio("Remote Only?", ["All", "Yes"])

filtered_df = df.copy()

if company_filter != "All":
    filtered_df = filtered_df[filtered_df["company"] == company_filter]

if remote_filter == "Yes":
    filtered_df = filtered_df[filtered_df["is_remote"] == True]

# ==============================
# TABLE
# ==============================
st.subheader("📄 Job Listings")
st.dataframe(filtered_df, use_container_width=True)

# ==============================
# CHARTS
# ==============================
st.subheader("📊 Top Companies")
st.bar_chart(df["company"].value_counts().head(10))

st.subheader("🌍 Remote vs Non-Remote")
st.bar_chart(df["is_remote"].value_counts())

# ==============================
# AI INSIGHTS
# ==============================
st.subheader("🧠 AI Insights")

try:
    insights = generate_insights(df)
    st.json(insights)
except Exception as e:
    st.warning(f"Insights error: {e}")

# ==============================
# SUMMARY
# ==============================
st.subheader("📊 Job Summary")

summary = {
    "total_jobs": len(df),
    "remote_jobs": int(df["is_remote"].sum()),
    "top_company": df["company"].value_counts().idxmax(),
    "senior_jobs": int(df["is_senior"].sum())
}

st.json(summary)

# ==============================
# REPORT
# ==============================
st.subheader("📄 Market Intelligence Report")

try:
    report = generate_report(df)
    st.write(report.get("summary", "No summary available"))
except Exception as e:
    st.warning(f"Report error: {e}")