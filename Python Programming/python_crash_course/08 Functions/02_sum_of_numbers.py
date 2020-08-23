# pass parameter to a function

num1 = input('Enter 1st number: ')
num2 = input('Enter 2nd number: ')

def sum(num1,num2):
    print('Sum of',num1,'and',num2,'is',num1+num2)

sum(int(num1),int(num2))