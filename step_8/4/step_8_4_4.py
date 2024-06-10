def recursive_sum(data):
    sum = 0
    for i in data:
        if type(i) == int:
            sum += int(i)
        if type(i) == list:
            sum += recursive_sum(i)
    return sum


my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))
