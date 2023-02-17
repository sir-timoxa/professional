from datetime import datetime, timedelta

time = datetime.strptime(input(), '%d.%m.%Y')

print((time-timedelta(days=1)).strftime('%d.%m.%Y'))
print((time+timedelta(days=1)).strftime('%d.%m.%Y'))
