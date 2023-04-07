import json


with open('people.json', 'r', encoding='UTF-8') as input,  open('updated_people.json', 'w', encoding='UTF-8') as file:
    data = json.load(input)
    s_of_keys=set(key for i in data for key in i.keys())
    newdata=[]
    for my_dict in data:
        difiirence=s_of_keys-set(my_dict.keys())
        my_dict.update(dict.fromkeys(difiirence,None))
        newdata.append(my_dict)


    json.dump(newdata, file, indent=3)
