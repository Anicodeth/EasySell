from typing import Dict, List

from bson import ObjectId
from pymongo import MongoClient

from Application.UseCases.DTOs.User.create_user_dto import CreateUserDto
from Application.UseCases.DTOs.User.user_dto import UserDto
from Application.Contracts.iuser_repository import UserRepositoyInterface

conn_string = "mongodb+srv://afmtoday:OlxwPFCF0rLMnA3e@cluster0.edrrjyh.mongodb.net/easysell?retryWrites=true&w=majority"


class UserRepository(UserRepositoyInterface):
    def __init__(self, data: List[Dict[str, object]]):
        self.data = data
        self.client = MongoClient(conn_string)
        self.db = self.client.rentomatic
        self.users = self.db.users

    def list(self) -> List[UserDto]:
        return [UserDto.from_dict(user) for user in list(self.user.find())]

    def add(self, user: CreateUserDto) -> ObjectId:
        user_id = self.users.insert_one(user).inserted_id
        return user_id

    def get(self, id: ObjectId) -> UserDto:
        return UserDto.from_dict(self.users.find_one({"_id": id}))

    def update(self, id: ObjectId, room: CreateUserDto) -> None:
        return self.users.update_one({"_id": id}, {"$set": room})

    def delete(self, id: ObjectId) -> None:
        return self.users.delete_one({"_id": id})