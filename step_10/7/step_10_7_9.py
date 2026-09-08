from datetime import date

def years_days(year):
    start = date(year,1,1).toordinal()
    end = date(year,12,31).toordinal()
    yield from (date.fromordinal(x) for x in range(start,end+1))




dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))