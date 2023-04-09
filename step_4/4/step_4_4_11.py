
import csv
import json

with open('playgrounds.csv', 'r', encoding='UTF-8') as input, open('addresses.json', 'w', encoding='UTF-8') as output:
    rows = csv.DictReader(input, delimiter=';')
    new_data = {}
    for row in rows:
        new_data.setdefault(row['AdmArea'], {}).setdefault(
            row['District'], []).append(row['Address'])

    json.dump(new_data,output, indent=3, ensure_ascii=False)
