def hash_as_key(objects):
    my_dict = {}
    for x in objects:
        my_dict.setdefault(hash(x),[]).append(x)
    result = {key: (value[0] if len(value) == 1 else value) for key, value in my_dict.items()}
    return result


data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))
