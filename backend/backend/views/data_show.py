import json
from flask import Blueprint, jsonify, request
from model import User, ClusterData, Cluster, Indicator,Node,NodeSingleData,Disk,NodeMultipleData
import json
import helper.data_process as dp
from sqlalchemy import distinct

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
def get_cluster_data():
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

    result = ClusterData.query.filter(ClusterData.time > start_time,
                                      ClusterData.time < end_time,
                                      ClusterData.cluster_id.in_(cluster_ids),
                                      ClusterData.indicator_id.in_(indicator_ids)).order_by(ClusterData.cluster_id, ClusterData.indicator_id, ClusterData.time).all()
    result_list = []
    for item in result:
        result_list.append(item.to_json())
    return jsonify(result_list=result_list)


@ds.route("/NodeSingleData", strict_slashes=False, methods=["POST", "GET"])
def get_node_id(node_ip, node_name, cluster_id):
    result = Node.query.filter(Node.cluster_id == cluster_id,
                               Node.node_ip == node_ip,
                               Node.node_name == node_name).first()
    return result.node_id


def get_node_single_data():
    # start_time = request.form["start_time"]
    # end_time = request.form["end_time"]
    end_time = "2023/04/12 17:35"
    start_time = "2023/04/01 00:00"
    start_time = dp.datetime_to_timestamp(start_time)
    end_time = dp.datetime_to_timestamp(end_time)
    cluster_ids = request.form["cluster_ids"]

    result = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                         NodeSingleData.time < end_time,
                                         NodeSingleData.node_id).order_by(NodeSingleData.indicator_id, NodeSingleData.node_id, NodeSingleData.time).all()

    result_list = []
    node_dict_id = 0
    indicator_id = 0
    node_dict = {}
    point_dict = {}
    for i in range(len(result)):

        if (node_dict_id != result[i].node_id) and (node_dict_id != 0):
            node_dict[node_dict_id] = point_dict
            node_dict_id = result[i].node_id
            point_dict = {}

        if (indicator_id != result[i].indicator_id) and (indicator_id != 0):
            result_list.append(node_dict.to_json())
            indicator_id = result[i].indicator_id
            node_dict = {}

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value

        if i == len(result)-1:
            result_list.append(node_dict.to_json())

    return jsonify(result_list)


@ds.route("/NodeMultipleData", strict_slashes=False, methods=["POST", "GET"])
def get_disk_id(cluster_id, node_ip, node_name, disk_name):
    result = Disk.query.filter(Disk.cluster_id == cluster_id,
                               Disk.node_ip == node_ip,
                               Disk.node_name == node_name,
                               Disk.disk_name == disk_name).first()
    return result.disk_id


def get_node_multiple_data():

    result = NodeMultipleData.query.filter(NodeMultipleData.time > start_time,
                                           NodeMultipleData.time < end_time,
                                           NodeMultipleData.disk_id).order_by(NodeMultipleData.indicator_id, NodeMultipleData.disk_id, NodeMultipleData.time).all()

    result_list = []
    disk_dict_id = 0
    indicator_id = 0
    disk_dict = {}
    point_dict = {}
    for i in range(len(result)):

        if (disk_dict_id != result[i].disk_id) and (disk_dict_id != 0):
            disk_dict[disk_dict_id] = point_dict
            disk_dict_id = result[i].disk_id
            point_dict = {}

        if (indicator_id != result[i].indicator_id) and (indicator_id != 0):
            result_list.append(disk_dict.to_json())
            indicator_id = result[i].indicator_id
            disk_dict = {}

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value

        if i == len(result)-1:
            result_list.append(disk_dict.to_json())

    return jsonify(result_list)



def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item


@ds.route("/getIndicatorName", strict_slashes=False,methods=["POST", "GET"])
def get_indicator_name():
    mode = request.form["mode"]
    if mode == "cluster":
        data = ClusterData.query.with_entities(ClusterData.indicator_id).all()
    elif mode == 'nodeSingle':
        data = NodeSingleData.query.with_entities(NodeSingleData.indicator_id).all()
    else:
        data = NodeMultipleData.query.with_entities(NodeMultipleData.indicator_id).all()
    data = list(set(data))
    data = list(map(lambda x : x[0],data))
    indicators = []
    for item in data:
        temp = Indicator.query.filter(Indicator.indicator_id == item).all()
        for single in temp:
            single = single.to_json()
            single["value"] = single.pop("indicator_id")
            single["label"] = single.pop("indicator_name")
            indicators.append(single)
    return jsonify(indicators = indicators)

@ds.route("/clusterName", strict_slashes=False,methods=["POST", "GET"])
def cluster_name():
    cluster = []
    data = Cluster.query.all()
    for item in data:
        item = item.to_json()
        item["value"] = item.pop("cluster_id")
        item["label"] = item.pop("cluster_name")
        cluster.append(item)
    return jsonify(cluster=cluster)

@ds.route("/getNodeIP", strict_slashes=False,methods=["POST", "GET"])
def get_node_ip():
    cluster_name = request.form["cluster_name"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x : x[0],cluster_id))
    data = Node.query.filter(Node.cluster_id == cluster_id[0]).with_entities(Node.ip).all()
    data = list(set(data))
    data = sorted(list(map(lambda x : x[0],data)))
    node_ip = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        node_ip.append(temp)
    return jsonify(node_ip=node_ip)

@ds.route("/getNodeName", strict_slashes=False,methods=["POST", "GET"])
def get_node_name():
    cluster_name = request.form["cluster_name"]
    node_ip = request.form["node_ip"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x : x[0],cluster_id))
    data = Node.query.filter(Node.cluster_id == cluster_id[0],Node.ip == node_ip).with_entities(Node.node_name).all()
    data = list(set(data))
    data = sorted(list(map(lambda x : x[0],data)))
    node_name = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        node_name.append(temp)
    return jsonify(node_name=node_name)

@ds.route("/getDiskName", strict_slashes=False,methods=["POST", "GET"])
def get_disk_name():
    cluster_name = request.form["cluster_name"]
    node_ip = request.form["node_ip"]
    node_name = request.form["node_name"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x : x[0],cluster_id))
    data = Disk.query.filter(Disk.cluster_id == cluster_id[0],Disk.ip == node_ip,Disk.node_name == node_name).with_entities(Disk.disk_name).all()
    data = list(set(data))
    data = sorted(list(map(lambda x : x[0],data)))
    disk_name = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        disk_name.append(temp)
    return jsonify(disk_name=disk_name)
