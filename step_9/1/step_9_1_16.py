name = input()
result = sorted(name, key=lambda x: (
not x.islower(), not x.isupper(), x.isdigit() and int(x) % 2 == 0, x.isdigit() and int(x) % 2 == 1, x))
print(''.join(x for x in result))
