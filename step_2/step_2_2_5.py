n = int(input())

s = [x for x in range(1,n+1)]

my_d={}

for a in s:
    k=sum(map(int,str(a)))
    my_d.setdefault(k,[]).append(a)

result=max(my_d.values(),key=lambda x :len(x))
print(len(result))