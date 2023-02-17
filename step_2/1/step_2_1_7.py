def print_given(*args,**kwargs):
    for x in args:
        print(x,type(x))
    for key,value in sorted(kwargs.items()):
        print(key,value,type(value))
print_given(b=2, d=4, c=3, a=1)