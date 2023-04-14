from zipfile import ZipFile
from datetime import datetime

pattern='%Y-%m-%d %H:%M:%S'
my_time=datetime.strptime('2021-11-30 14:22:00',pattern)
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    s=[x.filename.split('/')[-1] for x in info if datetime(*x.date_time)>my_time]


print(*sorted(s),sep='\n')