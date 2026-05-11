from sqlalchemy import create_engine, text
import os
import pandas as pd

# =========================
# DB CONNECTION
# =========================
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///vendorwatch.db")
engine = create_engine(DATABASE_URL, echo=False)

# =========================
# INIT DB
# =========================
def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            url TEXT,
            is_remote BOOLEAN,
            is_senior BOOLEAN
        )
        """))

    print("Database initialized")

# =========================
# SAVE TO DB
# =========================
def save_to_db(data):
    if data is None:
        print("No data received")
        return

    if isinstance(data, pd.DataFrame):
        if data.empty:
            print("Empty DataFrame")
            return
        data = data.to_dict(orient="records")

    with engine.begin() as conn:
        conn.execute(text("DELETE FROM jobs"))

        for job in data:
            conn.execute(
                text("""
                INSERT INTO jobs (
                    title, company, location, url, is_remote, is_senior
                )
                VALUES (
                    :title, :company, :location, :url, :is_remote, :is_senior
                )
                """),
                {
                    "title": job.get("title"),
                    "company": job.get("company"),
                    "location": job.get("location"),
                    "url": job.get("url"),
                    "is_remote": job.get("is_remote", False),
                    "is_senior": job.get("is_senior", False),
                }
            )

    print(f"Inserted {len(data)} jobs into database")