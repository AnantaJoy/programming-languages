import json

def get_stored_username():
    """Get stored information if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        pass
    else:
        return username
def new_username():
    """Prompt for new username"""
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back",username+"!")

    else:
        username = new_username()
        print("We'll remember you when you com back",username+"!")
        
greet_user()
