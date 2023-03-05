import calendar

year, month = input().split()

name = list(calendar.month_name)

number = name.index(month)

print(calendar.monthrange(int(year), number)[1])
