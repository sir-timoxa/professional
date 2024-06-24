data=eval(input())

if type(data) == list:
    print(data[-1])
elif type(data) == tuple:
    print(data[0])
elif type(data) == set:
    print(len(data))