import dataclasses
from datetime import datetime


@dataclasses.dataclass
class User:
    telegram_id: str
    phone_number: str

    _id: str = None
    updated_at: datetime = datetime.now()
    created_at: datetime = datetime.now()

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
