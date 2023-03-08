import sys

for i, line in enumerate(sys.stdin):
    if i==0:
        my_number=int(line.strip())
        continue
    now_number=int(line.strip())
    if now_number==(my_number+1):
        answer=1
        my_number=now_number
    elif now_number==(my_number*2):
        answer=2
        my_number=now_number
    else:
        answer=0
        print("Не прогрессия")
        break

if answer==1:
    print("Арифметическая прогрессия")
elif answer==2:
    print("Геометрическая прогрессия")

