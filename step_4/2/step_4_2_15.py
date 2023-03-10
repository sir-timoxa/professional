import csv 

def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',')
        result={}
        for dictionary in rows:
            for key,val in dictionary.items():
                result.setdefault(key,[]).append(val)
    return result
