from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

pattern = '%H:%M'
result=0
for x in data:
    start=[int(y) for y in x[0].split(':')]
    stop=[int(y) for y in x[1].split(':')]
    mydelta = abs(timedelta(hours=int(start[0]),minutes=int(start[1]))-timedelta(hours=int(stop[0]),minutes=int(stop[1])))
    result+=(mydelta.total_seconds()//60)
print(int(result))