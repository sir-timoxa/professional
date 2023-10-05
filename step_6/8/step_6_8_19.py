from collections import Counter


def scrabble(symbols, word):
    counter1 = Counter(symbols.lower())
    counter1.subtract(word.lower())
    return False if min(counter1.values()) < 0 else True


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))
