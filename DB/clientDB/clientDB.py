from DB.IClientDB import IClientBD
from pymongo import MongoClient
from bson.objectid import ObjectId

from UserClass.DataUser import DataUser
from UserClass.User import User

from typing import List


class ClientBD(IClientBD):

    def __init__(self):
        self.DB_name = "Avrora"
        self.Collection_user_name = "Users"

        self.mongo_client = MongoClient("localhost", 27017)

        self.DB = self.mongo_client[self.DB_name]

        self.Collection_user = self.DB[self.Collection_user_name]

    def check_user(self, data: DataUser) -> bool:

        if not self.Collection_user.find_one({"nickname": data.nickname}):
            return False

        return True

    def recv_user(self, old_data: DataUser, new_data: DataUser):

        new_data = {
            "name": new_data.name,
            "nickname": new_data.nickname,
            "first_key": new_data.first_key,
            "second_key": new_data.second_key
        }

        self.Collection_user.replace_one({"nickname": old_data.nickname}, new_data)

    def set_user(self, data: DataUser) -> ObjectId:

        post = {
            "name": data.name,
            "nickname": data.nickname,
            "first_key": data.first_key,
            "second_key": data.second_key
        }

        id = self.Collection_user.insert_one(post).inserted_id

        return ObjectId(id)

    def delete_user(self, data: DataUser):
        self.Collection_user.delete_one({"nickname": data.nickname})

    def All_users(self):

        list_user: List[User] = []

        for user in self.Collection_user.find():

            list_user.append(User(user["name"], user["nickname"], user["first_key"], user["second_key"], user["_id"]))

        return list_user

