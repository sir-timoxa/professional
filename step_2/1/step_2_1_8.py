def convert(string):
    x=list(map(lambda x: x.isalpha() and x.isupper(),string))
    y=list(map(lambda x: x.isalpha() and x.islower(),string))
    if x.count(True) > y.count(True):
        return string.upper()
    else:
        return string.lower()

print(convert('BEEgek'))
print(convert('pyTHON'))
print(convert('pi31415!'))