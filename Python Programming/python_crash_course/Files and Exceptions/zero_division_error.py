# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# try -except-else block
print('Give me two numbers, and I\'ll divide them')
print('Enter \'q\' to quit')

while True:
    first_number = input("\nEnter first number:")
    if first_number=='q':
        break
    second_number = input("\nEnter second number:")
    try:
        result = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You Can't divide by Zero!")
    else:
        print(result)