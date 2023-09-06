import dataclasses
from bson import ObjectId


@dataclasses.dataclass
class Product:
    _id: ObjectId
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    createdAt: str
    