from collections import Counter

# books=Counter([x for x in input().split()])
# prices={}
# for _ in range(int(input())):
#     a=input().split()
#     prices[a[0]]=a[1]
# print(books)
# print(prices)
# sum=0
# for x in prices:
#     print(books)
#     if books[x]>0:
#         books[x]-=1
#         sum+=int(prices[x])
# print(sum)

books=Counter([x for x in input().split()])
prices=[input().split() for _ in range(int(input()))]
sum=0
for x in prices:
    if books[x[0]]>0:
        books[x[0]]-=1
        sum+=int(x[1])
print(sum)
