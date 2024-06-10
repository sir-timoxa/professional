def dict_travel(nested_dicts,path=''):
    for key, value in sorted(nested_dicts.items()):
        if isinstance(value, dict):
            dict_travel(value, path +f"{key}.")
        else:
            print(f"{path}{key}: {value}")


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
