import json
from flask import Blueprint, jsonify, request
from model import User, ClusterData, Cluster, Indicator, Node, NodeSingleData, Disk, NodeMultipleData
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


def list_to_tree(json_data):
    my_tree = dp.MyTree()
    my_tree.insert_list_to_tree(json_data)
    return my_tree.tree


@ds.route("/getIndicatorName", strict_slashes=False, methods=["POST", "GET"])
def get_indicator_name():
    mode = request.form["mode"]
    if mode == "cluster":
        data = ClusterData.query.with_entities(ClusterData.indicator_id).all()
    elif mode == 'nodeSingle':
        data = NodeSingleData.query.with_entities(NodeSingleData.indicator_id).all()
    else:
        data = NodeMultipleData.query.with_entities(NodeMultipleData.indicator_id).all()
    data = list(set(data))
    data = list(map(lambda x: x[0], data))
    indicators = []
    for item in data:
        temp = Indicator.query.filter(Indicator.indicator_id == item).all()
        for single in temp:
            single = single.to_json()
            single["value"] = single.pop("indicator_id")
            single["label"] = single.pop("indicator_name")
            indicators.append(single)
    return jsonify(indicators=indicators)


@ds.route("/clusterName", strict_slashes=False, methods=["POST", "GET"])
def cluster_name():
    cluster = []
    data = Cluster.query.all()
    for item in data:
        item = item.to_json()
        item["value"] = item.pop("cluster_id")
        item["label"] = item.pop("cluster_name")
        cluster.append(item)
    return jsonify(cluster=cluster)


@ds.route("/getNodeIP", strict_slashes=False, methods=["POST", "GET"])
def get_node_ip():
    cluster_name = request.form["cluster_name"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x: x[0], cluster_id))
    data = Node.query.filter(Node.cluster_id == cluster_id[0]).with_entities(Node.ip).all()
    data = list(set(data))
    data = sorted(list(map(lambda x: x[0], data)))
    node_ip = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        node_ip.append(temp)
    return jsonify(node_ip=node_ip)


@ds.route("/getNodeName", strict_slashes=False, methods=["POST", "GET"])
def get_node_name():
    cluster_name = request.form["cluster_name"]
    node_ip = request.form["node_ip"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x: x[0], cluster_id))
    data = Node.query.filter(Node.cluster_id == cluster_id[0], Node.ip == node_ip).with_entities(Node.node_name).all()
    data = list(set(data))
    data = sorted(list(map(lambda x: x[0], data)))
    node_name = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        node_name.append(temp)
    return jsonify(node_name=node_name)


@ds.route("/getDiskName", strict_slashes=False, methods=["POST", "GET"])
def get_disk_name():
    cluster_name = request.form["cluster_name"]
    node_ip = request.form["node_ip"]
    node_name = request.form["node_name"]
    cluster_id = Cluster.query.filter(Cluster.cluster_name == cluster_name).with_entities(Cluster.cluster_id).all()
    cluster_id = list(map(lambda x: x[0], cluster_id))
    data = Disk.query.filter(Disk.cluster_id == cluster_id[0], Disk.ip == node_ip,
                             Disk.node_name == node_name).with_entities(Disk.disk_name).all()
    data = list(set(data))
    data = sorted(list(map(lambda x: x[0], data)))
    disk_name = []
    for item in data:
        temp = dict()
        temp["value"] = item
        temp["label"] = item
        disk_name.append(temp)
    return jsonify(disk_name=disk_name)


def get_cluster_id(name):
    if name == "cc-cc408-hya":
        return 1
    else:
        return 2


def get_node_id(node_ip, node_name, cluster_id):
    result = Node.query.filter(Node.cluster_id == cluster_id,
                               Node.node_ip == node_ip,
                               Node.node_name == node_name).first()
    return result.node_id


def get_indicator_id(name):
    result = Indicator.query.filter(Indicator.indicator_name == name).first()
    return result.indicator_id


def get_disk_id(cluster_id, node_ip, node_name, disk_name):
    result = Disk.query.filter(Disk.cluster_id == cluster_id,
                               Disk.node_ip == node_ip,
                               Disk.node_name == node_name,
                               Disk.disk_name == disk_name).first()
    return result.disk_id


@ds.route("/getClusterData", strict_slashes=False, methods=["POST", "GET"])
def get_cluster_data():
    if request.method == "GET":
        end_time = "2023/04/12 22:35"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        request_number = 10
        cluster_ids = [1, 2]

        indicator_ids = [1, 2]

        result = ClusterData.query.filter(ClusterData.time > start_time,
                                          ClusterData.time < end_time,
                                          ClusterData.cluster_id.in_(cluster_ids),
                                          ClusterData.indicator_id.in_(indicator_ids)).order_by(ClusterData.cluster_id,
                                                                                                ClusterData.indicator_id,
                                                                                                ClusterData.time).all()
        result_number = ClusterData.query.filter(ClusterData.time > start_time,
                                                 ClusterData.time < end_time,
                                                 ClusterData.cluster_id.in_(cluster_ids),
                                                 ClusterData.indicator_id.in_(indicator_ids)).count()

        result = dp.limit_data(result, result_number, limit_number=request_number)

        result_list = []
        for item in result:
            result_list.append(item.to_json())
        return jsonify(result_list=result_list)

    if request.method == "POST":
        # start_time = request.form["start_time"]
        # end_time = request.form["end_time"]
        end_time = "2023/04/12 17:35"
        start_time = "2023/04/01 00:00"
        end_time = dp.datetime_to_timestamp(end_time)
        start_time = dp.datetime_to_timestamp(start_time)
        info = request.form["data"]
        request_number = 2
        list_data = json.loads(info)
        tree_data = list_to_tree(list_data)
        result = []

        for cluster_name, indicator_dict in tree_data.items():
            cluster_id = get_cluster_id(cluster_name)
            indicator_ids = []
            for indicator_name in indicator_dict.keys():
                indicator_ids.append(get_indicator_id(indicator_name))
            result_item = (ClusterData.query.filter(ClusterData.time > start_time,
                                                    ClusterData.time < end_time,
                                                    ClusterData.cluster_id == cluster_id,
                                                    ClusterData.indicator_id.in_(indicator_ids)).order_by(
                ClusterData.indicator_id,
                ClusterData.time).all())
            result_number = ClusterData.query.filter(ClusterData.time > start_time,
                                                    ClusterData.time < end_time,
                                                    ClusterData.cluster_id == cluster_id,
                                                    ClusterData.indicator_id.in_(indicator_ids)).count()
            result_item = dp.limit_data(result_item, result_number, limit_number=request_number*len(indicator_ids))
            result.extend(result_item)
        result_list = []
        for item in result:
            result_list.append(item.to_json())
        print(result_list)

        return jsonify(result_list=result_list)




def single_result_process(result):
    result_list = []
    node_dict_id = -1
    indicator_id = -1
    node_dict = {}
    point_dict = {}
    point_list = []
    for i in range(len(result)):
        if i == 0:
            node_dict_id = result[i].node_id
            indicator_id = result[i].indicator_id

        if node_dict_id != result[i].node_id:
            node_dict[node_dict_id] = point_list
            node_dict_id = result[i].node_id
            point_list = []

        if indicator_id != result[i].indicator_id:
            result_list.append(node_dict)
            indicator_id = result[i].indicator_id
            node_dict = {}

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value
        point_list.append(point_dict)
        point_dict = {}

        if i == len(result) - 1:
            node_dict[node_dict_id] = point_list
            result_list.append(node_dict)

    return result_list


@ds.route("/getNodeSingleData", strict_slashes=False, methods=["POST", "GET"])
def get_node_single_data():
    if request.method == "GET":
        # start_time = request.form["start_time"]
        # end_time = request.form["end_time"]
        end_time = "2023/04/12 17:35"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        node_ids = [1, 2, 3, 4, 5]
        indicator_ids = [5, 6]
        request_number = 20

    if request.method == "POST":
        pass

    result = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                         NodeSingleData.time < end_time,
                                         NodeSingleData.node_id).order_by(NodeSingleData.indicator_id,
                                                                          NodeSingleData.node_id,
                                                                          NodeSingleData.time).all()
    result_number = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                                NodeSingleData.time < end_time,
                                                NodeSingleData.node_id).count()
    result = dp.limit_data(result, result_number, limit_number=request_number)

    result_list = single_result_process(result)

    return jsonify(result_list)


def multiple_result_process(result):
    result_list = []
    disk_dict_id = -1
    indicator_id = -1
    disk_dict = {}
    point_dict = {}
    point_list = []
    for i in range(len(result)):
        if i == 0:
            disk_dict_id = result[i].disk_id
            indicator_id = result[i].indicator_id

        if (disk_dict_id != result[i].disk_id):
            disk_dict[disk_dict_id] = point_list
            disk_dict_id = result[i].disk_id
            point_list = []

        if (indicator_id != result[i].indicator_id):
            result_list.append(disk_dict)
            indicator_id = result[i].indicator_id
            disk_dict = {}

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value
        point_list.append(point_dict)
        point_dict = {}

        if i == len(result) - 1:
            disk_dict[disk_dict_id] = point_list
            result_list.append(disk_dict)

    return result_list


@ds.route("/getNodeMultipleData", strict_slashes=False, methods=["POST", "GET"])
def get_node_multiple_data():
    if request.method == "GET":
        # start_time = request.form["start_time"]
        # end_time = request.form["end_time"]
        end_time = "2023/04/12 17:35"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        disk_ids = [1, 2, 3, 4, 5, 6]
        indicator_ids = [10]
        request_number = 15

    if request.method == "POST":
        pass

    result = NodeMultipleData.query.filter(NodeMultipleData.time > start_time,
                                           NodeMultipleData.time < end_time,
                                           NodeMultipleData.indicator_id.in_(indicator_ids),
                                           NodeMultipleData.disk_id.in_(disk_ids)).order_by(
        NodeMultipleData.disk_id,
        NodeMultipleData.time).all()
    result_number = NodeMultipleData.query.filter(NodeMultipleData.time > start_time,
                                                  NodeMultipleData.time < end_time,
                                                  NodeMultipleData.indicator_id.in_(indicator_ids),
                                                  NodeMultipleData.disk_id.in_(disk_ids)).count()
    result = dp.limit_data(result, result_number, limit_number=request_number)
    result_list = multiple_result_process(result)

    return jsonify(result_list)


def to_json(self):
    """将实例对象转化为json"""
    item = self.__dict__
    if "_sa_instance_state" in item:
        del item["_sa_instance_state"]
    return item
