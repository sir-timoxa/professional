def filter_anagrams(word,args):
    return [x for x in args if sorted(word)==sorted(x)]

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))