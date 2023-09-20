import dataclasses


@dataclasses.dataclass
class CreateProductDto:
    name: str
    price: int
    description: str
    image: str
    categories: list
    quantity: int
    createdAt: str
    userTelegramId: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
