from abc import ABCMeta, abstractmethod
from typing import List
from bson import ObjectId
from Application.UseCases.DTOs.User.create_user_dto import CreateUserDto
from Application.UseCases.DTOs.User.user_dto import UserDto


class UserRepositoyInterface(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[UserDto]:
        pass

    @abstractmethod
    def add(self, user: CreateUserDto) -> None:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> UserDto:
        pass

    @abstractmethod
    def update(self, id: ObjectId, user: CreateUserDto) -> None:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass