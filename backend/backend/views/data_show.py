from flask import Blueprint, jsonify, request
from model import User, ClusterData, Cluster, Indicator,Node,NodeSingleData,Disk,NodeMultipleData
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
                                      ClusterData.indicator_id.in_(indicator_ids)).order_by(ClusterData.cluster_id,ClusterData.indicator_id,ClusterData.time).all()
    result_list = []
    for item in result:
        result_list.append(item.to_json())
    return jsonify(result_list=result_list)



@ds.route("/NodeSingleData", strict_slashes=False, methods=["POST", "GET"])
def getNodeId():
    cluster_id=request.form["cluster_id"]
    node_ip=request.form["node_ip"]
    node_name=request.form["node_name"]
    result=Node.query.filter(Node.cluster_id==cluster_id,Node.node_ip==node_ip,Node.node_name==node_name).first()
    return result.node_id

def getNodeSingleData():
    # start_time = request.form["start_time"]
    # end_time = request.form["end_time"]
    end_time = "2023/04/12 17:35"
    start_time = "2023/04/01 00:00"
    start_time = dp.datetime_to_timestamp(start_time)
    end_time = dp.datetime_to_timestamp(end_time)
    cluster_ids=request.form["cluster_ids"]
    result=NodeSingleData.query.filter(NodeSingleData.time>start_time,
                                       NodeSingleData.time<end_time,
                                       NodeSingleData.node_id).order_by(NodeSingleData.indicator_id,NodeSingleData.node_id,NodeSingleData.time).all()
    
   
    result_list=[]
    node_dict_id=0
    indicator_id=0
    node_dict={}
    point_dict={}
    for item in result:

        if (node_dict_id != item.node_id)and(node_dict_id!=0):
            node_dict[node_dict_id]=point_dict
            node_dict_id=item.node_id
            point_dict={}

        if (indicator_id != item.indicator_id) and (indicator_id != 0):
            result_list.append(node_dict.to_json())
            indicator_id=item.indicator_id
            node_dict={}

        #点的字典
        point_dict["time"]=item.time
        point_dict["value"]=item.value


    return jsonify(result_list)


