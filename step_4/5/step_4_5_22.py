from zipfile import ZipFile
import json

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    for path in info:
        if path.filename.endswith('.json'):
            # print(path.filename)
            try:
                result=[]
                with zip_file.open(path.filename) as file:
                    # print(file.read().decode('utf-8'))
                    my_data=json.load(file)
                    if my_data['team']=='Arsenal':
                            result.append([my_data['first_name'],my_data['last_name']])
                    # print(my_data)
                #     for team in my_data:
                #         print(team)
                #         if team['team']=='Arsenal':
                #             result.append([team['first_name'],team['last_name']])
                result=sorted(result,key=)
                print(*result)
            except:
                pass
