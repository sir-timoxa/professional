
old_print = print


def print(*args, sep=' ', end='\n'):
    caps = [arg.upper() if isinstance(arg, str) else arg for arg in args]
    if isinstance(sep,str):
        sep = sep.upper()
    if isinstance(end, str):
        end = end.upper()
    old_print(*caps, sep=sep, end=end)


print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')
words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')
