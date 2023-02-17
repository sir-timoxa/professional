from datetime import date

def print_good_dates(dates):
    result = list(filter(lambda x: (x.month+x.day==29) and int(x.year)==1992, dates))
    for x in sorted(result):
        print(x.strftime('%B %d, %Y'))




# TEST_7:
dates = [date(1257, 12, 12), date(1992, 6, 23), date(1284, 11, 2), date(1992, 1, 1)]
print_good_dates(dates)

# TEST_8:
print(print_good_dates([]))