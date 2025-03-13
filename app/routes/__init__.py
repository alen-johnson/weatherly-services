from fastapi import APIRouter

from .weather_routes import router as weather_router
from .forcast_routes import router as forcast_router
from .news_routes import router as news_router

router = APIRouter()

router.include_router(weather_router, prefix="/weather", tags=["Weather"])
router.include_router(forcast_router, prefix="/forecast", tags=["Forecast"])
router.include_router(news_router, prefix="/news", tags=["News"])