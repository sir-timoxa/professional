from collections import Counter

books=Counter([x for x in input().split()])
prices=[input().split() for _ in range(int(input()))]
sum=0
for x in prices:
    if books[x[0]]>0:
        books[x[0]]-=1
        sum+=int(x[1])
print(sum)
