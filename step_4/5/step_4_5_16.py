from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    last = 100
    for x in info:
        if x.is_dir():
            continue
        else:
            if (x.compress_size/x.file_size)*100 <= last:
                last = (x.compress_size/x.file_size)*100
                last_file=x.filename
print(last_file.split('/')[-1])

