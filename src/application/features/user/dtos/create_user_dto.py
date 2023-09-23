from pydantic import BaseModel
from src.domain.entities.user import User


class CreateUserDto(BaseModel):
    telegram_id: str
    phone_number: str

    @classmethod
    def from_dict(cls, d) -> "CreateUserDto":
        return cls(**d)

    def to_entity(self) -> User:
        return User(
            telegram_id=self.telegram_id,
            phone_number=self.phone_number,
        )
