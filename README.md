# 🌍 Baku-Air-Pulse (MVP)

A lightweight Data Engineering pipeline that extracts real-time air quality data from the OpenWeather API, transforms the JSON response into a structured format, and loads it into a Supabase (PostgreSQL) database.

## 🚀 The Project Goal
This is a "No-Nonsense" data ingestion engine built to demonstrate a reliable ETL (Extract, Transform, Load) workflow. It currently monitors air quality metrics in **Baku, Azerbaijan**, and is designed to scale to multiple global cities.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Database:** Supabase (PostgreSQL)
- **Libraries:** `requests`, `python-dotenv`, `supabase-py`
- **Infrastructure:** GitHub Actions (Planned for 24/7 automation)

## 📊 Data Schema
The pipeline captures the following metrics every hour:
- **AQI:** Air Quality Index (1-5)
- **CO:** Carbon Monoxide
- **NO2:** Nitrogen Dioxide
- **PM2.5 & PM10:** Fine and coarse particulate matter
- **Timestamp:** Recorded in UTC with local offset

## 📁 Project Structure
```text
├── main.py              # The ETL Engine
├── .env                 # API Keys & DB Credentials (Hidden)
├── .gitignore           # Safety filter for secrets
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```
