import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

from scraper.jobs_scraper import scrape_jobs
from cleaning.clean_jobs import clean_jobs
from database.db import init_db, save_to_db


def run_pipeline():
    print("=== PIPELINE STARTED ===")

    init_db()

    raw_data = scrape_jobs()
    print(f"Extracted: {len(raw_data)} records")

    cleaned_data = clean_jobs(raw_data)
    print(f"Cleaned: {len(cleaned_data)} records")

    save_to_db(cleaned_data)

    print("=== PIPELINE COMPLETE ===")


if __name__ == "__main__":
    run_pipeline()