
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

# Примечание 2. В периоде (две даты через дефис) граничные даты включены.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.
from datetime import datetime, date


def change_date(gap):
    new_gap = gap.split('-')
    start = datetime.strptime(new_gap[0], '%d.%m.%Y').toordinal()
    end = datetime.strptime(new_gap[1], '%d.%m.%Y').toordinal()
    return [str(datetime.fromordinal(i)) for i in range(start, end+1)]


def is_available_date(booked_dates, date_for_booking):
    result_bd = []
    result_fb = []
    for x in booked_dates:
        if '-' in x:
            result_bd.extend(change_date(x))
        else:
            a = datetime.strptime(x, '%d.%m.%Y').toordinal()
            result_bd.append(str(datetime.fromordinal(a)))
    if '-' in date_for_booking:
        result_fb.extend(change_date(date_for_booking))
    else:
        a = datetime.strptime(date_for_booking, '%d.%m.%Y').toordinal()
        result_fb.append(str(datetime.fromordinal(a)))
    # return result_bd, result_fb
    if set(result_bd) & set(result_fb):
        return False
    else: 
        return True



# TEST_1:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

# TEST_2:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_3:
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))

# TEST_4:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))

# TEST_5:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))

# TEST_6:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))

# TEST_7:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))

# TEST_8:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))

# TEST_9:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

# TEST_10:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_11:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))

# TEST_12:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))

# TEST_13:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))

# TEST_14:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))

# TEST_15:
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))

# TEST_16:
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))

# TEST_17:
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))

# TEST_18:
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))

# TEST_19:
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))

# TEST_20:
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '04.11.2021'
print(is_available_date(dates, some_date))