import httpx
from app.utils import WEATHER_API_KEY, WEATHER_API_URL

def get_weather_data(city: str):
    url = f"{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}&aqi=no"

    try:
        res = httpx.get(url, timeout=10)
        res.raise_for_status()
        print(res.status_code)

        return res.json()
    except httpx.HTTPStatusError as e:
        return {"Error: " f"Failed to fetch data: {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
        return {"Error: " f"Request failed  {str(e)}"}

def get_air_data(city:str):
    url =f"{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={city}&aqi=yes"

    try:
        res = httpx.get(url, timeout=10)
        res.raise_for_status()
        print(res.status_code)
        data = res.json()
        return {
            "air_quality": data["current"].get("air_quality", "No AQI data available")
        }
    except httpx.HTTPStatusError as e:
        return {"Error: " f"Failed to fetch data: {e.response.status_code} {e.response.text}"}
    except httpx.RequestError as e:
        return {"Error: " f"Request failed  {str(e)}"}
    

pm25_breakpoints = [(0, 50), (12, 100), (35.4, 150), (55.4, 200), (150.4, 300), (250.4, 500)]
pm10_breakpoints = [(0, 50), (54, 100), (154, 150), (254, 200), (354, 300), (424, 500)]
o3_breakpoints = [(0, 50), (54, 100), (70, 150), (85, 200), (105, 300), (200, 500)]

def get_aqi(concentration, breakpoints):

    for i in range(len(breakpoints) - 1):
        c_low, c_high = breakpoints[i][0], breakpoints[i + 1][0]
        aqi_low, aqi_high = breakpoints[i][1], breakpoints[i + 1][1]

        if c_low <= concentration <= c_high:
            return ((aqi_high - aqi_low) / (c_high - c_low)) * (concentration - c_low) + aqi_low
    
    return None  

def get_aqi_category(aqi):

    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

def get_air_quality_index(air_quality_data):

    pm25 = air_quality_data.get("pm2_5", 0)
    pm10 = air_quality_data.get("pm10", 0)
    o3 = air_quality_data.get("o3", 0)

    pm25_aqi = get_aqi(pm25, pm25_breakpoints)
    pm10_aqi = get_aqi(pm10, pm10_breakpoints)
    o3_aqi = get_aqi(o3, o3_breakpoints)


    overall_aqi = max(pm25_aqi, pm10_aqi, o3_aqi)

    return {
        "aqi": overall_aqi,
        "category": get_aqi_category(overall_aqi),
        "pollutants": {
            "PM2.5": pm25_aqi,
            "PM10": pm10_aqi,
            "O3": o3_aqi
        }
    }