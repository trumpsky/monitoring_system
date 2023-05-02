from flask import Blueprint, jsonify, request
from model import ClusterData, Cluster, Indicator, Node, NodeSingleData, Disk, NodeMultipleData

fg = Blueprint("frontend_get", __name__)

@fg.route("/getIndicatorName", strict_slashes=False, methods=["POST", "GET"])
def get_indicator_name():
    mode = request.form["mode"]
    if mode == "cluster":
        data = ClusterData.query.with_entities(ClusterData.indicator_id).all()
    elif mode == 'nodeSingle':
        data = NodeSingleData.query.with_entities(NodeSingleData.indicator_id).all()
    else:
        data = NodeMultipleData.query.with_entities(NodeMultipleData.indicator_id).all()
    data = list(set(data))
    data = sorted(list(map(lambda x: x[0], data)))
    indicators = []
    for item in data:
        temp = Indicator.query.filter(Indicator.indicator_id == item).all()
        for single in temp:
            single = single.to_json()
            single["value"] = single.pop("indicator_id")
            single["label"] = single.pop("indicator_name")
            indicators.append(single)
    return jsonify(indicators=indicators)


@fg.route("/clusterName", strict_slashes=False, methods=["POST", "GET"])
def cluster_name():
    cluster = []
    data = Cluster.query.all()
    for item in data:
        item = item.to_json()
        item["value"] = item.pop("cluster_id")
        item["label"] = item.pop("cluster_name")
        cluster.append(item)
    return jsonify(cluster=cluster)


@fg.route("/getNodeIP", strict_slashes=False, methods=["POST", "GET"])
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


@fg.route("/getNodeName", strict_slashes=False, methods=["POST", "GET"])
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


@fg.route("/getDiskName", strict_slashes=False, methods=["POST", "GET"])
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