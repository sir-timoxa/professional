from zipfile import ZipFile, ZipInfo

with ZipFile('workbook.zip') as zip_file:
    s=list(map(ZipInfo.is_dir,zip_file.infolist()))
    print(s.count(False))
    