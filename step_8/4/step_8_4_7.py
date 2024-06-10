def get_all_values(nested_dicts, key):
    result = set()
    def get_all_values_rec(nested_dicts):
        if key in nested_dicts:
            result.add(nested_dicts[key])
        for v in nested_dicts.values():
            if type(v) == dict:
                get_all_values_rec(v)
    get_all_values_rec(nested_dicts)
    return result


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))