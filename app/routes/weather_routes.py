from fastapi import APIRouter
from app.services.weather_service import get_weather_data


router = APIRouter()


@router.get("/{city}")
def get_weather(city: str):
    return get_weather_data(city)