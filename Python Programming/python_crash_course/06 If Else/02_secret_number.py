# guessing game

i = 1
while(i<=3):
    secret_number = int(input('Enter your secret number:'))
    input_num = int(input('Enter a number:'))
    if(secret_number == input_num):
        print('You Won')
        print('Game Ended')
        break
    else:
        print('Try Again')
    i+=1