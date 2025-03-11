import httpx
import os
from dotenv import load_dotenv


load_dotenv()
WEATHER_API_URL ='https://api.weatherapi.com/v1/current.json'
FORECAST_API_URL = 'https://api.weatherapi.com/v1/forecast.json'
API_KEY =  os.getenv("WEATHER_API_KEY")


def get_weather_data(city: str):
    url = f"{WEATHER_API_URL}?key={API_KEY}&q={city}"

    try:
        response = httpx.get(url,timeout=10)
        response.raise_for_status()
        print(response.status_code)

        return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"Failed to fetch data  : {e.response.status_code} {e.response.text} "}
    except httpx.RequestError as e:
        return {"error": f"Request failed : {str(e)}"}
    


def get_forecast_data(city:str, days: int = 8):
    url = f"{FORECAST_API_URL}?key={API_KEY}&q={city}&days={days}"

    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        return response.json()
    except httpx.HTTPStatusError as e:
            return {"error:" : f"failed to fetch data : {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
         return {"error:" f"Request failed : {str(e)}"}
