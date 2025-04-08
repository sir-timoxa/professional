def generator_square_polynom(a, b, c):
    def f(x):
        return a * (x ** 2) + b * x + c

    return f

f = generator_square_polynom(26, 83, 22)
print(f(55))