import calendar
from datetime import date


def get_all_mondays(year):
    result = []
    for month in range(1, 13):
        days = calendar.monthrange(year, month)[1]
        for day in range(1, days+1):
            if calendar.weekday(year, month, day) == 0:
                result.append(date(year, month, day))
    return result
