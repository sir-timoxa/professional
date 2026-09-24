from itertools import chain


def sum_of_digits(iterable):
    data = map(str, iterable)

    return sum(map(int,chain.from_iterable(data)))




print(sum_of_digits([13, 20, 41, 2, 2, 5]))
