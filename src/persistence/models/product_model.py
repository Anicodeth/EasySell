import dataclasses
import datetime

from src.domain.entities.product import Product


@dataclasses.dataclass
class ProductModel:
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductModel":
        return cls(
            name=entity.name,
            price=entity.price,
            description=entity.description,
            image=entity.image,
            categories=entity.categories,
            quantity=entity.quantity,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
            user_id=entity.user_id,
        )

    def to_dict(self):
        return dataclasses.asdict(self)
