from functools import reduce

def get_biggest(data):
    if data:
        final = sorted(data,key=lambda x: str(x)*len(str(max(data))),reverse=True)
        return int(reduce(lambda x,y:str(x)+str(y),final))
    else:
        return -1