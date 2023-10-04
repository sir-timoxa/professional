from collections import Counter

words=Counter(input().lower().split()).most_common()

result=[y[0] for y in sorted(filter(lambda x: x[1]==words[-1][1], words))]

print(', '.join(result))
