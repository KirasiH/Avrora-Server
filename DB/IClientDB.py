from abc import ABC, abstractmethod
from bson.objectid import ObjectId
from UserClass.DataUser import DataUser


class IClientBD(ABC):

    @abstractmethod
    def check_user(self, data: DataUser) -> bool:
        pass

    @abstractmethod
    def recv_user(self, old_data: DataUser, new_data: DataUser) -> bool:
        pass

    @abstractmethod
    def set_user(self, data: DataUser) -> ObjectId:
        pass

    @abstractmethod
    def delete_user(self, data: DataUser) -> bool:
        pass

