from typing import TypeVar, Optional, Generic

from pydantic import BaseModel, Field

T = TypeVar("T")


class ApiResponse(BaseModel):
    success: bool = Field(...)
    message: str = Field(...)


class GenericResponse(ApiResponse, Generic[T]):
    value: T = None
    error: Optional[dict] = None
