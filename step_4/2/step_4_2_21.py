import csv 

with open('student_counts.csv', encoding='utf-8') as file,open('sorted_student_counts.csv', 'w', encoding='utf-8') as csv_file:
    rows = csv.DictReader(file, delimiter=',')
    sorted_result=sorted(rows.fieldnames[1:],key=lambda x: (int(x.split('-')[0]),x.split('-')[1]))
    header=[rows.fieldnames[0],*sorted_result]

    writer = csv.DictWriter(csv_file,delimiter=',',fieldnames=header)
    writer.writeheader()
    writer.writerows(rows)


        