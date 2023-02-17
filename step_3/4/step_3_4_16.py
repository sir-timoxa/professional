from datetime import datetime, timedelta

start = datetime(1, 1, 1, 0, 0, 0)
time = datetime.strptime(input(), '%H:%M:%S')


print((time-start).seconds)
