import dataclasses

from bson import ObjectId


@dataclasses.dataclass
class Product:
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    created_at: str
    user_telegram_id: str
    _id: str = None

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
