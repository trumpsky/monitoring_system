import time
import datetime
import sys


def datetime_to_timestamp(dt):
    dt = time.strptime(dt, "%Y/%m/%d %H:%M")
    return int(time.mktime(dt))


def timestamp_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts)


def limit_data(data, data_number, limit_number=15):
    if data_number <= limit_number:
        return data
    return data[0::int(data_number / limit_number)]


# 把一个 路径集合 变成一个 树状字典
# list 转 dict
class MyTree:
    def __init__(self):
        self.tree = {}

    # onepoint 是 list
    def append_Point_to_tree(self, onepoint):
        nowPositon = self.tree
        index = 0
        while index < len(onepoint):

            if nowPositon.__contains__(onepoint[index]):
                nowPositon = nowPositon[onepoint[index]]
                index += 1

            else:
                # 创建新节点
                nowPositon[onepoint[index]] = {}
        return self.tree

    # 把【 【路径1 a,b,c,d】 ，【路径2】 】
    # 多条路径一次性插入到树中
    def insert_list_to_tree(self, pointlist):
        for onepoint in pointlist:
            self.append_Point_to_tree(onepoint)

def list_to_tree(json_data):
    my_tree = MyTree()
    my_tree.insert_list_to_tree(json_data)
    return my_tree.tree

def find_muldule_or_package():
    for path in sys.path:
        print(path)

if __name__ == '__main__':
    tree = MyTree()
    input = [['cc-cc408-hya'], ['cc-cc408-hya', 'elasticsearch_cluster_health_active_shards'], ['cc-cc408-hya', 'elasticsearch_cluster_health_number_of_nodes'], ['cc-cc408-hya', 'elasticsearch_cluster_health_status']]
    tree.insert_list_to_tree(input)
    print(tree.tree)
# {'cc-cc408-hya': {'elasticsearch_os_load5': {'9.9.2.153': {'data-node-01': {}, 'data-node-06': {}}, '9.9.2.154': {'data-node-12': {}}}, 'elasticsearch_transport_rx_size_bytes_total': {
# '9.9.2.153': {'data-node-01': {}}}}} !!!!!!!!!!!!!!!!

# {'cc-cc408-hya': {'elasticsearch_filesystem_data_available_bytes': {'9.9.2.153': {'data-node-01': {'/srv/data01 (/dev/sdb)': {}, '/srv/data02 (/dev/sdc)': {}}, 'data-node-06': {'/srv/d
# ata05 (/dev/sdf)': {}, '/srv/data06 (/dev/sdg)': {}}}, '9.9.2.154': {'data-node-02': {'/srv/data01 (/dev/sdb)': {}}}}}}


