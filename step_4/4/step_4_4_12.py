import csv
import json

with open('students.json', 'r', encoding='UTF-8') as input, open('data.csv', 'w', encoding='UTF-8') as output:
    data = json.load(input)
    my_list=[]
    for x in data:
        if x['age']>17 and x['progress']>74:
            my_list.append({'name':x['name'],'phone':x['phone']})
    
    
    header=['name','phone']
    writer = csv.DictWriter(output,delimiter=',',fieldnames=header)
    writer.writeheader()
    writer.writerows(sorted(my_list,key=lambda x:x['name']))


   
