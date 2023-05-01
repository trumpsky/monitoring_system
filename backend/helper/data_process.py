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


def find_muldule_or_package():
    for path in sys.path:
        print(path)
