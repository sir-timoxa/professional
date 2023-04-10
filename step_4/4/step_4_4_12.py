import json
import csv


with open('pools.json', 'r', encoding='UTF-8') as input:
    data = json.load(input)
    my_data={}
    for x in data:
        new_time = x['WorkingHoursSummer']["Понедельник"].split('-')
        start = new_time[0].split(':')[0]
        end = new_time[1].split(':')[0]
        if int(start) <= 10 and int(end) >= 12:
            my_data.setdefault(x['Address'],(int(x['DimensionsSummer']['Length']),int(x['DimensionsSummer']['Width'])))
    result=sorted(my_data.items(),key=lambda x: (x[1][0],x[1][1]),reverse=True)
    print('x'.join(map(str,result[0][1])))
    print(result[0][0])
