from flask import Blueprint, jsonify
from model import User

ds = Blueprint("data_show", __name__)

@ds.route("/login", strict_slashes=False)
def login():
    user_list = []
    users = User.query.all()
    for user in users:
        user_list.append(user.to_json())
    
    return jsonify(user_list=user_list)

@ds.route("/index", strict_slashes=False)
def index():
    return "index"