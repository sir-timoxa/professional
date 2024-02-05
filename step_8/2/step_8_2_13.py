def print_digits(number):
    start=0
    number = str(number)
    if len(number) > 0:
        print(number[start])
        print_digits(number[start+1:])


print_digits(12345)
