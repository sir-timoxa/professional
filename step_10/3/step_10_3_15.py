def is_iterator(obj):
    try:
        next(obj)
        return True
    except TypeError:
        return False



