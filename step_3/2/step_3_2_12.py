from datetime import date
a = date.fromisoformat(input())
b = date.fromisoformat(input())

if a < b:
    print(a.strftime('%d-%m (%Y)'))
else:
    print(b.strftime('%d-%m (%Y)'))
