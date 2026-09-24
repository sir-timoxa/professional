from itertools import pairwise,starmap

def is_rising(iterable):
    return all(starmap(lambda x, y: y > x, pairwise(iterable)))

def is_rising(iterable):
    return all(a < b for a, b in pairwise(iterable))

print(is_rising([1, 2, 3, 4, 5]))