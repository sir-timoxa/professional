import sys

data = list(map(str.strip, sys.stdin))



if len(data) % 2 == 0:
    if int(data[-1]) % 2 == 0:
        print('Дима')
    else:
        print("Анри")
else:
    if int(data[-1]) % 2 == 0:
        print("Анри")
    else:
        print('Дима')

