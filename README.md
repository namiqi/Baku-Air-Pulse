# Baku-Air-Pulse

Automated ETL pipeline that monitors air quality across six major Caspian Sea port cities and stores structured measurements in Supabase for downstream analysis.

## Project Overview

`Baku-Air-Pulse` (also suitable for the name `AeroStream`) is a lightweight, production-style data pipeline that:
- **Extracts** hourly air pollution data from the OpenWeather Air Pollution API
- **Transforms** nested JSON into a clean relational payload
- **Loads** records into Supabase (PostgreSQL)

Tracked cities:
- Baku
- Sumqayit
- Makhachkala
- Aktau
- Turkmenbasy
- Bandar-e Anzali

## Tech Stack

- **Python** (pipeline logic)
- **OpenWeather API** (air quality source)
- **Supabase / PostgreSQL** (data storage)
- **GitHub Actions** (hourly automation)

## Architecture

The pipeline uses **GitHub Actions as a serverless scheduler**:
1. A cron trigger runs every hour.
2. The workflow installs Python dependencies from `requirements.txt`.
3. `main.py` executes once, loops through all configured Caspian cities, and inserts each record into Supabase.

This design removes the need for a dedicated VM or always-on server while keeping ingestion fully automated.

## Data Points Collected

Each run stores key air-quality indicators, including:
- **AQI** (Air Quality Index)
- **PM2.5**
- **PM10**
- **CO** (Carbon Monoxide)
- **NO2** (Nitrogen Dioxide)
- **City name**
- **Timestamp** (recorded by database defaults or insert timing)

## Setup Instructions

### 1) Local Development (`.env`)

Create a `.env` file in the project root with:

```env
OPENWEATHER_API_KEY=your_openweather_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_or_anon_key
```

### 2) GitHub Actions Secrets

In your GitHub repository, add the same keys under:
`Settings` -> `Secrets and variables` -> `Actions` -> `New repository secret`

Required secrets:
- `OPENWEATHER_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`

## Current Status

The pipeline is **live** and scheduled to run automatically every hour via GitHub Actions, continuously collecting air quality records for the configured Caspian cities.
