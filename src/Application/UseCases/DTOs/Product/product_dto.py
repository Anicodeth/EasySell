import dataclasses

from bson import ObjectId


@dataclasses.dataclass
class ProductDto:
    _id: ObjectId
    name: str
    price: int
    description: str
    image: str
    quantity: int
    createdAt: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
