import dataclasses
from datetime import datetime

from bson import ObjectId


@dataclasses.dataclass
class Product:
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    user_telegram_id: str
    _id: str = None
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
