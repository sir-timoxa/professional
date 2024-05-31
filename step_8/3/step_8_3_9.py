def range_sum(numbers, start, end):
    if start == end:
        return numbers[start]
    else:
        return numbers[end] + range_sum(numbers, start, end - 1)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
