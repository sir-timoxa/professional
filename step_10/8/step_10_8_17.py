import itertools as it
import string

def alnum_sequence():
    num_and_chars = zip(range(1,27),string.ascii_uppercase)
    raspack = (elem for tuple in num_and_chars for elem in tuple)
    yield from it.cycle(raspack)


from itertools import cycle
from string import ascii_uppercase


def alnum_sequence():
    for item in zip(cycle(range(1, 27)), cycle(ascii_uppercase)):
        yield from item


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))