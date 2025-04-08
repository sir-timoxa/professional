from datetime import date


def date_formatter(localization):
    loc = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    def f(my_date):
        return my_date.strftime(loc[localization])

    return f

date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))