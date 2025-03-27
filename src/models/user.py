from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TelegramUser(BaseModel):
    id: int = Field(alias="_id")
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    register_date: datetime
    is_active: bool = True

    class Config:
        populate_by_name = True
