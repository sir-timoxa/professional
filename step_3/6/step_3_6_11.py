import time


def get_the_fastest_func(funcs, arg):
    result = {}
    for x in funcs:
        start = time.perf_counter()
        value = x(arg)
        end = time.perf_counter()
        timing=end-start
        result[x]=result.setdefault(x, 0)+timing
    print(result)
    return min(result, key=result.get)


