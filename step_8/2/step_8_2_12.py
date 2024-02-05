def print_digits(number):
    number = str(number)
    if len(number) > 0:
        print(number[-1])
        print_digits(number[:len(number)-1])


print_digits(12345)
