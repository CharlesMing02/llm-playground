import requests

def fetch_weather_forecast(latitude, longitude, hourly, daily, temperature_unit, timezone, forecast_days):
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": hourly,
        "daily": daily,
        "temperature_unit": temperature_unit,
        "timezone": timezone,
        "forecast_days": forecast_days
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def main():
    # Example usage:
    forecast_data = fetch_weather_forecast(
        latitude=37.8716,
        longitude=-122.2728,
        hourly="temperature_2m,precipitation_probability,precipitation",
        daily="temperature_2m_max,temperature_2m_min,sunrise,sunset",
        temperature_unit="fahrenheit",
        timezone="America/Los_Angeles",
        forecast_days=1
    )

    print(forecast_data)

if __name__ == '__main__':
    main()