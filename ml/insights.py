import pandas as pd

SKILLS = ["python", "sql", "aws", "excel", "java", "react", "ml", "ai", "docker"]


def extract_skills(text):
    if not isinstance(text, str):
        return []
    text = text.lower()
    return [s for s in SKILLS if s in text]


def generate_insights(df: pd.DataFrame):

    if df is None or df.empty:
        return {"error": "no data"}

    df = df.copy()

    df["company"] = df.get("company", "unknown").fillna("unknown")
    df["title"] = df.get("title", "").fillna("")

    df["is_remote"] = df.get("is_remote", False)
    df["is_senior"] = df.get("is_senior", False)

    df["is_remote"] = df["is_remote"].fillna(False).astype(bool)
    df["is_senior"] = df["is_senior"].fillna(False).astype(bool)

    total = len(df)

    return {
        "total_jobs": total,
        "remote_ratio": round(df["is_remote"].mean(), 2),
        "senior_ratio": round(df["is_senior"].mean(), 2),
        "top_companies": df["company"].value_counts().head(5).to_dict(),
        "top_skills": df["title"].apply(extract_skills).explode().value_counts().head(10).to_dict()
    }