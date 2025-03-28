from fastapi import APIRouter, HTTPException, Depends
from src.models.channel import TelegramChannel
from src.services.database import db_service
from src.services.auth_validation import verify_credentials


router = APIRouter(
    tags=["Channel"]
)


@router.post("/channels/add", response_model=TelegramChannel)
async def add_channel(
        channel: TelegramChannel,
        access: str = Depends(verify_credentials)):
    # Проверяем, существует ли канал с данным _id
    existing_channel = db_service.get_all_documents(
        "channels", {"_id": channel.id}
    )
    if existing_channel:
        raise HTTPException(
            status_code=400, detail="Channel with this ID already exists"
        )
    # Добавляем канал
    db_service.add_document("channels", channel.model_dump(by_alias=True))
    return channel


@router.put("/channels/{channel_id}", response_model=TelegramChannel)
async def update_channel(
        channel_id: int, channel: TelegramChannel,
        access: str = Depends(verify_credentials)):
    # Проверяем, существует ли канал с данным _id
    existing_channel = db_service.get_all_documents(
        "channels", {"_id": channel_id}
    )
    if not existing_channel:
        raise HTTPException(
            status_code=404, detail="Channel with this ID does not exist"
        )
    if channel_id != channel.id:
        raise HTTPException(status_code=400, detail="Channel ID mismatch")
    # Обновляем канал
    db_service.update_document(
        "channels", {"_id": channel_id}, channel.model_dump(by_alias=True))
    return channel


@router.delete("/channels/{channel_id}")
async def delete_channel(
        channel_id: int,
        access: str = Depends(verify_credentials)):
    existing_channel = db_service.get_all_documents(
        "channels", {"_id": channel_id}
    )
    if not existing_channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    db_service.delete_document("channels", {"_id": channel_id})
    return {"detail": "Channel deleted successfully"}


@router.post("/channels/get", response_model=list[TelegramChannel])
async def get_channel(
        select_params: dict = None,
        access: str = Depends(verify_credentials)):
    # Если параметры фильтрации пусты, устанавливаем пустой словарь
    if not select_params:
        select_params = {}
    # Получаем каналы с указанными параметрами
    existing_channels = db_service.get_all_documents("channels", select_params)
    if not existing_channels:
        raise HTTPException(status_code=404, detail="No channels found")
    return existing_channels
