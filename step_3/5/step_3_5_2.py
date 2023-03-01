from datetime import date, time, datetime, timedelta

start = date(1, 1, 1).toordinal()
end = date(9999, 12, 31).toordinal()

d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


for i in range(start,end+1):
    if date.fromordinal(i).day==13:
        x=date.fromordinal(i).weekday()
        d[x] = d.setdefault(x, 1)+1
print(*d.values(),sep='\n')