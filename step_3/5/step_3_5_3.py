from datetime import datetime, time, timedelta

pattern = '%d.%m.%Y %H:%M'

my_input = datetime.strptime(input(), pattern)


my_time = my_input.time()

if my_input.weekday() in range(0, 5):
    start = time(9, 0, 0)
    end = time(21, 0, 0)
    if start <= my_time < end:
        print(int((timedelta(hours=21)-timedelta(hours=my_input.hour,
              minutes=my_input.minute)).total_seconds()//60))
    else:
        print("Магазин не работает")
else:
    start = time(10, 0, 0)
    end = time(18, 0, 0)
    if start <= my_time < end:
        print(int((timedelta(hours=18)-timedelta(hours=my_input.hour,
              minutes=my_input.minute)).total_seconds()//60))
    else:
        print("Магазин не работает")