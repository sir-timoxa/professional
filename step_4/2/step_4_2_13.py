import csv

with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    result={}
    for row in rows:
        result.setdefault(row['company_name'],[]).append(int(row['salary']))
    last={}
    for row in result:
        last[row]=last.setdefault(row,0)+(sum(result[row])/len(result[row]))


print(*sorted(last,key=last.get),sep='\n')
