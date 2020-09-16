def word_counts(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read() 
    except FileNotFoundError:
        print("Sorry, the file "+filename+" does not exist.")
    else:
        words = content.split()
        word_len = len(words)
        print("The file "+filename+" has about "+ str(word_len)+" words.")

filename = 'alice.txt'
word_counts(filename)

# you can open and count multiple books 
# save filename in lists and loop through this lists