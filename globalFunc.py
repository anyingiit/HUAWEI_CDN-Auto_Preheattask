import time
def timestampToTime(timestamp):
    timestamp = time.localtime(timestamp)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S",timestamp)
    return timestamp