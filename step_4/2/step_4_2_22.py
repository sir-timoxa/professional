import csv 

with open('prices.csv', encoding='utf-8') as f:
    rows = csv.DictReader(f, delimiter=';')
    result={}
    for row in rows:
        print(row)

        # print(min(row.items(),key=lambda x: int(x[1])))

 


        # result[row['Магазин']]=result.setdefault(row)



