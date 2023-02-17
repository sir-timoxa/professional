def is_valid(pin):
    if 4<=len(pin)<=6:
        return all(list(map(lambda x: x.isdigit() and x!=' ',pin)))
    else:
        return False
print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))