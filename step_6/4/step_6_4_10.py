import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', mode='rb') as file:
    data=pickle.load(file)

for x in data:
    for field, word in zip(Animal._fields,x):
        print(f"{field}: {word}")
    print()