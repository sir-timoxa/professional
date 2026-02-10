import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if isinstance(value, str):
            return value
        else:
            raise TypeError

    return wrapper





# INPUT DATA:

# TEST_1:
@returns_string
def beegeek():
    return 'beegeek'


print(beegeek())


# TEST_2:
@returns_string
def add(a, b):
    return a + b


try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))

