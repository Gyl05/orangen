import time


def trans_stamp2datetime(timestamp):
    struct_time = time.gmtime(timestamp)
    time_str = time.strftime(struct_time)
    return time_str
