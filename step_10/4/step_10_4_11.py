class PowerOf:
    def __init__(self, n):
        self.n = n
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter +=1
        return self.n ** self.counter



