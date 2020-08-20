user_input = input("Enter any key to continue or 'q' to exit the program:")
while user_input != 'q':

    def addNumbers(num1,num2):
        sum_number = num1 + num2
        return sum_number

    x = int(input('Enter 1st number: '))
    y = int(input('Enter 2nd number: '))

    sum_of_two = addNumbers(x,y)

    print('Sum of two numbers:',sum_of_two)
    user_input = input("Enter 'c' to continue or 'q' to exit the program:")

print('Your Program Ended')


