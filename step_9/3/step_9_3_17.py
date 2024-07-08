def print_operation_table(operation, rows, cols):
    result = [[operation(m, n) for n in range(1,cols+1)] for m in range(1,rows+1)]
    for x in result:
        print(*x)

print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)
