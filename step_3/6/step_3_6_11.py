import time


def get_the_fastest_func(funcs, arg):
    result = {}
    for x in funcs:
        start = time.perf_counter()
        value = x(arg)
        end = time.perf_counter()
        timing=end-start
        result[x]=result.setdefault(x, 0)+timing
    print(result)
    return min(result, key=result.get)


def for_and_append(iterable):             # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result
        

def list_comprehension(iterable):         # с использованием списочного выражения
    return [elem for elem in iterable]    
    

def list_function(iterable):              # с использованием встроенной функции list()
    return list(iterable) 

funcs = [for_and_append, list_comprehension,list_function]

print(get_the_fastest_func(funcs, range(100000)))