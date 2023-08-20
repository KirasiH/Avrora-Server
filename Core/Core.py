from DB.Cache.Cache import Cache
from UserClass.DataUser import DataUser
from Core.MessagesCache.Messages import Message
from Core.MessagesCache.MessagesCache import MessagesCache

import hashlib

class Core:

    @staticmethod
    def send_message(message: Message, data: DataUser):

        Core.hash(data)

        if not Cache.check_key(data):
            return False

        MessagesCache.add_message(message)

        return True

    @staticmethod
    def recv_message(data: DataUser):

        Core.hash(data)

        if not Cache.check_key(data):
            return None

        message = MessagesCache.get_message(data)
        MessagesCache.del_message(data)

        return message

    @staticmethod
    def hash(data: DataUser):
        data.first_key = hashlib.sha256(data.first_key.encode("utf-8")).hexdigest()
        data.second_key = hashlib.sha256(data.second_key.encode("utf-8")).hexdigest()

