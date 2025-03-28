from fastapi import APIRouter, HTTPException, Depends
from src.models.user import TelegramUser
from src.services.database import db_service
from src.services.auth_validation import verify_credentials


router = APIRouter(
    tags=["User"]
)


@router.post("/users/", response_model=TelegramUser)
async def add_user(
        user: TelegramUser,
        access: str = Depends(verify_credentials)):
    existing_user = db_service.get_all_documents(
        "users",
        {"_id": user.id}
    )
    if existing_user:
        raise HTTPException(
            status_code=400, detail="User with this ID already exists"
        )
    db_service.add_document("users", user.model_dump(by_alias=True))
    return user


@router.put("/users/{user_id}", response_model=TelegramUser)
async def update_user(
        user_id: int, user: TelegramUser,
        access: str = Depends(verify_credentials)):
    existing_user = db_service.get_all_documents(
        "users",
        {"_id": user_id}
    )
    if not existing_user:
        raise HTTPException(
            status_code=404, detail="User with this ID does not exist"
        )
    if user_id != user.id:
        raise HTTPException(status_code=400, detail="User ID mismatch")
    db_service.update_document(
        "users", {"_id": user_id}, user.model_dump(by_alias=True))
    return user


@router.delete("/users/{user_id}")
async def delete_user(
        user_id: int,
        access: str = Depends(verify_credentials)):
    existing_user = db_service.get_all_documents(
        "users",
        {"_id": user_id}
    )
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_service.delete_document("users", {"_id": user_id})
    return {"detail": "User deleted successfully"}


@router.get("/users/{user_id}", response_model=TelegramUser)
async def get_user(
        user_id: int,
        access: str = Depends(verify_credentials)):
    existing_user = db_service.get_all_documents(
        "users",
        {"_id": user_id}
    )
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return existing_user[0]
