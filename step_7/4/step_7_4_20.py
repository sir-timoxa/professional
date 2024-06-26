import json

try:
    with open(input(), encoding='utf-8') as file:
        data=json.load(file)
        print(data)
except OSError:
    print('Файл не найден')
except ValueError:
    print('Ошибка при десериализации')