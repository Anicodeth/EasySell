from typing import TypeVar, Generic, Optional, Dict
import json

T = TypeVar("T")


class Response[Generic[T]]:
    def __init__(self, status_code: str, message: str, data: Optional[T] = None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
