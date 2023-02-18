from typing import Dict
from UserClass.User import User
from UserClass.DataUser import DataUser


class Cache:

    __DictUser: Dict[str, User] = {}

    def __init__(self):
        self.DictUser: Dict[str, User] = {}

    @staticmethod
    def get_user(data: DataUser):

        try:
            data = Cache.__DictUser[data.nickname]

        except:
            return None

        else:
            return data

    @staticmethod
    def set_user(data: User):

        try:
            data = Cache.__DictUser[data.nickname]

        except:
            Cache.__DictUser[data.nickname] = data

        else:
            raise Exception("User exists")

    @staticmethod
    def delete_user(data: DataUser):

        Cache.__DictUser.pop(data.nickname)

    @staticmethod
    def recv_user(old_data: DataUser, new_data: DataUser):

        Cache.__DictUser[old_data.nickname] = new_data.ToUser()

    @staticmethod
    def check_key(data: DataUser) -> bool:

        if not Cache.check_user(data):
            return False

        try:
            user = Cache.__DictUser[data.nickname]
        except:
            return False

        else:
            if (user.first_key == data.first_key) and (user.second_key == data.second_key):
                return True

    @staticmethod
    def check_user(data: DataUser) -> bool:

        try:
            data = Cache.__DictUser[data.nickname]
        except:
            return False

        return True
