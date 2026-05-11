import sys
import os
import streamlit as st
import pandas as pd
import requests

# ==============================
# FIX: Make project root visible
# ==============================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from database.db import engine

# ==============================
# UI CONFIG
# ==============================
st.set_page_config(page_title="VendorWatch AI", layout="wide")

st.title("📊 VendorWatch AI – Job Intelligence Dashboard")

# ==============================
# LOAD DATA
# ==============================
df = pd.read_sql("jobs", engine)

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
# 🧠 AI INSIGHTS (FASTAPI)
# ==============================
st.subheader("🧠 AI Insights")

try:
    insights = requests.get("http://127.0.0.1:8000/insights").json()
    st.json(insights)
except:
    st.warning("AI Insights API not running")

# ==============================
# 📊 JOB SUMMARY (FASTAPI)
# ==============================
st.subheader("📊 Job Summary")

try:
    summary = requests.get("http://127.0.0.1:8000/jobs/summary").json()
    st.json(summary)
except:
    st.warning("Job Summary API not running")
# ==============================
# 📄 MARKET REPORT (AI LAYER)
# ==============================

st.subheader("📄 Market Intelligence Report")

try:
    report = requests.get("http://127.0.0.1:8000/report").json()
    st.write(report["summary"])
except:
    st.warning("Report API not running")