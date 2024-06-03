def to_binary(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif number >= 2:
        return str(to_binary(number // 2)) + str(number % 2)


print(to_binary(256))
