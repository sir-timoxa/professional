def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    return len(names)+1
