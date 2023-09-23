import dataclasses

from src.domain.entities.user import User


@dataclasses.dataclass
class UserDto:
    telegram_username: str
    phone_number: int

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @classmethod
    def from_entity(cls, entity: User) -> "UserDto":
        return cls(
            telegram_username=entity.telegram_username,
            phone_number=entity.phone_number,
        )

    def to_dict(self):
        return dataclasses.asdict(self)
