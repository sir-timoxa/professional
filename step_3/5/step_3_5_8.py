
from datetime import datetime, timedelta


def choose_plural(x, data):
    if str(x)[-2::] in ('11', '12', '13', '14'):
        return str(x)+' '+str(data[2])
    elif str(x)[-1] == '1':
        return str(x)+' '+str(data[0])
    elif str(x)[-1] in ('2', '3', '4'):
        return str(x)+' ' + str(data[1])
    else:
        return str(x)+' '+str(data[2])


pattern = '%d.%m.%Y %H:%M'

stop = datetime.strptime(input(), pattern)
start = datetime.strptime('08.11.2022 12:00', pattern)

delta = start-stop


days = delta.days
hours = delta.seconds//3600
minutes = (delta.seconds // 60) % 60


choose = {0: ("день", "дня", "дней"), 
        1: ("час", "часа", "часов"), 
        2: ("минута", "минуты", "минут")}


if days<0:
    print("Курс уже вышел!")
else:
        if days > 0:
            if hours > 0:
                if minutes > 0:
                    print(
                        f'До выхода курса осталось: {choose_plural(days,choose[0])} и {choose_plural(hours,choose[1])}')
                else:
                    print(f'До выхода курса осталось: {choose_plural(days,choose[0])}')
            else:
                if minutes>0:
                    print(f'До выхода курса осталось: {choose_plural(days,choose[0])}')
                else:
                    print(f'До выхода курса осталось: {choose_plural(days,choose[0])}')
        else:
            if hours > 0:
                if minutes > 0:
                    print(f'До выхода курса осталось: {choose_plural(hours,choose[1])} и {choose_plural(minutes,choose[2])}')
                else:
                    print(f'До выхода курса осталось: {choose_plural(hours,choose[1])}')
            else:
                if minutes > 0:
                    print(f'До выхода курса осталось: {choose_plural(minutes,choose[2])}')
                else:
                    print("Курс уже вышел!")