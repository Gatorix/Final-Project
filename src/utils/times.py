import time


def get_current_milli_time():
    return int(round(time.time() * 1000))
