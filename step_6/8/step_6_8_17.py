from collections import Counter

data = Counter(
    'aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

def min_values():
    min_value=min(data.items(),key=lambda x: x[1])[1]
    result=[y for y in filter(lambda x :x[1]==min_value,data.items())]
    return result

def max_values():
    max_value=max(data.items(),key=lambda x: x[1])[1]
    result=[y for y in filter(lambda x :x[1]==max_value,data.items())]
    return result


data.min_values=min_values
data.max_values=max_values

print(data.max_values())
print(data.min_values())
