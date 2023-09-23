import dataclasses

from src.domain.entities.product import Product


@dataclasses.dataclass
class CreateProductDto:
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    created_at: str
    user_telegram_id: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_entity(self) -> Product:
        return Product(
            name=self.name,
            price=self.price,
            description=self.description,
            image=self.image,
            categories=self.categories,
            quantity=self.quantity,
            created_at=self.created_at,
            user_telegram_id=self.user_telegram_id,
        )

    def to_dict(self):
        return dataclasses.asdict(self)
