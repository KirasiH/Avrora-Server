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
    def get_message(data: DataUser):

        try:
            messages = MessagesCache.__DictMessages[data.nickname]
            message = messages.pop(0)
        except:
            return None

        return message

    @staticmethod
    def del_message(data: DataUser):

        try:
            MessagesCache.__DictMessages[data.nickname].pop()

        except:
            pass
