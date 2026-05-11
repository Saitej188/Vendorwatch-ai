import pandas as pd
from database.db import engine


def generate_insights():
    df = pd.read_sql("jobs", engine)

    insights = {
        "total_jobs": len(df),
        "remote_percentage": round(df["is_remote"].mean() * 100, 2),
        "senior_percentage": round(df["is_senior"].mean() * 100, 2),
        "top_companies": df["company"].value_counts().head(5).to_dict(),
        "most_common_role": df["title"].mode()[0] if not df.empty else None
    }

    return insights