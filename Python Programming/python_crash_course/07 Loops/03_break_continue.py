# Guessing Game
import random

secret_number = random.randint(0,6)
user_input_number = int(input('Guess the secret number(1-10):')) 


if secret_number==user_input_number:
    print("You Won")
else:
    print("Try Again")

##############
## Grade Calculation Exercise
###############################