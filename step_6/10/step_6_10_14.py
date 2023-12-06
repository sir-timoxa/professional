from collections import ChainMap


def deep_update(chainmap, key, value):
    flag = False
    for x in chainmap.maps:
        if key in x:
            x[key]=value
            flag=True
    if not flag:
        chainmap.maps[0][key]=value


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)
