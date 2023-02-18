

class CheckJson:

    keys_userdata = [
        "name",
        "nickname",
        "first_key",
        "second_key"
    ]

    keys_messages = [
        "whom",
        "content",
        "user"
    ]

    keys_content = [
        "b",
        "type"
    ]

    @staticmethod
    def CheckUserData(_dict: dict):

        try:
            for key in CheckJson.keys_userdata:
                data = _dict[key]

        except:
            return False

        return True

    @staticmethod
    def CheckMessagesData(_dict: dict):

        try:
            for key in CheckJson.keys_messages:
                data = _dict[key]

            for key in CheckJson.keys_userdata:
                data = _dict["user"][key]

            for key in CheckJson.keys_content:
                data = _dict["content"][key]

        except:
            return False

        return True
