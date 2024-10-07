import json


my_list = [1, 2, 3, 4, 5]


with open('my_list.json', 'w') as file: #SAVE LIST TO FILE
    json.dump(my_list, file)
