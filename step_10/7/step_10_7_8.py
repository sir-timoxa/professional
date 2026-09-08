

with open('data.csv', encoding='utf-8') as csv_file:
    file_lines = (line for line in csv_file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_dicts = (dict(zip(file_headers, data)) for data in line_values)
    summa =sum(int(x['raisedAmt']) for x in line_dicts if x['round'] == 'a')
    print(summa)

with open('data.csv', encoding='utf-8') as file:
    data_rows = (line.strip().split(',') for line in file)
    total_a_round = sum(int(amt) for _, amt, rnd in data_rows if rnd == 'a')
    print(total_a_round)