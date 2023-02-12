file_name = 'files.txt'
size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
s = []
with open(file_name, 'r', encoding='utf-8') as input:
    for line in input:
        split_line = line.split()
        f2 = size_file[split_line[-1]]*int(split_line[-2])
        f1 = split_line[0].split('.')
        s.append(f1+[f2])

final = sorted(s, key=lambda x: (x[1], x[0]))

size=0
for i in range(1,len(final)):
    print(f'{final[i-1][0]}.{final[i-1][1]}')   
    if final[i-1][1] != final[i][1]:
        size+=int(final[i-1][2])
        if size>=size_file['GB']:
            size=round(size/size_file['GB'])
            file_end='GB'
        elif size>=size_file['MB']:
            size=round(size/size_file['MB'])
            file_end='MB'
        elif size>=size_file['KB']:
            size=round(size/size_file['KB'])
            file_end='KB'
        else:
            file_end='B'
        print('----------')
        print(f'Summary: {size} {file_end}')
        print()
        size=0
    else:
        size+=int(final[i-1][2])
else:
        print(f'{final[-1][0]}.{final[-1][1]}') 
        size+=int(final[-1][2])
        if size>=size_file['GB']:
            size=round(size/size_file['GB'])
            file_end='GB'
        elif size>=size_file['MB']:
            size=round(size/size_file['MB'])
            file_end='MB'
        elif size>=size_file['KB']:
            size=round(size/size_file['KB'])
            file_end='KB'
        else:
            file_end='B'
        print('----------')
        print(f'Summary: {size} {file_end}')


77320192