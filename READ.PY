import json

with open('my_list.json', 'r') as file:
    recovered_list = json.load(file)

print(recovered_list)
