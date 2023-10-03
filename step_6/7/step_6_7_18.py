from collections import Counter

products = Counter(input().split(','))

max_len = 1
for key in products:
    if len(key) > max_len:
        max_len = len(key)


for key in dict(sorted(products.items())):
    if ' ' not in list(key):
        sum_of_ord = sum(map(ord, list(key)))
    else:
        sum_of_ord = sum(map(ord, list(key))) - 32
    print(
        f'{key:{max_len}}: {sum_of_ord} UC x {products[key]} = {sum_of_ord*products[key]} UC')
