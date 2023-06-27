from zipfile import ZipFile

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for x in info:
        #print(x.filename)
        if '/' not in x.filename:
            print(f"{x.filename} {convert_bytes(x.file_size)}")
        elif x.filename[-1] == '/':
            print("  "*(len(x.filename.split('/'))-2)+f"{x.filename.split('/')[-2]}")
        else:
            print("  "*(len(x.filename.split('/'))-1)+f"{x.filename.split('/')[-1]} {convert_bytes(x.file_size)}")
