def zip_longest(*args, fill=None):
    max_long = len(max(args, key=len))
    for arg in args:
        if len(arg) < max_long:
            arg.extend(list(map(lambda x: fill, range(max_long - len(arg)))))
    return list(zip(*args))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))
data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))
