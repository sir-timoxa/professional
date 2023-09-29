from collections import Counter

data=list(input().split(','))

result=Counter(data)

for x in sorted(result):
    print(f"{x}: {result[x]}")


# products = Counter(input().split(','))

# for product, count in sorted(products.items()):
#     print(f'{product}: {count}')