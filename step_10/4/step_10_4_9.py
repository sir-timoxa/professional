class Square:
    def __init__(self, n):
        self.n = n
        self.counter = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.n:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter**2



