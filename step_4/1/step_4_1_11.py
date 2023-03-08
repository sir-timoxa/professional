import sys
from datetime import datetime

data = list(map(str.strip, sys.stdin))
dates = [datetime.fromisoformat(x) for x in data]

result=max(dates)-min(dates)

print(result.days)