import random

class RandomNumbers:
    def __init__(self, left,right,n):
        self.left = left
        self.right = right
        self.n = n
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.n:
            raise StopIteration
        else:
            self.counter += 1
            return random.randint(self.left, self.right)



