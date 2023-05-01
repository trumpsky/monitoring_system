from flask import Blueprint, jsonify, request
from model import User, ClusterData, Cluster, Indicator
import json
import helper.data_process as dp

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


@ds.route("/getClusterData", strict_slashes=False, methods=["POST", "GET"])
def getClusterData():
    # start_time = request.form["start_time"]
    # end_time = request.form["end_time"]
    end_time = "2023/04/12 17:35"
    start_time = "2023/04/01 00:00"
    start_time = dp.datetime_to_timestamp(start_time)
    end_time = dp.datetime_to_timestamp(end_time)
    request_number = 100
    cluster_ids = [1, 2]
    # indicator_ids = request.form["indicator_ids"]
    indicator_ids = [1, 2]

    result = ClusterData.query.filter(ClusterData.time>start_time, 
                                      ClusterData.time<end_time, 
                                      ClusterData.cluster_id.in_(cluster_ids), 
                                      ClusterData.indicator_id.in_(indicator_ids)).order_by(ClusterData.cluster_id,ClusterData.indicator_id,ClusterData.time).limit(request_number).all()
    result_list = []
    for item in result:
        result_list.append(item.to_json())
    return jsonify(result_list=result_list)
