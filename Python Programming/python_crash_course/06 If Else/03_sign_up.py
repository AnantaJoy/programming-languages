# You can't register to this account if your less than 18 years

user_age = int(input('Enter your age: '))

if user_age<14:
    print("Sorry Kiddo! You're to small")
elif user_age<18 and user_age >=14:
    print("You're not allowed to individual.But you can create a account jointly with your parents")
else:
    print('Go to the next process')