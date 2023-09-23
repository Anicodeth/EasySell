from typing import Dict, List

from bson import ObjectId
from fastapi import APIRouter, Body, Path

from src.application.features.user.dtos.create_user_dto import CreateUserDto
from src.application.features.user.dtos.user_dto import UserDto
from src.application.features.user.user_service import UserService
from src.persistence.db_client import DbClient
from src.persistence.repositories.user_repository import UserRepository
from src.webapi.responses.api_response import GenericResponse

db_client = DbClient()
user_repository = UserRepository(db_client)
user_service = UserService(user_repository)

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/")
def list_users() -> GenericResponse[List[UserDto]]:
    response = user_service.get_all()

    if response.is_success:
        return GenericResponse[List[UserDto]](
            success=True,
            value=[user.to_dict() for user in response.value],
            message="Users retrieved successfully",
        )
    return GenericResponse[List[UserDto]](
        success=False, value=None, message=response.error
    )


@user_router.post("/")
def create_user(user: CreateUserDto) -> GenericResponse[dict]:
    response = user_service.create(user)

    if response.is_success:
        return GenericResponse[Dict](
            success=True,
            value={"id": str(response.value)},
            message="User created successfully",
        )

    return GenericResponse[Dict](success=False, value={}, message=response.error)


@user_router.get("/{user_id}")
def get_user(user_id: str = Path(..., title="The user ID")) -> GenericResponse[UserDto]:
    response = user_service.get(ObjectId(user_id))

    if response.is_success:
        return GenericResponse[UserDto](
            success=True,
            value=response.value.to_dict(),
            message="User retrieved successfully",
        )
    return GenericResponse[UserDto](success=False, value=None, message=response.error)


@user_router.put("/{user_id}")
def update_user(
    user_id: str = Path(..., title="The user ID"),
    user: CreateUserDto = Body(..., title="Updated user data"),
) -> GenericResponse[None]:
    response = user_service.update(ObjectId(user_id), user)

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="User updated successfully"
        )

    return GenericResponse[None](success=False, value=None, message=response.error)


@user_router.delete("/{user_id}")
def delete_user(user_id: str = Path(..., title="The user ID")) -> GenericResponse[None]:
    response = user_service.delete(ObjectId(user_id))

    if response.is_success:
        return GenericResponse[None](
            success=True, value=None, message="User deleted successfully"
        )

    return GenericResponse[None](success=False, value=None, message=response.error)
