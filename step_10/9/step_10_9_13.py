from itertools import dropwhile

def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)


iterator = iter('ssssssssssssssssssssssss')

print(list(drop_this(iterator, 's')))