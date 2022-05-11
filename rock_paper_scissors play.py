import random

def play():
    user = input("What's your choice 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r', 'p', 's'])
    print(f"computer's guess : {computer}")

    # r>s, p>r, s>p
    if user == computer:
        print("it's a tie")

    elif is_win(user, computer):
        print('You won!')

    else:
        print('You lost')

def is_win(player, opponent):
    # return True if player wins
    # r>s, p>r, s>p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or \
            (player == 's' and opponent == 'p'):
        return True

play()








