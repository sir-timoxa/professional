def around(iterable):
    iterator = iter(iterable)
    try:
        current = next(iterator)
    except StopIteration:
        return
    previous = None

    for next_item in iterator:
        yield previous, current, next_item
        previous, current = current, next_item
    yield previous, current, None



data = map(str.upper, 'y')

iterator = around(data)

print(next(iterator))


