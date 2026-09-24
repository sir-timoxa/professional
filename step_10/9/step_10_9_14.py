from itertools import islice


def first_true(iterable, predicate=None):
    try:
        return next(islice(filter(predicate, iterable), 1))
    except StopIteration:
        return None

from itertools import dropwhile

def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool
    return next(dropwhile(lambda elem: not predicate(elem), iterable), None)