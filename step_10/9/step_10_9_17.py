# from itertools import dropwhile
#
#
# def first_largest(iterable, number):
#     try:
#         return next(dropwhile(lambda x: x[1] < number, enumerate(iterable)),-1)[0]
#     except:
#         return -1
#
#
# numbers = [10, 2, 14, 7, 7, 18, 20]
#
# print(first_largest(numbers, 11))
#
#
# iterator = iter([-1, -2, -3, -4, -5])
#
# print(first_largest(iterator, 10))
#
#
#


def correct_comma(data):
    balance = 0
    for item in data:
        if item == ')':
            balance += 1
        elif item == '(':
            balance -= 1
    return True if balance == 0 else False

data=str(input())

print(correct_comma(data))


ports = [
    22,
    80,
    443,
    8080,
    8443,
]

print(ports[-2:-5:-1])
print(ports[-2:-5:1])