import json
from flask import Blueprint, jsonify, request
import os
import pandas as pd
import numpy as np
from tslearn.metrics import dtw_path, dtw
from shapesimilarity import shape_similarity
from scipy.spatial.distance import directed_hausdorff

cp = Blueprint("comparison", __name__)


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def standardization(data):
    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    return (data - mu) / sigma


# 定义一个函数，用于将CSV文件加载到numpy数组中
def load_csv(filename):
    data = pd.read_csv(filename, header=None).values
    data = np.delete(pd.to_numeric(data[:, 2], errors='coerce'), 0)
    data = standardization(data)
    return data


class DTW:
    def __init__(self):
        self.distances = []
        self.data = []

    @staticmethod
    def compute_dtw_distance(data_1, data_2):
        dist, path = dtw_path(data_1, data_2)
        return path

    def load_data(self):
        for index in range(21):
            self.data.append(load_csv(f"./backend/static/data/{index}.csv"))
            self.distances.append(tuple([index, self.compute_dtw_distance(self.data[0], self.data[index])]))

    def show_rank(self):
        self.distances.sort(key=lambda x: x[1])
        for i, (file_id, dist) in enumerate(self.distances):
            print(f'rank_{i + 1} file_{file_id} distance:{dist}')

    def run(self):
        self.load_data()
        self.show_rank()


class Frechet:
    def __init__(self):
        self.similarity = []
        self.data = []

    def load_data(self):
        indexs = [i for i in range(5)]
        for index in range(21):
            data_value = load_csv(f"./backend/static/data/{index}.csv")
            data_point = [list(t) for t in zip(indexs, data_value)]
            data_item = np.column_stack(data_point)
            self.data.append(data_item)
            self.similarity.append(tuple([index, shape_similarity(self.data[index], self.data[0], rotations=30, checkRotation=False)]))

    def show_rank(self):
        print("Frechet")
        self.similarity.sort(key=lambda x: x[1], reverse=True)
        for i, (file_id, similarity) in enumerate(self.similarity):
            print(f'rank_{i + 1} file_{file_id} similarity:{similarity}')

    def run(self):
        self.load_data()
        self.show_rank()


class Hausdorff:
    def __init__(self):
        self.distances = []
        self.data = []

    def load_data(self):
        indexs = [i for i in range(5)]
        for index in range(21):
            data_value = load_csv(f"./backend/static/data/{index}.csv")
            self.data.append([list(t) for t in zip(indexs, data_value)])
            distance = max(
                directed_hausdorff(self.data[index], self.data[0])[0],
                directed_hausdorff(self.data[0], self.data[index])[0]
            )
            self.distances.append(tuple([index, distance]))

    def show_rank(self):
        print("Frechet")
        self.distances.sort(key=lambda x: x[1])
        for i, (file_id, distance) in enumerate(self.distances):
            print(f'rank_{i + 1} file_{file_id} similarity:{distance}')

    def run(self):
        self.load_data()
        self.show_rank()


@cp.route("/getRank", strict_slashes=False, methods=["POST", "GET"])
def get_rank():
    pass


if __name__ == '__main__':
    # dtw = DTW()
    # dtw.run()

    # frechet = Frechet()
    # frechet.run()

    # hausdorff = Hausdorff()
    # hausdorff.run()
    pass
