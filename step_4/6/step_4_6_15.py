import pickle

filename=input()
hashsumm=int(input())

with open(filename, mode='rb') as file:
    data=pickle.load(file)

if type(data) is dict:
    data_hash=sum(list(filter(lambda x: type(x) is int, data)))
elif type(data) is list:
    reb=list(filter(lambda x: type(x) is int,data))
    if len(reb)<2:
        data_hash=0
    else:
        data_hash= min(reb)*max(reb)

if data_hash==hashsumm:
    print('Контрольные суммы совпадают')
else:
     print('Контрольные суммы не совпадают')

