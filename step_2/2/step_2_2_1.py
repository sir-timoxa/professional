s = [int(input()) for x in range(3)]
s.sort()

a = sum(s)
k = (s[0]+s[1])*2

print(min(a, k))
