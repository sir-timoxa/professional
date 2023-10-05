from collections import Counter
import csv

with open('name_log.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    data = []
    for line in rows:
        data.append(line['email'])


for k,v in sorted(Counter(data).items()):
    print(f"{k}: {v}")

# with open('name_log.csv', 'r', encoding='utf8') as file:
#     result = Counter(el['email'] for el in csv.DictReader(file))    