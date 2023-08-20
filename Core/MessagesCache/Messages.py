

class Message:

    def __init__(self, content: bytes, type_content: str, sender_name: str, sender_nickname: str, whom: str):
        self.content = content
        self.type_content = type_content
        self.sender_name = sender_name
        self.sender_nickname = sender_nickname
        self.whom = whom

    @staticmethod
    def FromDict(_dict: dict):
        return Message(_dict["content"]["b"], _dict["content"]["type"], _dict["user"]["name"], _dict["user"]["nickname"], _dict["whom"])
