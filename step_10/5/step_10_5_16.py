def alternating_sequence(count=None):
    n = 1
    while n-1 != count:
        if n % 2 == 0:
            yield -n
        else:
            yield n
        n += 1
