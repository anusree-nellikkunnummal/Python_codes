import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose something from list
    if '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user guessed

    lives = 10
    # getting user input
    while len(word_letters) > 0 and lives >0:
        # letter used
        # ''.join([a, b, c]) --> 'a b c'
        print(f'You have {lives} lives left and used these letters: ', ''.join(used_letters))

        # what current word is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word is: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('letter is not in word')
                lives = lives - 1


        elif user_letter in used_letters:
            print('You have already used that letter, please try another: ')
        else:
            print('Invalid guess, try a letter: ')

    if lives > 0:
        print(f'congrats!! it\'s {word}. You have guessed the word correctly. !!')  # gets here when word_length == 0 and lives > 0

    else:
        print('Oh sorry!! Lives = 0, you are dead!')  # at this time lives == 0


hangman()


