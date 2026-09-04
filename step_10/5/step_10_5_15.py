def simple_sequence():
    start = 1
    while True:
        for _ in range(start):
            yield start
        start += 1



