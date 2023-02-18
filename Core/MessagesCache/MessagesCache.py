from typing import Dict, List
from Core.MessagesCache.Messages import Message
from UserClass.DataUser import DataUser


class MessagesCache:

    __DictMessages: Dict[str, List[Message]] = {}

    @staticmethod
    def add_message(message: Message):

        try:
            data = MessagesCache.__DictMessages[message.whom]

        except:
            MessagesCache.__DictMessages[message.whom] = [message]
            return

        MessagesCache.__DictMessages[message.whom].append(message)

    @staticmethod
    def set_message(data: DataUser):

        try:
            data = MessagesCache.__DictMessages[data.nickname]

        except:
            return None

        return data.pop(0)

    @staticmethod
    def del_message(data: DataUser):

        try:
            MessagesCache.__DictMessages[data.nickname].pop()

        except:
            pass
