import dataclasses

from pydantic import BaseModel

from src.domain.entities.product import Product


@dataclasses.dataclass
class CreateProductDto(BaseModel):
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    user_telegram_id: str

    @classmethod
    def from_dict(cls, d) -> "CreateProductDto":
        return cls(**d)

    def to_entity(self) -> Product:
        return Product(
            name=self.name,
            price=self.price,
            description=self.description,
            image=self.image,
            categories=self.categories,
            quantity=self.quantity,
            user_telegram_id=self.user_telegram_id,
        )
