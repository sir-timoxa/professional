n, x, y, a, b = map(int, input().split())

s = [int(x) for x in range(1, n+1)]




f1= s[:x-1]+list(reversed(s[x-1:y]))+s[y::]
f2 = f1[:a-1]+list(reversed(f1[a-1:b]))+f1[b::]


print(*f2)