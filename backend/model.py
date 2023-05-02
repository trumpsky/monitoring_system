from extension import db


class BaseJSON():
    def to_json(self):
        """将实例对象转化为json"""
        item = self.__dict__
        if "_sa_instance_state" in item:
            del item["_sa_instance_state"]
        return item


class Cluster(db.Model, BaseJSON):
    __tablename__ = 'cluster'
    cluster_id = db.Column(db.SmallInteger, primary_key=True)
    cluster_name = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(30), nullable=True)


class Indicator(db.Model, BaseJSON):
    __tablename__ = 'indicator'
    indicator_id = db.Column(db.SmallInteger, primary_key=True)
    indicator_name = db.Column(db.String(50), nullable=False)


class ClusterData(db.Model, BaseJSON):
    __tablename__ = 'cluster_data'
    time = db.Column(db.BigInteger, primary_key=True)
    cluster_id = db.Column(db.SmallInteger, primary_key=True)
    indicator_id = db.Column(db.SmallInteger, primary_key=True)
    value = db.Column(db.SmallInteger, nullable=False)


class Node(db.Model, BaseJSON):
    __tablename__ = 'node'
    node_id = db.Column(db.SmallInteger, primary_key=True)
    cluster_id = db.Column(db.SmallInteger, nullable=False)
    node_name = db.Column(db.String(50), nullable=False)
    ip = db.Column(db.String(30), nullable=False)


class NodeSingleData(db.Model, BaseJSON):
    __tablename__ = 'node_single_data'
    time = db.Column(db.BigInteger, primary_key=True)
    node_id = db.Column(db.SmallInteger, primary_key=True)
    indicator_id = db.Column(db.SmallInteger, primary_key=True)
    value = db.Column(db.Float, nullable=False)


class Disk(db.Model, BaseJSON):
    __tablename__ = 'disk'
    disk_id = db.Column(db.SmallInteger, primary_key=True)
    ip = db.Column(db.String(30), nullable=False)
    cluster_id = db.Column(db.SmallInteger, nullable=False)
    node_name = db.Column(db.String(30), nullable=False)
    disk_name = db.Column(db.String(30), nullable=False)


class NodeMultipleData(db.Model, BaseJSON):
    __tablename__ = 'node_multiple_data'
    time = db.Column(db.BigInteger, primary_key=True)
    disk_id = db.Column(db.SmallInteger, primary_key=True)
    indicator_id = db.Column(db.SmallInteger, primary_key=True)
    value = db.Column(db.Float, nullable=False)

