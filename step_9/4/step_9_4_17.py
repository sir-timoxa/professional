def polynom(x):
    result = x ** 2 + 1
    polynom.values.add(result)
    return result


polynom.values = set()
