def power(x):
    def mult(y):
        return y ** x
    return mult


result = power(4)(2)
print(result)