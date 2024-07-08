def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


def verification(login, password, success, failure):
    d = {0: 'в пароле нет ни одной буквы',
         1: 'в пароле нет ни одной заглавной буквы',
         2: 'в пароле нет ни одной строчной буквы',
         3: 'в пароле нет ни одной цифры'}
    result = [
        any(map(lambda x: x.isascii() and x.isalpha(), password)),
        any(map(lambda x: x.isupper(), password)),
        any(map(lambda x: x.isascii() and x.islower(), password)),
        any(map(lambda x: x.isdigit(), password))
    ]
    return (success(login) if all(result)
          else failure(login,text=d[result.index(False)]))


verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)