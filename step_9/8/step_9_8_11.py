import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        value = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {func.__name__}(): {repr(value)}")
        return value

    return wrapper


# INPUT DATA:

# TEST_1:
@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')


# TEST_2:
@trace
def sub(a, b, c):
    '''прекрасная функция'''
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)


# TEST_3:
@trace
def beegeek():
    '''beegeek docs'''
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)

