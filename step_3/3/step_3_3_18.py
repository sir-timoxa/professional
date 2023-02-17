from datetime import datetime
file_name = 'diary.txt'

with open(file_name, 'r', encoding='utf-8') as input:
    text = input.read().split('\n\n')

a=sorted(text,key=lambda x: datetime.strptime(x.split('\n')[0],'%d.%m.%Y; %H:%M'))

print(*a,sep='\n\n')
