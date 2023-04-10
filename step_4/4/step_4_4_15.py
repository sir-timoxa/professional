import json

with open('food_services.json', 'r', encoding='UTF-8') as input:
    data = json.load(input)
    first, second = {}, {}
    for x in data:
        first[x['District']] = first.setdefault(x['District'], 0)+1
        if x['OperatingCompany']:
            second[x['OperatingCompany']] = second.setdefault(x['OperatingCompany'], 0)+1
    max_key_first=max(first,key=lambda x: first[x])
    max_key_second=max(second,key=lambda x: second[x])
    print(max_key_first,first[max_key_first],sep=': ')
    print(max_key_second,second[max_key_second],sep=': ')