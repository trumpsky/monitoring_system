from flask import Blueprint, jsonify, request
from model import User
import json

ds = Blueprint("data_show", __name__)


@ds.route("/login/", strict_slashes=False, methods=["POST", "GET"])
def login():
    user_list = []
    users = User.query.all()
    for user in users:
        user_list.append(user.to_json())

    return jsonify(user_list=user_list)


@ds.route("/index", strict_slashes=False, methods=["POST", "GET"])
def index():
    get_data = request.form["test"]
    json_data = json.loads(get_data)
    print(json_data)

    print(type(get_data))
    print(json_data[0].get("value"))
    return jsonify(json_data)
