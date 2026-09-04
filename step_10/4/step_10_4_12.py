class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.keys=list(data.keys())


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            item = self.data[self.keys[self.index]]
            key = self.keys[self.index]
            self.index += 1
            return key,item



