import random


def play():
    user_choice = input('r for rock, s for scissors, p for paper: ')
    computer_choice = random.choice(['r', 's', 'p'])

    if user_choice == computer_choice:
        return f"It's a tie. You both have chosen {user_choice}"
    if is_win(user_choice, computer_choice):
        return f"You win! You have chosen {user_choice}, your opponent - {computer_choice}"

    return f"You lose. You chose {user_choice}, your opponent - {computer_choice}"


def is_win(user, opponent):
    # r>s, s>p, p>r
    if user == 'r' and opponent == 's' or user == 's' and opponent == 'p' or user == 'p' and opponent == 'r':
        return True


print(play())
