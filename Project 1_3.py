import random

x = True
guess = 0
while (x == True):
    num = int(input('Guess a number from 1-100: '))
    num2 = random.randint(1, 100)
    
    if (num > num2):
        guess += 1
        print('Too high, try again')
        
    elif (num < num2):
        guess += 1
        print('Too low, try again')
        
    elif (num == num2):
        guess += 1
        print('Congrats! You guessed it!')
        print('Number of guesses:', guess)