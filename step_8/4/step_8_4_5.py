def linear(nested_lists):
    sum = []
    def linear_rec(nested_lists):
        for i in nested_lists:
            if type(i) == int:
                sum.append(i)
            elif type(i) == list:
                linear_rec(i)
        return sum
    return linear_rec(nested_lists)

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))