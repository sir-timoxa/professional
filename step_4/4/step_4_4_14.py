import csv
import json
from datetime import datetime
pattern = '%Y-%m-%d %H:%M:%S'

with open('exam_results.csv', 'r', encoding='UTF-8') as input, open('best_scores.json', 'w', encoding='UTF-8') as output:
    rows =list(csv.DictReader(input, delimiter=','))
    rows=sorted(rows,key=lambda x: datetime.strptime(x['date_and_time'], pattern))
    my_data = {}
    for x in rows:
        if x['email'] not in my_data:
            new_value = {key: value for key, value in zip(
                ('name', 'surname', 'best_score', 'date_and_time', 'email'), x.values())}
            new_value['best_score'] = int(new_value['best_score'])
            my_data.setdefault(x['email'], new_value)
        else:
            if int(x['score']) >= int(my_data[x['email']]['best_score']):
                my_data[x['email']].update({'best_score': int(x['score'])})
                my_data[x['email']].update(
                    {'date_and_time': x['date_and_time']})
    my_data = dict(sorted(my_data.items()))
    my_data = list(my_data.values())
    json.dump(my_data, output, indent=3)
