import dataclasses
from datetime import datetime

from src.domain.entities.user import User


@dataclasses.dataclass
class UserModel:
    telegram_id: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @classmethod
    def from_entity(cls, entity: User) -> "UserModel":
        return cls(
            telegram_id=entity.telegram_id,
            phone_number=entity.phone_number,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    def to_dict(self):
        return dataclasses.asdict(self)
