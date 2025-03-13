import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

WEATHER_API_URL ='https://api.weatherapi.com/v1/current.json'
FORECAST_API_URL = 'https://api.weatherapi.com/v1/forecast.json'
NEWS_API_URL = 'https://newsapi.org/v2/everything'