from fastapi import APIRouter
from app.services.weather_service import get_weather_data
from app.services.weather_service import get_air_data
from app.services.weather_service import get_air_quality_index

router = APIRouter()


@router.get("/{city}")
def get_weather(city: str):
    return get_weather_data(city)

@router.get("/{city}/air-quality")
def get_air_quality(city: str):

    air_data = get_air_data(city)

    if "air_quality" in air_data:
        air_data["aqi"] = get_air_quality_index(air_data["air_quality"])

    return air_data
