import csv

with open('data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    result = {}
    for row in rows:
        distric = row['email'].split('@')[1]
        result[domain]=result.setdefault(domain,0)+1
    sorted_result=dict(sorted(result.items(), key=lambda item: (item[1],item[0])))

with open('domain_usage.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['domain', 'count'])
    writer.writeheader()
    for row in sorted_result:
        writer.writerow({'domain': row,'count':sorted_result[row]})