from fastapi import APIRouter
from app.services import get_weather_data

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Welcome to weatherly"}

@router.get("/weather/{city}")
def get_weather(city: str):
    return get_weather_data(city)