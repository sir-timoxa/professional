import pickle

def filter_dump(filename ,objects, typename):
    data=list(filter(lambda x: type(x) is typename, objects))
    with open(filename, mode='wb') as file:
         pickle.dump(data, file)

filter_dump('numbers.pkl', [1, '2', 3, 4, '5'], int)
