from typing import List
from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    description: str
    image: str
    categories: List[str]
    quantity: int
    created_at: str
    user_telegram_id: str


class ProductCreate(ProductBase):
    pass
