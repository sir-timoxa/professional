from collections import Counter

words=Counter([len(x) for x in input().lower().split()]).most_common()

for k,v in sorted(words, key=lambda x: x[1]):
    print(f"Слов длины {k}: {v}")
