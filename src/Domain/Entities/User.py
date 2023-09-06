import dataclasses
from bson import ObjectId


@dataclasses.dataclass
class User:
    _id: ObjectId
    telegramId: str
    telegramUsername: str
    phoneNumber: int