import dataclasses

from src.domain.entities.user import User


@dataclasses.dataclass
class CreateUserDto:
    telegram_id: str
    telegram_username: str
    phone_number: int

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_entity(self) -> User:
        return User(
            telegram_id=self.telegram_id,
            telegram_username=self.telegram_username,
            phone_number=self.phone_number,
        )

    def to_dict(self):
        return dataclasses.asdict(self)