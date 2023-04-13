from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info=zip_file.infolist()
    file_size=0
    compress_size=0
    for x in info:
        file_size+=x.file_size
        compress_size+=x.compress_size
    print(f"Объем исходных файлов: {file_size} байт(а)")
    print(f"Объем сжатых файлов: {compress_size} байт(а)")