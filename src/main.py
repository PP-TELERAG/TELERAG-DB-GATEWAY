from fastapi import Depends, FastAPI

from src.api.user import router as user_router
from src.services.auth_validation import verify_credentials
from src.settings.config import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(user_router, prefix="/api/v1")


@app.get("/")
async def root(access: str = Depends(verify_credentials)):
    return {"message": "Hello World"}


@app.get("/users/me")
def read_current_user(access: str = Depends(verify_credentials)):
    return {"message": f"Hello, {access}!"}
