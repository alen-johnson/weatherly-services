from fastapi import APIRouter
from app.services.news_service import get_news_data

router = APIRouter()

@router.get("/{city}")
def get_news(city: str):
    return get_news_data(city)