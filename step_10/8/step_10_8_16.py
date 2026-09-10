import itertools as it

def factorials(n):
    yield from it.accumulate(range(1, n+1), lambda a, b: a * b)

numbers = factorials(2)

print(next(numbers))
print(next(numbers))