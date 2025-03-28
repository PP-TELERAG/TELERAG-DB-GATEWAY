from fastapi import FastAPI

from src.api.user import router as user_router
from src.api.channel import router as channel_router
from src.settings.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(user_router, prefix="/api/v1")
app.include_router(channel_router, prefix="/api/v1")
