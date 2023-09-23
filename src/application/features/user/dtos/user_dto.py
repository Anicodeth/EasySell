from typing import Dict

from src.domain.entities.user import User
from pydantic import BaseModel


class UserDto(BaseModel):
    id: str
    telegram_username: str
    telegram_id: str
    phone_number: str

    @classmethod
    def from_entity(cls, entity: User) -> "UserDto":
        print(entity._id)
        return cls(
            id=str(entity._id),
            telegram_username=entity.telegram_username,
            telegram_id=entity.telegram_id,
            phone_number=entity.phone_number,
        )

    def to_dict(self) -> Dict:
        return self.dict()
