from DB.clientDB.clientDB import ClientBD
from DB.IClientDB import IClientBD
from DB.Cache.Cache import Cache

from UserClass.DataUser import DataUser
import hashlib

class ClientDBProxy(IClientBD):

    def __init__(self):
        self.clientBD = ClientBD()

        for user in self.clientBD.All_users():
            Cache.set_user(DataUser.FromUser(user))

    def hash(self, data: DataUser):
        data.first_key = hashlib.sha256(data.first_key.encode("utf-8")).hexdigest()
        data.second_key = hashlib.sha256(data.second_key.encode("utf-8")).hexdigest()

    def check_user(self, data: DataUser) -> bool:

        self.hash(data)

        if not Cache.get_user(data):
            return False

        return True

    def recv_user(self, old_data: DataUser, new_data: DataUser) -> bool:

        self.hash(old_data)
        self.hash(new_data)

        if not Cache.check_key(old_data):
            return False

        Cache.recv_user(old_data, new_data)

        self.clientBD.recv_user(old_data, new_data)

        return True

    def set_user(self, data: DataUser) -> bool:

        self.hash(data)

        if Cache.check_user(data):
            return False

        _id = self.clientBD.set_user(data)

        Cache.set_user(data.ToUser())

        return True

    def delete_user(self, data: DataUser) -> bool:

        self.hash(data)

        if not Cache.check_key(data):
            return False

        Cache.delete_user(data)

        self.clientBD.delete_user(data)

        return True



