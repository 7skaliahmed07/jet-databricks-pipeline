import requests
import pandas as pd

def fetch_amsterdam_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.3676,
        "longitude":4.9041,
        "hourly": "temperature_2m,precipitation,wind_speed_10m",
        "timezone": "Europe/Amsterdam",
        "past_days": 1,
        "forecast_days": 1
    }
    
    response = requests.get(url,params=params)
    
    response.raise_for_status()
    
    data = response.json()
    
    hourly_data = data["hourly"]
    
    df_weather = pd.DataFrame({
        "timestamp": hourly_data['time'],
        "temperature_celsius" :hourly_data["temperature_2m"],
        "precipitation_mm":hourly_data["precipitation"],
        "wind_speed_kmh": hourly_data['wind_speed_10m']     
    })
    
    return df_weather

if __name__ =="__main__":
    print("Fetching weather data for the Amsterdam Please Wait..!")
    
    df_weather = fetch_amsterdam_weather()
    
    file_name = "raw_weather.csv"
    df_weather.to_csv(file_name, index=False)
    
    print(f"Data has been fethed Successfully and saved to {file_name}")
    