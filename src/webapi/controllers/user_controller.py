from typing import Dict, List

from bson import ObjectId
from fastapi import APIRouter, Body, Path

from src.application.features.product.dtos.product_dto import ProductDto
from src.application.features.user.dtos.create_user_dto import CreateUserDto
from src.application.features.user.dtos.user_dto import UserDto
from src.application.features.user.user_service import UserService
from src.persistence.repositories.unit_of_work import UnitOfWork
from src.webapi.responses.api_response import GenericResponse

unit_of_work = UnitOfWork()
user_service = UserService(unit_of_work)

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/")
def list_users() -> GenericResponse[List[UserDto]]:
    response = user_service.get_all()

    if response.is_success:
        return GenericResponse[List[UserDto]](
            success=True,
            value=[user.to_dict() for user in response.value],
            message="Users retrieved successfully.",
        )
    return GenericResponse[List[UserDto]](
        success=False,
        value=None,
        message="Users list could not be retrieved.",
        error=response.error,
    )


@user_router.post("/")
def create_user(user: CreateUserDto) -> GenericResponse[dict]:
    response = user_service.create(user)

    if response.is_success:
        return GenericResponse[Dict](
            success=True,
            value={"id": str(response.value)},
            message="User created successfully.",
        )

    return GenericResponse[Dict](
        success=False,
        value=None,
        message="User could not be created.",
        error=response.error,
    )


@user_router.get("/{user_id}")
def get_user(user_id: str = Path(..., title="The user ID")) -> GenericResponse[UserDto]:
    response = user_service.get(ObjectId(user_id))

    if response.is_success:
        return GenericResponse[UserDto](
            success=True,
            value=response.value.to_dict(),
            message="User retrieved successfully.",
        )
    return GenericResponse[UserDto](
        success=False,
        value=None,
        message="User could not be retrieved.",
        error=response.error,
    )


@user_router.put("/{user_id}")
def update_user(
    user_id: str = Path(..., title="The user ID"),
    user: CreateUserDto = Body(..., title="Updated user data"),
) -> GenericResponse:
    response = user_service.update(ObjectId(user_id), user)

    if response.is_success:
        return GenericResponse(
            success=True, value=None, message="User updated successfully."
        )

    return GenericResponse(
        success=False,
        value=None,
        message="User could not be updated.",
        error=response.error,
    )


@user_router.delete("/{user_id}")
def delete_user(user_id: str = Path(..., title="The user ID")) -> GenericResponse:
    response = user_service.delete(ObjectId(user_id))

    if response.is_success:
        return GenericResponse(
            success=True, value=None, message="User deleted successfully."
        )

    return GenericResponse(
        success=False,
        value=None,
        message="User could not be deleted.",
        error=response.error,
    )


@user_router.get("/{user_id}/products")
def get_all_products(
    user_id: str = Path(..., title="The user ID")
) -> GenericResponse[List[ProductDto]]:
    response = user_service.get_user_products(user_id)

    if response.is_success:
        return GenericResponse[List[ProductDto]](
            success=True,
            value=[product.to_dict() for product in response.value],
            message="Products for user retrieved successfully.",
        )
    return GenericResponse[List[ProductDto]](
        success=False,
        value=None,
        message="Products for user could not be retrieved.",
        error=response.error,
    )
