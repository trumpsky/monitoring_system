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


def find_muldule_or_package():
    for path in sys.path:
        print(path)

# if __name__ == '__main__':
#     input = [['cc-cc408-hya'], ['cc-cc408-hya', 'elasticsearch_cluster_health_active_shards'], ['cc-cc408-hya', 'elasticsearch_cluster_health_number_of_nodes'], ['cc-cc408-hya', 'elasticsearch_cluster_health_status']]
#     tree.insert_list_to_tree(input)
#     print(tree.tree)
