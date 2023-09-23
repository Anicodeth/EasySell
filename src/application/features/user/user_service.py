from typing import List

from bson import ObjectId

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.persistence.abc_unit_of_work import \
    ABCUnitOfWork
from src.application.features.product.dtos.product_dto import ProductDto
from src.application.features.user.dtos.create_user_dto import CreateUserDto
from src.application.features.user.dtos.user_dto import UserDto


class UserService:
    def __init__(self, unit_of_work: ABCUnitOfWork) -> None:
        self.unit_of_work: ABCUnitOfWork = unit_of_work

    def get_all(self) -> BaseResponse[List[UserDto], str]:
        try:
            users = self.unit_of_work.user_repository.list()
            return BaseResponse.success(
                "Users retrieved successfully.", list(map(UserDto.from_entity, users))
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving users.", "Internal server error."
            )

    def create(self, user: CreateUserDto) -> BaseResponse[ObjectId, str]:
        try:
            user_id = self.unit_of_work.user_repository.create(user.to_entity())
            return BaseResponse.success("User created successfully.", user_id)
        except Exception:
            return BaseResponse.error("Error creating user.", "Internal server error.")

    def get(self, user_id: ObjectId) -> BaseResponse[UserDto, str]:
        try:
            user = self.unit_of_work.user_repository.get(user_id)
            return BaseResponse.success(
                "User retrieved successfully.", UserDto.from_entity(user)
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving user.", "Internal server error."
            )

    def update(self, user_id: ObjectId, user: CreateUserDto) -> BaseResponse[None, str]:
        try:
            is_updated = self.unit_of_work.user_repository.update(
                user_id, user.to_entity()
            )
            if not is_updated:
                return BaseResponse.error("User updating failed.", "User not found.")
            return BaseResponse.success("User updated successfully.", None)
        except Exception:
            return BaseResponse.error("Error updating user.", "Internal server error.")

    def delete(self, user_id: ObjectId) -> BaseResponse[None, str]:
        try:
            is_deleted = self.unit_of_work.user_repository.delete(user_id)
            if not is_deleted:
                return BaseResponse.error("User deletion failed.", "User not found.")
            return BaseResponse.success("User deleted successfully.", None)
        except Exception:
            return BaseResponse.error("Error deleting user.", "Internal server error.")

    # Product related methods
    def get_user_products(self, user_id: str):
        try:
            products = self.unit_of_work.product_repository.get_user_products(user_id)
            return BaseResponse.success(
                "Products for user retrieved successfully.",
                list(map(ProductDto.from_entity, products)),
            )
        except Exception:
            return BaseResponse.error(
                "Error getting products of user.", "Internal server error."
            )
