def get_min_max(iterable):
    try:
        iterator = iter(iterable)
        min_val = max_val = next(iterator)

        for val in iterator:
            if val < min_val:
                min_val = val
            elif val > max_val:
                max_val = val

        return (min_val, max_val)
    except StopIteration:
        return None
