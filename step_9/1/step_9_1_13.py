def my_pow(number):
    return sum(int(a)**b for b,a in enumerate(str(number),start=1))

print(my_pow(139))