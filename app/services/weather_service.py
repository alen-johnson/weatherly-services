import httpx
from app.utils import WEATHER_API_KEY, WEATHER_API_URL

def get_weather_data(city: str):
    url = f"{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}"

    try:
        res = httpx.get(url, timeout=10)
        res.raise_for_status()
        print(res.status_code)

        return res.json()
    except httpx.HTTPStatusError as e:
        return {"Error: " f"Failed to fetch data: {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
        return {"Error: " f"Request failed  {str(e)}"}
