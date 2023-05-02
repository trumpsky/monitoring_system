import json
from flask import Blueprint, jsonify, request
from model import ClusterData, Cluster, Indicator, Node, NodeSingleData, Disk, NodeMultipleData
import helper.data_process as dp

ds = Blueprint("data_show", __name__)


def node_id_to_name_ip(node_id):
    node = Node.query.filter(Node.node_id == node_id).first()
    cluster_name = cluster_id_to_name(node.cluster_id)
    node_information = cluster_name + "-" + node.ip + "-" + node.node_name
    return node_information


def disk_id_to_nodename_ip_diskname(disk_id):
    disk = Disk.query.filter(Disk.disk_id == disk_id).first()
    cluster_name = cluster_id_to_name(disk.cluster_id)
    disk_information = cluster_name + "-" + disk.ip + "-" + disk.node_name + "-" + disk.disk_name
    return disk_information


def get_cluster_id(name):
    if name == "cc-cc408-hya":
        return 1
    else:
        return 2


def cluster_id_to_name(cluster_id):
    if cluster_id == 1:
        return "cc-cc408-hya"
    else:
        return "cc-cc553-interestPrice"


def get_node_id(node_ip, node_name, cluster_id):
    result = Node.query.filter(Node.cluster_id == cluster_id,
                               Node.ip == node_ip,
                               Node.node_name == node_name).first()
    return result.node_id


def get_indicator_id(name):
    result = Indicator.query.filter(Indicator.indicator_name == name).first()
    return result.indicator_id


def indicator_id_to_name(indicator_id):
    result = Indicator.query.filter(Indicator.indicator_id == indicator_id).first()
    return result.indicator_name


def get_disk_id(cluster_id, node_ip, node_name, disk_name):
    result = Disk.query.filter(Disk.cluster_id == cluster_id,
                               Disk.ip == node_ip,
                               Disk.node_name == node_name,
                               Disk.disk_name == disk_name).first()
    return result.disk_id


def load_request():
    start_time = request.form["start_time"]
    end_time = request.form["end_time"]
    end_time = dp.datetime_to_timestamp(end_time)
    start_time = dp.datetime_to_timestamp(start_time)
    info = request.form["data"]
    list_data = json.loads(info)
    tree_data = dp.list_to_tree(list_data)
    return start_time, end_time, tree_data


def cluster_data_process(result):
    result_list = []
    cluster_id = -1
    indicator_id = -1
    indicator_dict = {}
    point_dict = {}
    point_list = []
    for i in range(len(result)):
        if i == 0:
            cluster_id = result[i]['cluster_id']
            indicator_id = result[i]['indicator_id']
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)
            # cluster_name = cluster_id_to_name(cluster_id)
            # indicator_dict[cluster_name] = point_list

        # #只变indicator
        if indicator_id != result[i]['indicator_id'] and cluster_id == result[i]['cluster_id']:
            # 1.把集群：【point_list】加到indicator_dict
            indicator_dict[cluster_id_to_name(cluster_id)] = point_list
            # 2.把indicator_dict append到result_list
            result_list.append(indicator_dict)
            # 3.更新列表、字典，cluster id，indicator id
            point_list = []
            indicator_id = result[i]['indicator_id']
            indicator_dict = {}
            cluster_id = result[i]['cluster_id']
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 只变cluster
        if cluster_id != result[i]['cluster_id'] and indicator_id == result[i]['indicator_id']:
            indicator_dict[cluster_id_to_name(cluster_id)] = point_list
            # indicator_dict["cc-cc408-hya"] = point_list
            cluster_id = result[i]['cluster_id']
            point_list = []
        # 都变
        if cluster_id != result[i]['cluster_id'] and indicator_id != result[i]['indicator_id']:
            # 1.把集群：【point_list】加到indicator_dict
            indicator_dict[cluster_id_to_name(cluster_id)] = point_list
            # 2.把indicator_dict append到result_list
            result_list.append(indicator_dict)
            # 3.更新列表、字典，cluster id，indicator id
            point_list = []
            indicator_dict = {}
            cluster_id = result[i]['cluster_id']
            indicator_id = result[i]['indicator_id']
            # 4.把新的indicator_dict里面增加第一行

            # indicator：xxx
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 点的字典
        point_dict["time"] = result[i]['time']
        point_dict["value"] = result[i]['value']
        point_list.append(point_dict)
        point_dict = {}

        if i == len(result) - 1:
            indicator_dict[cluster_id_to_name(cluster_id)] = point_list
            result_list.append(indicator_dict)

    return result_list


@ds.route("/getClusterData", strict_slashes=False, methods=["POST", "GET"])
def get_cluster_data():
    if request.method == "GET":
        end_time = "2023/04/12 17:33"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        request_number = 100
        cluster_ids = [1]

        indicator_ids = [1, 2, 3]

        result = ClusterData.query.filter(ClusterData.time > start_time,
                                          ClusterData.time < end_time,
                                          ClusterData.cluster_id.in_(cluster_ids),
                                          ClusterData.indicator_id.in_(indicator_ids)).order_by(
            ClusterData.indicator_id,
            ClusterData.cluster_id,
            ClusterData.time).all()
        result_number = ClusterData.query.filter(ClusterData.time > start_time,
                                                 ClusterData.time < end_time,
                                                 ClusterData.cluster_id.in_(cluster_ids),
                                                 ClusterData.indicator_id.in_(indicator_ids)).count()

        result = dp.limit_data(result, result_number, limit_number=result_number)

        result_list = []
        for item in result:
            result_list.append(item.to_json())
        result_list = cluster_data_process(result)

    if request.method == "POST":
        request_number = 150
        start_time, end_time, tree_data = load_request()
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
            result_item = dp.limit_data(result_item, result_number, limit_number=request_number * len(indicator_ids))
            result.extend(result_item)
        result_list = []
        for item in result:
            result_list.append(item.to_json())
        result_list = cluster_data_process(result_list)

    return jsonify(result_list=result_list)


def single_result_process(result):
    result_list = []
    node_id = -1
    indicator_id = -1
    indicator_dict = {}
    point_dict = {}
    point_list = []
    for i in range(len(result)):
        if i == 0:
            node_id = result[i].node_id
            indicator_id = result[i].indicator_id
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 变indicator
        if node_id != result[i].node_id and indicator_id != result[i].indicator_id:
            # 1.把集群：【point_list】加到indicator_dict
            indicator_dict[node_id_to_name_ip(node_id)] = point_list
            # 2.把indicator_dict append到result_list
            result_list.append(indicator_dict)
            # 3.更新列表、字典，cluster id，indicator id
            point_list = []
            indicator_dict = {}
            node_id = result[i].node_id
            indicator_id = result[i].indicator_id
            # 4.把新的indicator_dict里面增加第一行
            # indicator：xxx
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)
            node_id = result[i].node_id
            indicator_id = result[i].indicator_id
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 只变cluster
        if node_id != result[i].node_id and indicator_id == result[i].indicator_id:
            indicator_dict[node_id_to_name_ip(node_id)] = point_list
            # indicator_dict["cc-cc408-hya"] = point_list
            node_id = result[i].node_id
            point_list = []

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value
        point_list.append(point_dict)
        point_dict = {}

        if i == len(result) - 1:
            indicator_dict[node_id_to_name_ip(node_id)] = point_list
            result_list.append(indicator_dict)

    return result_list


@ds.route("/getNodeSingleData", strict_slashes=False, methods=["POST", "GET"])
def get_node_single_data():
    if request.method == "GET":
        end_time = "2023/04/12 17:35"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        node_ids = [1, 2, 3, 4, 5]
        indicator_ids = [5, 6]
        request_number = 20

        result = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                             NodeSingleData.time < end_time,
                                             NodeSingleData.node_id).order_by(NodeSingleData.indicator_id,
                                                                              NodeSingleData.node_id,
                                                                              NodeSingleData.time).all()
        result_number = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                                    NodeSingleData.time < end_time,
                                                    NodeSingleData.node_id).count()
        result = dp.limit_data(result, result_number, limit_number=request_number)

    if request.method == "POST":
        request_number = 40
        start_time, end_time, tree_data = load_request()
        result = []

        for cluster_name, indicator_dict in tree_data.items():
            cluster_id = get_cluster_id(cluster_name)
            for indicator_name, ip_dict in indicator_dict.items():
                indicator_id = get_indicator_id(indicator_name)
                for ip, node_dict in ip_dict.items():
                    node_ids = []
                    for node_name in node_dict.keys():
                        node_ids.append(get_node_id(ip, node_name, cluster_id))
                    result_item = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                                              NodeSingleData.time < end_time,
                                                              NodeSingleData.indicator_id == indicator_id,
                                                              NodeSingleData.node_id.in_(node_ids)).order_by(
                        NodeSingleData.indicator_id,
                        NodeSingleData.node_id,
                        NodeSingleData.time).all()
                    result_number = NodeSingleData.query.filter(NodeSingleData.time > start_time,
                                                                NodeSingleData.time < end_time,
                                                                NodeSingleData.indicator_id == indicator_id,
                                                                NodeSingleData.node_id.in_(node_ids)).count()
                    result_item = dp.limit_data(result_item, result_number,
                                                limit_number=request_number * len(node_ids))
                    result.extend(result_item)

    result_list = single_result_process(result)
    # result_list = []
    # for item in result:
    #     result_list.append(item.to_json())
    # print(result_list)
    return jsonify(result_list=result_list)


def multiple_result_process(result):
    result_list = []
    disk_id = -1
    indicator_id = -1
    indicator_dict = {}
    point_dict = {}
    point_list = []
    for i in range(len(result)):
        if i == 0:
            disk_id = result[i].disk_id
            indicator_id = result[i].indicator_id
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 变indicator
        if disk_id != result[i].disk_id and indicator_id != result[i].indicator_id:
            # 1.把集群：【point_list】加到indicator_dict
            indicator_dict[disk_id_to_nodename_ip_diskname(disk_id)] = point_list
            # 2.把indicator_dict append到result_list
            result_list.append(indicator_dict)
            # 3.更新列表、字典，cluster id，indicator id
            point_list = []
            indicator_dict = {}
            disk_id = result[i].disk_id
            indicator_id = result[i].indicator_id
            # 4.把新的indicator_dict里面增加第一行
            # indicator：xxx
            indicator_dict["indicator"] = indicator_id_to_name(indicator_id)

        # 只变cluster
        if disk_id != result[i].disk_id and indicator_id == result[i].indicator_id:
            indicator_dict[disk_id_to_nodename_ip_diskname(disk_id)] = point_list
            # indicator_dict["cc-cc408-hya"] = point_list
            disk_id = result[i].disk_id
            point_list = []

        # 点的字典
        point_dict["time"] = result[i].time
        point_dict["value"] = result[i].value
        point_list.append(point_dict)
        point_dict = {}

        if i == len(result) - 1:
            indicator_dict[disk_id_to_nodename_ip_diskname(disk_id)] = point_list
            result_list.append(indicator_dict)

    return result_list


@ds.route("/getNodeMultipleData", strict_slashes=False, methods=["POST", "GET"])
def get_node_multiple_data():
    if request.method == "GET":
        end_time = "2023/04/12 17:35"
        start_time = "2023/04/01 00:00"
        start_time = dp.datetime_to_timestamp(start_time)
        end_time = dp.datetime_to_timestamp(end_time)
        disk_ids = [1, 2, 3, 4, 5, 6]
        indicator_ids = [10]
        request_number = 15

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

    if request.method == "POST":
        request_number = 50
        start_time, end_time, tree_data = load_request()
        result = []

        for cluster_name, indicator_dict in tree_data.items():
            cluster_id = get_cluster_id(cluster_name)
            for indicator_name, ip_dict in indicator_dict.items():
                indicator_id = get_indicator_id(indicator_name)
                for ip, node_dict in ip_dict.items():
                    for node_name, disk_dict in node_dict.items():
                        disk_ids = []
                        for disk_name in disk_dict.keys():
                            disk_ids.append(get_disk_id(cluster_id, ip, node_name, disk_name))
                        result_item = NodeMultipleData.query.filter(NodeMultipleData.time > start_time,
                                                                    NodeMultipleData.time < end_time,
                                                                    NodeMultipleData.indicator_id == indicator_id,
                                                                    NodeMultipleData.disk_id.in_(disk_ids)).order_by(
                            NodeMultipleData.indicator_id,
                            NodeMultipleData.disk_id,
                            NodeMultipleData.time).all()
                        result_number = NodeMultipleData.query.filter(NodeMultipleData.time > start_time,
                                                                      NodeMultipleData.time < end_time,
                                                                      NodeMultipleData.indicator_id == indicator_id,
                                                                      NodeMultipleData.disk_id.in_(disk_ids)).count()
                        result_item = dp.limit_data(result_item, result_number,
                                                    limit_number=request_number * len(disk_ids))
                        result.extend(result_item)

    result_list = multiple_result_process(result)

    return jsonify(result_list=result_list)
