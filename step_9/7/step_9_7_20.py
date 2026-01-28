def decor(func):
    def behavior(*args, **kwargs):
        args_new = tuple([x.upper() if isinstance(x, str) else x for x in args])
        kwargs_new = {key: value.upper() if isinstance(value, str) else value for key, value in kwargs.items()}
        func(*args_new, **kwargs_new)

    return behavior


def decor(func):
    def behavior(*args, **kwargs):
        args_new = tuple([x.upper() if isinstance(x, str) else x for x in args])
        kwargs_new = {key: value.upper() if isinstance(value, str) else value for key, value in kwargs.items()}
        func(*args_new, **kwargs_new)

    return behavior



print = decor(print)

print(111, 222, 333, sep='xxx')
