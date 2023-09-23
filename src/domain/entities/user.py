import dataclasses

from bson import ObjectId


@dataclasses.dataclass
class User:
    telegram_id: str
    telegram_username: str
    phone_number: str
    _id: str = None

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
