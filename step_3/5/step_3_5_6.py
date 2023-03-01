from datetime import datetime

pattern = '%d.%m.%Y'
result = {}

for i in range(int(input())):
    s = input().split()
    my_key = datetime.strptime(s[-1], pattern).date()
    my_name = ' '.join(s[:2])
    result.setdefault(my_key, []).append(my_name)


my_result = dict(sorted(result.items(), key=lambda x: len(x[1]),reverse=True))

final = []
max_result = 0

for x in my_result:
    if len(my_result[x]) >= max_result:
        max_result = len(my_result[x])
        final.append(x)


for x in sorted(final):
    print(x.strftime(pattern))