import random

def random_numbers(left,right):
    zero_iterator = iter(lambda: random.randint(left, right), -1)
    return zero_iterator



