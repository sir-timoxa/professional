def count_number(number):
    if number == 0:
        return 0
    else:
        return number%10 + count_number(number // 10)

print(count_number(int(input())))