import json

with open('food_services.json', 'r', encoding='UTF-8') as input:
    data = json.load(input)
    first = {}
    for x in data:
        first.setdefault(x['TypeObject'], []).append(
            (x['Name'], x['SeatsCount']))
    
    first=dict(sorted(first.items()))

    for y in first:
        max_key = max(first[y], key=lambda x: x[1])
        print(f"{y}: {', '.join(map(str,max_key))}")
