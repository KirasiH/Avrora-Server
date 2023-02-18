from flask import Flask, jsonify, request
from DB.proxyDB.ProxyDB import ClientDBProxy
from UserClass.DataUser import DataUser
from Core.Core import Core
from Core.MessagesCache.Messages import Message

from CheckJson.CheckJson import CheckJson


clientDB = ClientDBProxy()


app = Flask(__name__)


def create_user():

    _dict = request.json

    if not CheckJson.CheckUserData(_dict):
        return "Error data"

    if not clientDB.set_user(DataUser.FromDict(_dict)):
        return "Error data user"

    return "create"


def delete_user():

    _dict = request.json

    if not CheckJson.CheckUserData(_dict):
        return "Error data"

    if not clientDB.delete_user(DataUser.FromDict(_dict)):
        return "Error delete"

    return "delete"


def recv_user():

    _dict = request.json

    _dict_old_data = _dict["old_user"]
    _dict_new_data = _dict["new_user"]

    if not CheckJson.CheckUserData(_dict_old_data) or not CheckJson.CheckUserData(_dict_new_data):
        return "Error data"

    if not clientDB.recv_user(DataUser.FromDict(_dict_old_data), DataUser.FromDict(_dict_new_data)):
        return "Error recv"

    return "recreate"


def send_message():

    _dict = request.json

    if not Core.send_message(Message.FromDict(_dict), DataUser.FromDict(_dict["user"])):
        return "Error Message"

    return "Send"


def recv_message():

    _dict = request.json

    if not CheckJson.CheckUserData(_dict):
        return "Error data"

    message = Core.recv_message(DataUser.FromDict(_dict))

    if not message:
        return "Error"

    return jsonify(json={"Sender name": message.sender_name,
                         "Sender nickname": message.sender_nickname,
                         "Whom": message.whom,
                         "Content": message.content})


def main():

    app.add_url_rule("/create", methods=["POST"], view_func=create_user)
    app.add_url_rule("/delete", methods=["DELETE"], view_func=delete_user)
    app.add_url_rule("/recreate", methods=["PUT"], view_func=recv_user)
    app.add_url_rule("/send", methods=["POST"], view_func=send_message)
    app.add_url_rule("/recv", methods=["GET"], view_func=recv_message)

    app.run(debug=True, use_reloader=False)


if __name__ == "__main__":
    main()
