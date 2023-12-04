from collections import ChainMap
from collections import Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10,
         'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

prices = ChainMap(bread, meat, sauce, vegetables, toppings)

data=Counter(sorted(input().split(',')))
summa=0
max_len_data=len(max(data, key=len))
for x in data:
    print(f"{x:{max_len_data}} x {data[x]}")
    summa+=(data[x]*prices[x])
if max_len_data<10:
    print('-'*len(f"ИТОГ: {summa}р"))
else:
    print('-'*(max_len_data+len(str(summa))+1))
print(f"ИТОГ: {summa}р")
