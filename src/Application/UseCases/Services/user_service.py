from typing import List

from bson import ObjectId

from Application.Contracts.iuser_repository import UserRepositoyInterface
from Application.Contracts.iuser_service import UserServiceInterface
from Application.UseCases.DTOs.User.create_user_dto import CreateUserDto
from Application.UseCases.DTOs.User.user_dto import UserDto


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoyInterface) -> None:
        self.user_repository = user_repository

    def list(self) -> List[UserDto]:
        self.user_repository.list()

    def add(self, user: CreateUserDto) -> None:
        self.user_repository.add(user)

    def get(self, id: ObjectId) -> UserDto:
        self.user_repository.get(id)

    def update(self, id: ObjectId, user: CreateUserDto) -> None:
        self.user_repository.update(id, user)

    def delete(self, id: ObjectId) -> None:
        self.user_repository.delete(id)
