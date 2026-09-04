def interleave(*args):
    return (i for elem in zip(*args) for i in elem )
