from zipfile import ZipFile
import json
result=[]
with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    for path in info:
        if path.filename.endswith('.json'):
            try:
                with zip_file.open(path.filename) as file:
                    my_data=json.load(file)
                    if my_data['team']=='Arsenal':
                        result.append(f"{my_data['first_name']} {my_data['last_name']}")
            except:
                pass
result.sort()
print(*result,sep='\n')