from pydantic import BaseModel, Field
from typing import Optional


class TelegramChannel(BaseModel):
    id: int = Field(alias="_id")
    username: Optional[str]
    channel_type: str
    status: str

    class Config:
        populate_by_name = True
