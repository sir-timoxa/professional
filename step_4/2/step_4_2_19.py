import csv
from datetime import datetime

pattern="%d/%m/%Y %H:%M"

with open('name_log.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')
    result = {}
    for row in rows:
        datetime.strptime(row['dtime'], pattern)
       



