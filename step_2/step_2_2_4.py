s = [int(x) for x in input().split()]

print(*sorted(set(filter(lambda x: s.count(x) > 1, s))))
