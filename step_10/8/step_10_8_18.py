
def roundrobin(*args):
    iterators = [iter(arg) for arg in args]

    while iterators:
        active_iterators = []

        for iterator in iterators:
            try:
                yield next(iterator)
                active_iterators.append(iterator)
            except StopIteration:
                pass

        iterators = active_iterators


def roundrobin(*args):
    iters = tuple(iter(a) for a in args)
    while True:
        err_counter = 0
        for i in iters:
            try:
                res = next(i)
            except:
                err_counter += 1
            else:
                yield res
        if err_counter == len(iters):
            break


print(*roundrobin('abc', 'd', 'ef'))