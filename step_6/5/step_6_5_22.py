from collections import defaultdict


def wins(pairs):
    gamers = defaultdict(set)
    for key, value in pairs:
        gamers[key].add(value)
    return gamers

