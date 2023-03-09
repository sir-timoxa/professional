import csv

with open('sales.csv', encoding='utf-8') as file:
    rows = csv.reader(file, delimiter=';')
    rows=list(rows)  
    del rows[0]
    for row in rows:
        if int(row[2])<int(row[1]):
            print(row[0])


