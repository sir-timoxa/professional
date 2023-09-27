import csv
from collections import namedtuple
from datetime import datetime

with open('meetings.csv', encoding='utf-8') as file:
    data = file.read()
    table = [x.split(',') for x in data.splitlines()]


User = namedtuple('User', table[0])

tuple_data = [User(*x) for x in table[1::]]

def my_date(arg):
    return datetime.strptime(arg.meeting_date, '%d.%m.%Y')

def my_time(arg):
    return datetime.strptime(arg.meeting_time, '%H:%M')


tuple_data.sort(key=lambda x: (my_date(x),my_time(x)))

for x in tuple_data:
    print(x.surname,x.name)