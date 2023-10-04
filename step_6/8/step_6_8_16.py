from collections import Counter
import sys

result=Counter()
for line in sys.stdin:
    data=line.strip('\n').split()
    result.update({data[0]:int(data[1])})


print(result.most_common()[-2][0])