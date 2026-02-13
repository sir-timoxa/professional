import functools
def prefix(symbol,to_the_end=False):
            def decorator(func):
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    value = func(*args, **kwargs)
                    return value+symbol if to_the_end else symbol+value
                return wrapper
            return decorator

# TEST_1:
@prefix('€')
def get_bonus():
    return '2000'


print(get_bonus())


# TEST_2:
@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())


# TEST_3:
@prefix(' online-school', to_the_end=True)
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())

