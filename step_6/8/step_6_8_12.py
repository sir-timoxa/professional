from collections import Counter

result=Counter(input().lower().split()).most_common()

print(result[0][0])