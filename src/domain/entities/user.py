import dataclasses
from datetime import datetime

from bson import ObjectId


@dataclasses.dataclass
class User:
    telegram_id: str
    telegram_username: str
    phone_number: str
    _id: str = None
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
