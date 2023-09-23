from pydantic import BaseModel

from src.domain.entities.product import Product


class ProductDto(BaseModel):
    _id: str
    name: str
    price: int
    description: str
    image: str
    quantity: int
    created_at: str

    @classmethod
    def from_entity(cls, entity: Product) -> "ProductDto":
        return cls(
            _id=str(entity._id),
            name=entity.name,
            price=entity.price,
            description=entity.description,
            image=entity.image,
            quantity=entity.quantity,
            created_at=entity.created_at,
        )

    def to_dict(self):
        return self.dict()
