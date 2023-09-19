import pickle

filename=input()
hashsumm=int(input())

with open(filename, mode='rb') as file:
    data=pickle.load(file)
    if type(data) is dict:
        data_hash=sum(list(filter(lambda x: type(x) is int, data)))
    elif type(data) is list:
        reb=list(filter(lambda x: type(x) is int,data))
        data_hash= reb[0]*reb[1]
    if data_hash==hashsumm:
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')

