def reverse_args(func):
    def wrapper(*args, **kwargs):
        new_args = args[::-1]
        return func(*new_args, **kwargs)

    return wrapper


# TEST_1:
@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))


# TEST_2:
@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))



try:
    print(operation(0, 70))
except ZeroDivisionError:
    print('ZeroDivisionError')


# TEST_8:
@reverse_args
def operation(a, b, value=10):
    return a // b - value


print(operation(70, 70, value=70))