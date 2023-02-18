from DB.Cache.Cache import Cache
from UserClass.DataUser import DataUser
from Core.MessagesCache.Messages import Message
from Core.MessagesCache.MessagesCache import MessagesCache


class Core:

    @staticmethod
    def send_message(message: Message, data: DataUser):

        if not Cache.check_key(data):
            return False

        MessagesCache.add_message(message)

        return True

    @staticmethod
    def recv_message(data: DataUser):
        if not Cache.check_key(data):
            return None

        message = MessagesCache.set_message(data)
        MessagesCache.del_message(data)

        return message

