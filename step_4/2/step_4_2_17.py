import csv

with open('wifi.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    result = {}
    for row in rows:
        district = row['district']
        count = int(row['number_of_access_points'])
        result[district] = result.setdefault(district, 0)+count
    sorted_result = dict(sorted(result.items(), key=lambda item: (-item[1],item[0])))


for x in sorted_result:
    print(f'{x}: {sorted_result[x]}')
