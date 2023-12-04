from collections import ChainMap
import json

with open('zoo.json', encoding='utf-8') as file:
    json_data = json.load(file)

my_data = ChainMap(*json_data)
print(sum(my_data.values()))