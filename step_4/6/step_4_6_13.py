import pickle
import sys

data = list(map(str.strip, sys.stdin))
filename=data[0]

with open(filename, 'rb') as file:
    obj = pickle.load(file)
    print(obj(*data[1::]))
