from UserClass.IUser import IUser


class User(IUser):
    @staticmethod
    def FromDict(_dict: dict):
        return User(name=_dict["name"], nickname=_dict["nickname"], first_key=_dict["first_key"], second_key=_dict["second_key"])

