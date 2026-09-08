def stop_on(iterable, obj):
    data=iter(iterable)
    result = iter(lambda: next(data), obj)
    yield from result


numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))

iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))
