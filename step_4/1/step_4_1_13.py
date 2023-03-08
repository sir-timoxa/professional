import sys
from datetime import datetime

data = [int(x) for x in sys.stdin]

if data:
    print(f"Рост самого низкого ученика: {min(data)}")
    print(f"Рост самого высокого ученика: {max(data)}")
    print(f"Средний рост: {sum(data)/len(data)}")
else:
    print("нет учеников")
          
          
