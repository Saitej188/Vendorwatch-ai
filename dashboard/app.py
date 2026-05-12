import sys
import os
import streamlit as st
import pandas as pd

# ==============================
# FIX: Make project root visible
# ==============================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from database.db import engine, init_db
from ml.insights import generate_insights
from ml.report import generate_report

# ==============================
# UI CONFIG
# ==============================
st.set_page_config(page_title="VendorWatch AI", layout="wide")

st.title("📊 VendorWatch AI – Job Intelligence Dashboard")

# Ensure the SQLite table exists before querying it.
init_db()

# ==============================
# LOAD DATA
# ==============================
try:
    df = pd.read_sql("jobs", engine)
except Exception as e:
    st.error("Unable to load job data: {}".format(e))
    st.info("Run `python pipeline/run_pipeline.py` to populate the database.")
    st.stop()

if df.empty:
    st.info("No jobs found in the database. Initializing data now...")
    try:
        from pipeline.run_pipeline import run_pipeline
        run_pipeline()
        df = pd.read_sql("jobs", engine)
    except Exception as e:
        st.error(f"Failed to initialize data: {e}")
        st.stop()

    if df.empty:
        st.warning("Still no job data available after initialization.")
        st.stop()

# Safety cleanup
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

company_filter = st.selectbox(
    "Company",
    ["All"] + sorted(df["company"].unique().tolist())
)

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
# ANALYTICS
# ==============================
st.subheader("📊 Top Companies")
st.bar_chart(df["company"].value_counts().head(10))

st.subheader("🌍 Remote vs Non-Remote")
st.bar_chart(df["is_remote"].value_counts())

# ==============================
# 🧠 AI INSIGHTS
# ==============================
st.subheader("🧠 AI Insights")
insights = generate_insights(df)
st.json(insights)

# ==============================
# 📊 JOB SUMMARY
# ==============================
st.subheader("📊 Job Summary")
summary = {
    "total_jobs": len(df),
    "remote_jobs": int(df["is_remote"].sum()),
    "top_company": df["company"].value_counts().idxmax() if not df["company"].empty else "N/A",
    "senior_jobs": int(df["is_senior"].sum())
}
st.json(summary)

# ==============================
# 📄 MARKET REPORT (AI LAYER)
# ==============================
st.subheader("📄 Market Intelligence Report")
report = generate_report(df)
st.write(report["summary"])
