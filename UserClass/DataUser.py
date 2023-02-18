from UserClass.IUser import IUser
from UserClass.User import User


class DataUser(IUser):

    def ToUser(self):
        return User(self.name, self.nickname, self.first_key, self.second_key, self._id)

    @staticmethod
    def FromUser(user: User):
        return DataUser(user.name, user.nickname, user.first_key, user.second_key, user._id)

    @staticmethod
    def FromDict(_dict: dict):
        return DataUser(name=_dict["name"], nickname=_dict["nickname"], first_key=_dict["first_key"], second_key=_dict["second_key"])
