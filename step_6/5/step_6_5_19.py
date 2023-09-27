from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642),
        ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

profit = defaultdict(int)
for name in data:
    profit[name[0]] += name[1]

sorted_items = dict(sorted(profit.items(), key=lambda item: item[0]))


for name in sorted_items:
    print(f"{name}: ${sorted_items[name]}")
