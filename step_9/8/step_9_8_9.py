import functools
def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        return value**2
    return wrapper




# TEST_1:
@square
def add(a, b):
    return a + b

print(add(3, 7))

# TEST_2:
@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)
