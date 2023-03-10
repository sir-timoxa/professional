import csv

with open('titanic.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    result = {}
    for row in rows:
        if row["survived"] == '1' and float(row['age']) < 18:
            result[row['name']] = result.setdefault(row['name'], row['sex'])

    sorted_result = dict( sorted(result.items(), key=lambda item: (item[1]),reverse=True))


# for x in sorted_result:
#     print(f'{x}: {sorted_result[x]}')

print(*sorted_result,sep='\n')
