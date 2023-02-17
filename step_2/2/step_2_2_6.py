from functools import reduce
s=[]
for i in range(int(input())):
    s.append(input().split(', '))

final=reduce(lambda a,b: set(a)&set(b),s)

if len(final)>0:
    print(*sorted(final),sep=', ')
else:
    print("Сериал снять не удастся")
