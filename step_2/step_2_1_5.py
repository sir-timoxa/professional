
def same_parity(numbers=[]):
    try:
        a = numbers[0]
        if a % 2 == 0:
            return list(filter(lambda x: x % 2 == 0, numbers))
        else:
            return list(filter(lambda x: x % 2 == 1, numbers))
    except:
        return []


print(same_parity([]))
