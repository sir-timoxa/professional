import csv
from datetime import datetime

pattern = "%d/%m/%Y %H:%M"

with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.DictReader(file, delimiter=','))
    result = {}
    rows = list(
        sorted(rows, key=lambda item: datetime.strptime(item['dtime'], pattern)))
    for row in rows:
        if row['email'] not in result:
            result.setdefault(row['email'], []).extend(
                [row['username'], row['email'], row['dtime']])
        else:
            now = datetime.strptime(row['dtime'], pattern)
            new = datetime.strptime(result[row['email']][2], pattern)
            if now > new:
                result[row['email']] = [row['username'], row['email'], row['dtime']]


sorted_result = dict(
    sorted(result.items(), key=lambda item: (item[1][1])))

with open('new_name_log.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=[
                            'username', 'email', 'dtime'])
    writer.writeheader()
    for row in sorted_result:
        writer.writerow(
            {'username': sorted_result[row][0], 'email': sorted_result[row][1], 'dtime': sorted_result[row][2]})


