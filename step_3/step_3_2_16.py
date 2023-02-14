from datetime import date
counter = 0
do = True
while do:
    my_date = input()
    if my_date == 'end':
        do = False
    else:
        try:
            day, month, year = my_date.split('.')
            my_date = date(int(year), int(month), int(day))
            print('Корректная')
            counter += 1
        except:
            print('Некорректная')
else:
    print(counter)
