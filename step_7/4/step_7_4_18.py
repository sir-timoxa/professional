def get_weekday(number):
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if int(number) < 1 or int(number) > 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return days[number-1]


days = [
    'Понедельник',
    'Вторник',
    'Среда',
    'Четверг',
    'Пятница',
    'Суббота',
    'Воскресенье'
]
