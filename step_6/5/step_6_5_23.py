from collections import defaultdict

def flip_dict(dict_of_lists):
    flip = defaultdict(list)
    for key, value in dict_of_lists.items():
        for x in value:
            flip[x].append(key)
    return flip

