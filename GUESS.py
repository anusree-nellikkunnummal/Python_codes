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

guess(10)