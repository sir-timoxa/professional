def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


# TEST_1:
@do_twice
def beegeek():
    print('beegeek')


beegeek()
print()


# TEST_2:
@do_twice
def beegeek():
    print('beegeek')


print(beegeek())
print()


