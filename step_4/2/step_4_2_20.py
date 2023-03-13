import csv 


def condense_csv(file_name,id_name):
    with open(file_name, encoding='utf-8') as file:
        rows = csv.reader(file)
        result={}
        for row in rows:
            if row[0] not in result:
                result[row[0]]=result.setdefault(row[0],{row[1]:row[2]})
            else:
                result[row[0]].update({row[1]:row[2]})
        
    # print(result)
    for x in result:
        header=[id_name,*(y for y in result[x])]
        break
    # print(header)

    with open('condensed.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        for row in result:
            answer=[row,*(y for y in result[row].values())]
            writer.writerow(answer)

condense_csv('test.csv', id_name='ID')


