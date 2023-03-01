from datetime import datetime, date

pattern = '%d.%m.%Y'
result = {}
check_list = []
check_date = datetime.strptime(input(), pattern).date()


for x in range(check_date.toordinal()+1, check_date.toordinal()+8):
    check_list.append((datetime.fromordinal(x).month,datetime.fromordinal(x).day))


for i in range(int(input())):
    s = input().split()
    my_key = datetime.strptime(s[-1], pattern).date()
    my_name = ' '.join(s[:2])
    result.setdefault(my_key, []).append(my_name)

result = dict(sorted(result.items(), reverse=True))




flag = False
for x in result:
    new_date = (x.month, x.day)
    if new_date in check_list:
        print(*result[x])
        flag = True
        break
        
if flag == False:
    print("Дни рождения не планируются")


