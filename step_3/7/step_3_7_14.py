import calendar
from datetime import date


def get_all_thursday(year):
    result = []
    for month in range(1, 13):
        counter=0
        days = calendar.monthrange(year, month)[1]
        for day in range(1, days+1):
            if calendar.weekday(year, month, day) == 3:
                counter+=1
                if counter==3:
                    result.append(date(year, month, day))
    return result

my_result=get_all_thursday(int(input()))

for x in my_result:
    print(x.strftime('%d.%m.%Y'))

