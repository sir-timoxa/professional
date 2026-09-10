import itertools as it


def tabulate(func):
    counter = it.count(1)
    yield from (func(num) for num in counter)

def tabulate(func):
    return map(func, it.count(1))


func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))
