import json

with open('data1.json', 'r', encoding='UTF-8') as input1,open('data2.json', 'r', encoding='UTF-8') as input2,  open('data_merge.json', 'w', encoding='UTF-8') as file:
    data1 = json.load(input1)
    data2 = json.load(input2)
    data1.update(data2)
    json.dump(data1, file, indent=3)