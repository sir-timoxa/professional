def parse_ranges(ranges):
    for part in ranges.split(','):
        start, end = map(int, part.split('-'))
        yield from range(start, end + 1)



