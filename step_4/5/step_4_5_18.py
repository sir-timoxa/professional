from zipfile import ZipFile
from datetime import datetime

pattern = '%Y-%m-%d %H:%M:%S'
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    s = {x.filename.split('/')[-1]: [datetime(*x.date_time).strftime(
        pattern), x.file_size, x.compress_size] for x in info if not x.is_dir()}

for x in sorted(s):
    print(x)
    print(f'  Дата модификации файла: {s[x][0]}')
    print(f'  Объем исходного файла: {s[x][1]} байт(а)')
    print(f'  Объем сжатого файла: {s[x][2]} байт(а)')
    print()