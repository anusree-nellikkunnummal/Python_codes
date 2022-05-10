#Guess a number from a random number (use randint function part of the random module)
import random
#define a function taking input 'x' and use while loop until condition is met

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print(f'Sorry, guess again. {guess} is too low.')
        elif guess > random_number:
            print(f'Sorry, guess again. {guess} is too high')
    print(f'Yay congrats!! You have guessed the number. It is {random_number}')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  #could also be high as low = high
        feedback = input(f'is {guess} too high (H), too low (L), or correct (C) ?? :')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('Yay !! the computer guessed your number correctly ')

computer_guess(200)
guess(50)