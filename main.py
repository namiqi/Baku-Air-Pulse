import os
import requests
from supabase import create_client
from dotenv import load_dotenv

# 1. Load the variables from your .env file
load_dotenv()

# 2. Setup the connections
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
weather_key = os.getenv("OPENWEATHER_API_KEY")

# create_client expects the Supabase project URL, not the REST endpoint path.
if url:
    url = url.rstrip("/")
    if url.endswith("/rest/v1"):
        url = url[:-8]

# Initialize Supabase
supabase = create_client(url, key)

def fetch_and_save_air_quality(city_name, lat, lon):
    print("Starting the pipeline...")
    
    weather_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={weather_key}"

    try:
        # 4. Extraction
        response = requests.get(weather_url)
        response.raise_for_status() # This checks if the API call actually worked
        data = response.json()['list'][0]

        # 5. Transformation (Mapping API data to our SQL columns)
        payload = {
            "city_name": city_name,
            "aqi": data['main']['aqi'],
            "co": data['components']['co'],
            "no2": data['components']['no2'],
            "pm2_5": data['components']['pm2_5'],
            "pm10": data['components']['pm10']
        }

        # 6. Loading to Supabase (Simplified for the public schema)
        print(f"Sending {city_name} AQI data to Supabase...")
        print(f"Payload: {payload}")
        
        # We removed schema="air_quality" to avoid the error
        insert_response = supabase.table("logs").insert(payload).execute()
        print(f"Supabase insert response: {insert_response}")
        
        print("Success! Data is now in your database.")

    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    print("Starting one-time air quality sync...")
    fetch_and_save_air_quality("Baku", 40.40, 49.86)

