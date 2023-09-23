from abc import ABCMeta, abstractmethod
from typing import List

from bson import ObjectId

from src.domain.entities.user import User


class ABCUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def list(self) -> List[User]:
        pass

    @abstractmethod
    def create(self, user: User) -> ObjectId:
        pass

    @abstractmethod
    def get(self, id: ObjectId) -> User:
        pass

    @abstractmethod
    def update(self, id: ObjectId, user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> bool:
        pass
