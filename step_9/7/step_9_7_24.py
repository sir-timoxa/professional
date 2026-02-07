def takes_positive(func):
    def wrapper(*args, **kwargs):
        int_check = all(isinstance(x, int) for x in [*args, *kwargs.values()])
        positive_check = all(x > 0 for x in [*args, *kwargs.values()])
        if not int_check:
            return TypeError
        if not positive_check:
            return ValueError
        else:
            return func(*args, **kwargs)


    return wrapper


# TEST_1:
@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# TEST_2:
@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))

