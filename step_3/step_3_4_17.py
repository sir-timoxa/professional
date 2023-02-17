from datetime import datetime, timedelta

start = datetime.strptime(input(), '%H:%M:%S')
time = int(input())


print((start+timedelta(seconds=time)).strftime('%H:%M:%S'))
