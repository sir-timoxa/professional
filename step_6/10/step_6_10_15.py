from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    try:
        if from_left:
            return chainmap[key]
        elif not from_left:
            for dct in reversed(chainmap.maps):
                if key in dct:
                    return dct[key]
                break
    except:
        return None            


    
chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))