import json

numbers = [2,3,4,2,4,5,7,9,8]
filename = 'number.json'

# dump in json file
with open(filename,'w') as file_object:
    json.dump(numbers, file_object)

# load in json file

with open(filename) as f_object:
    numbers = json.load(f_object)
    print(numbers)