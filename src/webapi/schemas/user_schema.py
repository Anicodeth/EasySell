from pydantic import BaseModel


class UserBase(BaseModel):
    telegram_id: str
    telegram_username: str
    phone_number: str


class UserCreate(UserBase):
    pass
