
# Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

# Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

# Примечание 2. В периоде (две даты через дефис) граничные даты включены.

# Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.
from datetime import datetime

def is_available_date(booked_dates,date_for_booking):
    result_bd=[]
    result_fb=[]
    


booked_dates=['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking

print(is_available_date(booked_dates))