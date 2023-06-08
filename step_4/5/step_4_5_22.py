from zipfile import ZipFile

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    for path in info:
        if path.filename.endswith('.json'):
            try:
                with zip_file.open(path.filename) as file:
                    print(file.read().decode('utf-8'))
            except:
                pass
