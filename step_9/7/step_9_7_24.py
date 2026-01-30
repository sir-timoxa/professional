def takes_positive(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return (result, 'Функция выполнилась без ошибок')
        except:
            return (None, 'При вызове функции произошла ошибка')

    return wrapper