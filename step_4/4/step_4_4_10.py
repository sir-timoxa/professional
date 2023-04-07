
import json

with open('countries.json','r',encoding='UTF-8') as input , open('religion.json','w',encoding='UTF-8') as output:
    data=json.load(input)
    my_dict={}
    for data_dict in data:
        my_dict.setdefault(data_dict['religion'],[]).append(data_dict['country'])

    json.dump(my_dict, output, indent=3)



