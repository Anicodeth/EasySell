from typing import List

from bson import ObjectId

from src.application.common.responses.base_response import BaseResponse
from src.application.contracts.persistence.user_repository_contract import \
    UserRepositoryContract
from src.application.features.user.dtos.create_user_dto import CreateUserDto
from src.application.features.user.dtos.user_dto import UserDto


class UserService:
    def __init__(self, user_repository: UserRepositoryContract) -> None:
        self.user_repository: UserRepositoryContract = user_repository

    def get_all(self) -> BaseResponse[List[UserDto], str]:
        try:
            users = self.user_repository.list()
            return BaseResponse.success(
                "Users retrieved successfully.", list(map(UserDto.from_entity, users))
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving users.", "Internal server error."
            )

    def create(self, user: CreateUserDto) -> BaseResponse[ObjectId, str]:
        try:
            user_id = self.user_repository.create(user.to_entity())
            return BaseResponse.success("User created successfully.", user_id)
        except Exception:
            return BaseResponse.error("Error creating user.", "Internal server error.")

    def get(self, user_id: ObjectId) -> BaseResponse[UserDto, str]:
        try:
            user = self.user_repository.get(user_id)
            return BaseResponse.success(
                "User retrieved successfully.", UserDto.from_entity(user)
            )
        except Exception:
            return BaseResponse.error(
                "Error retrieving user.", "Internal server error."
            )

    def update(self, user_id: ObjectId, user: CreateUserDto) -> BaseResponse[None, str]:
        try:
            is_updated = self.user_repository.update(user_id, user.to_entity())
            if not is_updated:
                return BaseResponse.error("User updating failed.", "User not found.")
            return BaseResponse.success("User updated successfully.", None)
        except Exception:
            return BaseResponse.error("Error updating user.", "Internal server error.")

    def delete(self, user_id: ObjectId) -> BaseResponse[None, str]:
        try:
            is_deleted = self.user_repository.delete(user_id)
            if not is_deleted:
                return BaseResponse.error("User deletion failed.", "User not found.")
            return BaseResponse.success("User deleted successfully.", None)
        except Exception:
            return BaseResponse.error("Error deleting user.", "Internal server error.")
