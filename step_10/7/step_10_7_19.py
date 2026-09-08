from collections import Counter


def unique(iterable):
    my_dict = Counter(iterable)
    unique = (x for x in my_dict)
    return unique


def unique(numbers):
    yield from (dict.fromkeys(numbers))

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))