import time
import datetime

def datetime_to_timestamp(dt):
    dt = time.strptime(dt , "%Y/%m/%d %H:%M")
    return int(time.mktime(dt))


def timestamp_to_datetime(ts):
    return datetime.datetime.fromtimestamp(ts)
