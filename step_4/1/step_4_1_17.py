import sys
from datetime import datetime
pattern = '%d.%m.%Y'

for line in sys.stdin:
    my_date=datetime.strptime(line.strip(),pattern)
    break

check=0
counter=0
for line in sys.stdin:
    new_date=datetime.strptime(line.strip(),pattern)
    if new_date>my_date:
        counter+=1
        check+=1
        my_date=new_date
    elif new_date<my_date:
        counter+=1
        check-=1
        my_date=new_date
    else:
        check=0

if check>0 and check==counter:
    print("ASC")
elif check<0 and abs(check)==counter:
    print("DESC")
else:
    print("MIX")



