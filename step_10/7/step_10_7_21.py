def with_previous(iterable):
    previous = None
    for current in iterable:
        yield (current, previous)
        previous = current



numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))