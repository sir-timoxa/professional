from datetime import date,datetime


def fill_up_missing_dates(dates):
    pattern='%d.%m.%Y'
    start = datetime.strptime(sorted(dates,key=lambda x : datetime.strptime(x,pattern))[0],pattern)
    end = datetime.strptime(sorted(dates,key=lambda x : datetime.strptime(x,pattern))[-1],pattern)

    return [(date.fromordinal(i)).strftime(pattern) for i in range(start.toordinal(), end.toordinal() + 1)]




# TEST_6:
dates = ['20.07.2021', '16.05.2021', '19.01.2021', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))

# TEST_7:
dates = ['20.07.2020', '16.05.2021', '19.01.2022', '18.11.2021', '17.10.2021', '15.03.2021']
print(len(fill_up_missing_dates(dates)))