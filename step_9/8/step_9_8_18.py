import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


# INPUT DATA:

# TEST_1:
@repeat(3)
def say_beegeek():
    '''documentation'''
    print('beegeek')


say_beegeek()
print()


# TEST_2:
@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')


print(say_beegeek.__name__)
print(say_beegeek.__doc__)

print()


# TEST_3:
@repeat(1)
def beegeek():
    '''beegeek docs'''
    print('beegeek')


print(beegeek.__name__)
print(beegeek.__doc__)
beegeek()

print()
