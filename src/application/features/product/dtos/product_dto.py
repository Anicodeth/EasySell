from datetime import datetime
from typing import Dict

from pydantic import BaseModel

from src.domain.entities.product import Product


class ProductDto(BaseModel):
    id: str
    name: str
    price: int
    description: str
    image: str
    quantity: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductDto":
        return cls(
            id=str(entity._id),
            name=entity.name,
            price=entity.price,
            description=entity.description,
            image=entity.image,
            quantity=entity.quantity,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_dict(self) -> Dict:
        return self.dict()
