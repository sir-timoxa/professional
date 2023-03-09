import csv

column=int(input())

with open('deniro.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=','))
    column-=1
    if column==0:
        result=sorted(rows,key=lambda x: x[0])
    else:
        result=sorted(rows,key=lambda x: int(x[column]))
    
for x in result:
    print(','.join(x))
