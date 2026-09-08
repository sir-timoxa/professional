def pairwise(iterable):
    iterator = iter(iterable)
    try:
        current = next(iterator)
        for next_item in iterator:
            yield current, next_item
            current = next_item
        yield current, None
    except StopIteration:
        pass



print(list(pairwise([])))
