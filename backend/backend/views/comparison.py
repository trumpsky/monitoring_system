import json
from flask import Blueprint, jsonify, request
from model import ClusterData, Cluster, Indicator, Node, NodeSingleData, Disk, NodeMultipleData
import helper.data_process as dp

cp = Blueprint("comparison", __name__)

