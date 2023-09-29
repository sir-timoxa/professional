from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})


new_data = OrderedDict()


for x in range(len(data)):
    if len(data) % 2 == 0:
        key, value = data.popitem(last=False)
        new_data[key] = value
    else:
        key, value = data.popitem(last=True)
        new_data[key] = value


print(new_data)

