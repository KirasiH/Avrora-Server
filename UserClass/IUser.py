from abc import ABC, abstractmethod
from bson import ObjectId


class IUser(ABC):

    def __init__(self, name: str, nickname: str, first_key: str, second_key: str, _id: ObjectId = None):
        self._id = _id
        self.name = name
        self.nickname = nickname
        self.first_key = first_key
        self.second_key = second_key

    @staticmethod
    @abstractmethod
    def FromDict(_dict: dict):
        pass


