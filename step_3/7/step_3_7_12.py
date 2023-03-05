from datetime import date
import calendar

def get_days_in_month(year,month_name):
    name = list(calendar.month_name)
    number_month = name.index(month_name)
    count_days=calendar.monthrange(int(year), number_month)[1]
    return [date(year,number_month,x) for x in range(1,count_days+1)]
