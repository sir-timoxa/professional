import sys

def test():
    def rec(start):
        if result[start] != '0':
            rec(start+1)
    print(*reversed(result),sep='\n')

result=[]
for line in sys.stdin:
    my_input=str(line.rstrip('\n'))
    result.append(my_input)
    if my_input=='0':
        break

test()