import sys

d={}
for line in sys.stdin:
    if "/" in line:
        data=line.strip().split(' / ')
        d.setdefault(data[1], []).append((data[0],float(data[-1])))
    else:
        theme=line.strip()

result=sorted(d[theme],key=lambda x: (x[1],x[0]))


for x in result:
    print(x[0])