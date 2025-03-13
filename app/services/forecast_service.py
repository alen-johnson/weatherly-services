import httpx
from app.utils import FORECAST_API_URL, WEATHER_API_KEY


def get_forecast_data(city:str, days: int = 8):
    url = f"{FORECAST_API_URL}?key={WEATHER_API_KEY}&q={city}&days={days}"

    try:
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        return response.json()
    except httpx.HTTPStatusError as e:
            return {"error:" : f"failed to fetch data : {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
         return {"error:" f"Request failed : {str(e)}"}


