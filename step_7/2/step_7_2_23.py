
import sys
data = list(map(str.strip, sys.stdin))
summa = 0
counter = 0
for x in data:
    if '.' in x:
        try:
            summa += float(x)
        except:
            counter += 1
    else:
        try:
            summa += int(x)
        except:
            counter += 1

print(summa)
print(counter)



