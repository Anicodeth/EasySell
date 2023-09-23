import dataclasses

from src.domain.entities.user import User
from pydantic import BaseModel


class UserDto(BaseModel):
    _id: str
    telegram_username: str
    phone_number: str

    @classmethod
    def from_entity(cls, entity: User) -> "UserDto":
        return cls(
            _id=str(entity._id),
            telegram_username=entity.telegram_username,
            phone_number=entity.phone_number,
        )

    def to_dict(self):
        return self.dict()
