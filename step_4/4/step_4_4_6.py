import sys
import json

data=sys.stdin

new_data=json.load(data)

for x,y in new_data.items():
    if type(y) != list:
        print(f"{x}: {y}")
    else:
         print(f"{x}: {', '.join(map(str,y))}")





