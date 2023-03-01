from datetime import datetime, timedelta

pattern = '%d.%m.%Y'

start = datetime.strptime(input(), pattern)
stop = datetime.strptime(input(), pattern)

my_date = start

while (my_date.month + my_date.day) % 2 == 0:
    my_date = my_date+timedelta(days=1)

while my_date <= stop:

    if my_date.weekday() != 0 and my_date.weekday() != 3:
        print(my_date.strftime(pattern))
    my_date = my_date+timedelta(days=3)