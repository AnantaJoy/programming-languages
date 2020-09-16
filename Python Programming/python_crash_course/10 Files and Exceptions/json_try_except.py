import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what's your name?")
    with open(filename,'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you comeback,"+username+"!")
else:
    print("Welcome back",username+"!")