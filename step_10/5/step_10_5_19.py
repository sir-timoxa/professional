import datetime

from datetime import date

def dates(start, count=None):
    n = 0
    try:
        while n != count:
            yield start
            start += datetime.timedelta(days=1)
            n+=1
    except OverflowError:
        return StopIteration
