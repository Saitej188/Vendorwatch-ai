# VendorWatch AI Architecture

## System Flow

Scraper → Cleaning → SQLite Database → FastAPI → Streamlit Dashboard

## Design Decisions

- SQLite used for simplicity and portability
- Pandas used for fast transformation
- FastAPI used for lightweight API layer
- Streamlit used for quick business dashboard

## Key Features

- Real-time job scraping
- Data cleaning & enrichment
- REST API for data access
- Interactive dashboard for insights

## Engineering Trade-offs

- No distributed system (scope control)
- No cloud DB (kept local for simplicity)
- No ML model (focus on pipeline quality)