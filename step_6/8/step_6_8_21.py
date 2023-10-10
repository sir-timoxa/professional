from collections import Counter
import csv
import json

final=Counter()
for name in ['quarter1.csv','quarter2.csv','quarter3.csv','quarter4.csv']:
    result={}
    with open(name, encoding='utf-8') as f1:
        _,*rows = list(csv.reader(f1, delimiter=','))
        for line in rows:
            result[line[0]]=sum(map(int,line[1:]))
        final+=result

with open('prices.json', encoding='utf-8') as fp:
    json_data = json.load(fp) 
    print(sum([json_data[x]*final[x] for x in final]))