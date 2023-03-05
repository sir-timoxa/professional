import calendar

year,month=input().split()

abbr=list(calendar.month_abbr)

print(calendar.month(int(year),abbr.index(month)))