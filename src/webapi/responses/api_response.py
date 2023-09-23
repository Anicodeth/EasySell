from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel):
    success: bool = Field(...)
    message: str = Field(...)


class GenericResponse(ApiResponse, Generic[T]):
    value: Optional[T] = None
    error: Optional[str] = None
