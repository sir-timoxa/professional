from datetime import timedelta, datetime

time = datetime.strptime(input(), '%d.%m.%Y')
delta = timedelta(days=0)

for i in range(1, 11):
    print((time+delta).strftime('%d.%m.%Y'))
    delta += timedelta(days=i+1)
