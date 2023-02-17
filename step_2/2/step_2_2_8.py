names=[]
end='@beegeek.bzz'
for _ in range(int(input())):
    names.append(input().split('@')[0])
new_box=[input() for _ in range(int(input()))]


for word in new_box:
    check=word
    for i in range(1,20):
        if check in names:
            check=word+str(i)
            continue
        else:
            names.append(check)
            print(check+end)
            break