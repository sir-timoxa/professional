from datetime import datetime,timedelta

dates = input().split()

pattern='%d.%m.%Y'
result=[]
for i in range(1,len(dates)):
    result.append(abs(datetime.strptime(dates[i],pattern)-datetime.strptime(dates[i-1],pattern)).days)


print(result)