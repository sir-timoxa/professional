from datetime import date


def saturdays_between_two_dates(start, end):
    a, b = start.toordinal(), end.toordinal()
    result=0
    if b < a:
        a, b = b, a
    for i in range(a,b+1):
        if date.fromordinal(i).weekday()==5:
            result+=1
    return result


# TEST_5:
date1 = date(2012, 7, 11)
date2 = date(2011, 8, 16)
print(saturdays_between_two_dates(date1, date2))

# TEST_6:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 5)
print(saturdays_between_two_dates(date1, date2))

# TEST_7:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)
print(saturdays_between_two_dates(date1, date2))

# TEST_8:
date1 = date(2018, 7, 14)
date2 = date(2018, 7, 14)
print(saturdays_between_two_dates(date1, date2))
