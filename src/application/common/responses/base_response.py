from typing import TypeVar, Generic, Optional, Dict

T = TypeVar("T")
E = TypeVar("E")


class BaseResponse(Generic[T, E]):
    def __init__(self, is_success: bool, message: str, data: Optional[T] = None, error: Optional[E] = None):
        self.is_success = is_success
        self.message = message
        self.value = data
        self.error = error

    def to_dict(self) -> Dict[str, any]:
        return {
            "is_success": self.is_success,
            "message": self.message,
            "data": self.value,
            "error": self.error,
        }

    @classmethod
    def success(cls, message: str, data: Optional[T] = None) -> 'BaseResponse[T, E]':
        return cls(is_success=True, message=message, data=data)

    @classmethod
    def error(cls, message: str, error: Optional[E] = None) -> 'BaseResponse[T, E]':
        return cls(is_success=False, message=message, error=error)
