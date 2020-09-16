filename = 'alice.txt'

try:
    with open(filename) as file_object:
        content = file_object()
except FileNotFoundError:
    msg = "Sorry, the file " + filename +" does not exist."
    print(msg)