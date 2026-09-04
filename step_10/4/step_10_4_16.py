class Alphabet:
    def __init__(self, language):
        self.data = {'en': 'abcdefghijklmnopqrstuvwxyz', 'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'}
        self.language = language
        self.iterator = iter(self.data[language])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            self.iterator = iter(self.data[self.language])
            return next(self.iterator)



