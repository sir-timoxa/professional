f = input()
a, b = map(int, input().split())

result_max = max([eval(f) for x in range(a,b+1)])
result_min = min([eval(f) for x in range(a,b+1)])

print(f"Минимальное значение функции {f} на отрезке [{a}; {b}] равно {result_min}")
print(f"Максимальное значение функции {f} на отрезке [{a}; {b}] равно {result_max}")

