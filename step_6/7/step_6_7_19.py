from collections import Counter

letters=Counter()
with open('pythonzen.txt', 'r') as file:
    for line in file:
        letters.update(filter(str.isalpha, line.lower()))


for x in sorted(letters):
    print(f"{x}: {letters[x]}")