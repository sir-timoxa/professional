from datetime import datetime, timedelta

pattern = '%d.%m.%Y'
result={}

for i in range(int(input())):
    s=input().split()
    my_key=datetime.strptime(s[-1],pattern).date()
    result.setdefault(my_key,[]).append(s[:2])

if len(result[min(result)])==1:
    print(min(result).strftime(pattern),*result[min(result)][0])
else:
    print(min(result).strftime(pattern),len(result[min(result)]),sep=' ')