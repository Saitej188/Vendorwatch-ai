# 📊 VendorWatch AI — B2B Job Market Intelligence System

## 🚀 Overview

VendorWatch AI is an end-to-end **data engineering and analytics system** that transforms raw job postings into actionable **business intelligence for market and hiring analysis**.

It simulates a real-world B2B use case where companies analyze:
- Competitor hiring activity
- Skill demand trends
- Remote vs on-site workforce distribution
- Seniority composition of teams
- Market hiring signals in real time

The system is built as a full pipeline:  
**Scraping → ETL → Database → API Layer → Analytics Dashboard → Intelligence Layer**

---

## 🎯 Problem Statement

Companies constantly lack structured visibility into:
- What skills are trending in the job market
- Which companies are aggressively hiring
- How remote-first the industry is becoming
- What roles are growing (senior vs junior distribution)

VendorWatch AI solves this by continuously converting raw job postings into structured intelligence.

---

## 🏗️ System Architecture

```text
                        ┌────────────────────┐
                        │  Job Data Source   │
                        └─────────┬──────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │   Scraper Layer    │
                        └─────────┬──────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │   ETL Pipeline     │
                        └─────────┬──────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │ Database (SQLite)  │
                        └─────────┬──────────┘
                                  │
                ┌─────────────────┴─────────────────┐
                ▼                                   ▼
     ┌────────────────────┐              ┌────────────────────┐
     │ FastAPI Backend    │              │ Streamlit Dashboard│
     └─────────┬──────────┘              └─────────┬──────────┘
               ▼                                   ▼
        ┌──────────────────────────────────────────────┐
        │        Intelligence Layer (Analytics)        │
        │  • Skill extraction (NLP keyword mining)     │
        │  • Hiring trend detection                    │
        │  • Company dominance scoring                 │
        │  • Remote vs onsite analysis                 │
        │  • Market intelligence reporting             │
        └──────────────────────────────────────────────┘
🧠 Key Features
🔹 Data Engineering Pipeline
Automated scraping of job listings
Pagination handling and fault tolerance
Missing data handling and normalization
Clean structured dataset generation
🔹 FastAPI Backend (Production-Style APIs)
Endpoint	Description
/jobs	Fetch all jobs
/jobs/search	Keyword-based search
/jobs/smart-search	Ranked intelligent search
/jobs/remote	Remote-only filtering
/jobs/summary	Business KPIs
/insights	AI-driven market insights
/report	Executive-level market report
🔹 Streamlit Analytics Dashboard
KPI overview (total jobs, remote %, senior roles)
Company distribution analysis
Remote vs onsite visualization
Interactive filtering system
Live API-driven insights

📸 Dashboard Screenshot:
(Add here: screenshots/dashboard.png)

🔹 Intelligence Layer (Business Analytics Engine)

The system includes a lightweight analytics engine that:

Extracts skills from job titles using NLP keyword mapping
Identifies top hiring companies
Computes remote hiring ratio
Measures senior vs junior distribution
Generates structured market intelligence reports

This simulates early-stage talent intelligence systems used in HR-tech & analytics startups.

📊 Example Output (Insights API)
{
  "total_jobs": 97,
  "remote_ratio": 0.29,
  "senior_ratio": 0.21,
  "top_companies": {
    "Careers In Travel": 8,
    "Aisles & Abroad": 2
  },
  "top_skills": {
    "python": 12,
    "ai": 9,
    "sql": 7
  }
}
📈 Market Intelligence Report

The system generates structured business insights such as:

Market hiring activity summary
Dominant hiring companies
High-demand skills
Workforce composition trends

📸 Report Screenshot:
(Add here: screenshots/report.png)

🛠️ Tech Stack
Python 3.10+
FastAPI (Backend APIs)
Streamlit (Dashboard UI)
Pandas (Data processing)
SQLAlchemy (ORM layer)
SQLite (Database)
Requests (API communication)
📂 Project Structure
vendorwatch-ai/
│
├── scraper/              # Web scraping logic
├── pipeline/             # ETL automation pipeline
├── database/             # DB connection (SQLAlchemy)
├── api/                  # Insights + report logic
├── ml/                   # Intelligence layer
│   ├── insights.py
│   └── report.py
├── dashboard/            # Streamlit UI
│   └── app.py
├── main.py               # FastAPI entry point
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/<your-username>/vendorwatch-ai.git
cd vendorwatch-ai
2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows
3. Install Dependencies
pip install -r requirements.txt
▶️ Running the System
Start Backend (FastAPI)
uvicorn main:app --reload

API runs at:

http://127.0.0.1:8000
Start Dashboard (Streamlit)
streamlit run dashboard/app.py
🧠 Intelligence Layer Design

Instead of heavy ML models, this system uses:

Fast rule-based NLP extraction
Frequency-based aggregation
Statistical market signals
Why this approach?
Highly interpretable
Production-friendly
Lightweight & scalable
Suitable for real-time pipelines
🔥 Key Engineering Highlights
End-to-end data pipeline architecture
Modular backend design (FastAPI)
Real-time dashboard with API integration
Smart ranking-based search engine
Lightweight AI analytics layer
Production-style folder structure
🚀 Future Improvements
Replace SQLite with PostgreSQL
Add vector search (FAISS / embeddings)
Deploy on cloud (AWS / Render)
Add predictive hiring trend model
Add real-time scheduler (Airflow / Cron)
👨‍💻 Project Summary

VendorWatch AI demonstrates a complete data engineering lifecycle:

Data extraction → transformation → storage → API layer → analytics → intelligence

It is designed to simulate how real-world B2B intelligence platforms operate.
1. 🖥️ Streamlit Dashboard
<img width="1912" height="941" alt="image" src="https://github.com/user-attachments/assets/2808892f-218a-4fe9-a523-959dbeafd13e" />
<img width="1908" height="821" alt="image" src="https://github.com/user-attachments/assets/e32f3d8a-76ad-4cf4-9006-325c81d6d4b6" />
<img width="1909" height="915" alt="image" src="https://github.com/user-attachments/assets/0565000b-0a5a-461b-ab24-cc42964f1a3b" />
📊 2. Job Table
<img width="1905" height="848" alt="image" src="https://github.com/user-attachments/assets/f2fd63fc-8272-4a8a-9ce0-bbef9f3d0783" />
⚡ 3. FastAPI Swagger UI
<img width="1919" height="939" alt="image" src="https://github.com/user-attachments/assets/f910438a-22a8-4f08-83fe-248bb9db7343" />
<img width="1900" height="957" alt="image" src="https://github.com/user-attachments/assets/40d42845-bbdb-47eb-b772-b2cf715f6d81" />
4.Insights JSON
<img width="1905" height="830" alt="image" src="https://github.com/user-attachments/assets/ddf908e7-a76c-417a-80b0-a40a732d1804" />
5.Market Report
<img width="1908" height="809" alt="image" src="https://github.com/user-attachments/assets/bcc1d5b1-ca70-4e20-a55d-783f943f2e68" />
