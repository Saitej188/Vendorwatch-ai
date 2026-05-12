from fastapi import FastAPI, Query
import pandas as pd
from database.db import engine, init_db

from ml.insights import generate_insights
from ml.report import generate_report

app = FastAPI(title="VendorWatch AI")

# Ensure the database schema exists before serving API requests.
init_db()

# ------------------------
# HEALTH CHECK
# ------------------------
@app.get("/")
def home():
    return {"status": "running"}

# ------------------------
# GET ALL JOBS
# ------------------------
@app.get("/jobs")
def get_jobs():
    df = pd.read_sql("jobs", engine)
    df = df.sort_values(by="company")
    return df.to_dict(orient="records")

# ------------------------
# SEARCH JOBS
# ------------------------
@app.get("/jobs/search")
def search(q: str = Query(...)):
    df = pd.read_sql("jobs", engine)
    result = df[df["title"].str.contains(q, case=False, na=False)]
    return result.to_dict(orient="records")

# ------------------------
# SMART SEARCH (TOP 1% FEATURE)
# ------------------------
@app.get("/jobs/smart-search")
def smart_search(q: str):
    df = pd.read_sql("jobs", engine)

    df["score"] = (
        df["title"].str.contains(q, case=False, na=False).astype(int) * 2 +
        df["company"].str.contains(q, case=False, na=False).astype(int)
    )

    result = df[df["score"] > 0].sort_values("score", ascending=False)

    return result.drop(columns=["score"]).to_dict(orient="records")

# ------------------------
# FILTER: REMOTE JOBS
# ------------------------
@app.get("/jobs/remote")
def remote_jobs():
    df = pd.read_sql("jobs", engine)
    return df[df["is_remote"] == True].to_dict(orient="records")

# ------------------------
# TOP COMPANIES
# ------------------------
@app.get("/jobs/top-companies")
def top_companies():
    df = pd.read_sql("jobs", engine)
    return df["company"].value_counts().head(10).to_dict()

# ------------------------
# JOB SUMMARY (INTERVIEW GOLD)
# ------------------------
@app.get("/jobs/summary")
def job_summary():
    df = pd.read_sql("jobs", engine)

    return {
        "total_jobs": len(df),
        "remote_jobs": int(df["is_remote"].sum()),
        "top_company": df["company"].value_counts().idxmax(),
        "senior_jobs": int(df["is_senior"].sum())
    }

# ------------------------
# AI INSIGHTS (ML LAYER)
# ------------------------
@app.get("/insights")
def insights():
    try:
        df = pd.read_sql("jobs", engine)
        return generate_insights(df)
    except Exception as e:
        return {"error": str(e)}

# ------------------------
# REPORT (BUSINESS LAYER)
# ------------------------
@app.get("/report")
def report():
    try:
        df = pd.read_sql("jobs", engine)
        return generate_report(df)
    except Exception as e:
        return {"error": str(e)}