import csv 

with open('prices.csv', encoding='utf-8') as f:
    rows = csv.DictReader(f, delimiter=';')
    result={}
    for row in rows:
        magaz_name=row.pop('Магазин')
        # print(row)
        # print(min(row.items(),key=lambda x: int(x[1])))
        result.setdefault(magaz_name,min(row.items(),key=lambda x: int(x[1])))
    # print(result)
    final = min(result.items(),key=lambda x: int(x[1][1]))
    # print(final)
    print(f"{final[1][0]} : {final[0]}")
