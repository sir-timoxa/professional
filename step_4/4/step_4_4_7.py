import json


def change_str(x):
    return x + '!'


def change_int(x):
    return x + 1


def change_bool(x):
    return not x


def change_list(x):
    return x*2


def change_dict(x):
    x["newkey"] = None
    return x




with open('newdata.json', 'r', encoding='UTF-8') as input,  open('step4_4_7.json', 'w', encoding='UTF-8') as file:
    data = json.load(input)
    new_data=[]
    for x in data:
        if type(x) == str:
            x = change_str(x)
            new_data.append(x)  
        elif type(x) == int:
            x = change_int(x)
            new_data.append(x)
        elif type(x) == list:
            x = change_list(x)
            new_data.append(x)
        elif type(x) == dict:
            x = change_dict(x)
            new_data.append(x)
        elif type(x) == bool:
            x = change_bool(x)
            new_data.append(x)
        elif type(x) == None:
            continue
        
        



    json.dump(new_data, file, indent=3)
