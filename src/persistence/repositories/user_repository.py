from typing import Dict, List

from bson import ObjectId

from src.application.contracts.persistence.user_repository_contract import \
    UserRepositoryContract
from src.domain.entities.user import User
from src.persistence.db_client import DbClient
from src.persistence.models.user_model import UserModel


class UserRepository(UserRepositoryContract):
    def __init__(self, db: DbClient):
        self.users = db.get_collection("users")

    def list(self) -> List[User]:
        return list(map(User.from_dict, self.users.find()))

    def create(self, user: User) -> ObjectId:
        user_id = self.users.insert_one(UserModel.from_entity(user).to_dict()).inserted_id
        return user_id

    def get(self, user_id: ObjectId) -> User:
        return User.from_dict(self.users.find_one({"_id": user_id}))

    def update(self, user_id: ObjectId, user: User) -> bool:
        status = self.users.update_one({"_id": user_id}, {"$set": UserModel.from_entity(user).to_dict()})
        return status.modified_count > 0

    def delete(self, user_id: ObjectId) -> bool:
        status = self.users.delete_one({"_id": user_id})
        return status.deleted_count > 0
