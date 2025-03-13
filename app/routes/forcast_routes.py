from fastapi import APIRouter
from app.services.forecast_service import get_forecast_data

router = APIRouter()


@router.get("/{city}")
def get_forecast(city: str):
    return get_forecast_data(city)