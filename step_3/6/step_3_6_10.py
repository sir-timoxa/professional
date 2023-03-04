import time


def calculate_it(func, *args):
    start = time.perf_counter()
    value = func(*args)
    end = time.perf_counter()
    return value, end-start
