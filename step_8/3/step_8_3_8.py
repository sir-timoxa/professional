def number_of_frogs(year):
    if year == 1:
        return 77
    else:
        return (number_of_frogs(year-1)-30)*3


print(number_of_frogs(2))
