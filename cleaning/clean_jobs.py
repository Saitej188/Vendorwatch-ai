import pandas as pd


def clean_jobs(raw_jobs):
    df = pd.DataFrame(raw_jobs)

    # ---------------- CLEANING ----------------
    df["title"] = df["title"].str.lower().str.strip()
    df["company"] = df["company"].fillna("unknown").str.strip()
    df["location"] = df["location"].fillna("remote").str.strip()

    # remove bad rows
    df = df.dropna(subset=["title"])

    # remove duplicates
    df = df.drop_duplicates(subset=["title", "company"])

    # feature engineering (VERY IMPORTANT)
    df["is_remote"] = df["location"].str.contains("remote", case=False, na=False)
    df["is_senior"] = df["title"].str.contains("senior|lead|staff", case=False, na=False)

    return df