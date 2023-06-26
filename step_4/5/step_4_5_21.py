from zipfile import ZipFile


def extract_this(zip_name, *args):
    if args:
        with ZipFile(zip_name) as zip_file:
            for name in args:
                 zip_file.extract(name)
    else:
        with ZipFile(zip_name) as zip_file:
            zip_file.extractall()


