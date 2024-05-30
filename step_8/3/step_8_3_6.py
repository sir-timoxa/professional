def count_number(number):
    if number == 0:
        return 0
    else:
        return 1 + count_number(number // 10)

print(count_number(int(input())))