import sys

counter=0
for line in sys.stdin:
    if line.strip()[0]=='#':
        counter+=1

print(counter)