
class Xrange:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if (self.end - self.current) * self.step <= 0:
            raise StopIteration

        value = self.current
        self.current += self.step
        return value


