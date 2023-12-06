from collections import ChainMap


def get_all_values(chainmap, key):
    result=set(x[key] for x in chainmap.maps if key in x)
    return result