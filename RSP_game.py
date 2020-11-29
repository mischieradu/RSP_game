import logging
from random import randint
import pprint

my_log = logging.getLogger()
my_log.setLevel(logging.WARNING)
file_handler = logging.FileHandler('logger_RSP_5.log', mode="a")
file_handler.setFormatter(logging.Formatter(" %(asctime)s  - %(message)s"))  # [%(levelname)s]
my_log.addHandler(file_handler)

with open("RSP_rules", "r") as f:
    data = f.readlines()

data2 = [ln.replace('\n', '') for ln in data]

dict_rules = {}


def print_rules():
    # data2 = [ln.replace('\n', '') for ln in data]
    for i, ln in enumerate(data2):
        dict_rules[i + 1] = ln
    print('\n')
    print("Rules of interaction the 5 elements are: ")
    for no, rule in dict_rules.items():
        print(f'{no}: {rule}')
    print('\n')


print_rules()

options = []
win_dict = {}


def option_rules():
    for rule in data2:
        win_one = rule.split(' ')[0].lower()
        lose_one = rule.split(' ')[-1].lower()

        if win_one not in options:
            options.append(win_one)

        if (win_one, lose_one) not in win_dict.keys():
            win_dict[(win_one, lose_one)] = rule

    return options, win_dict


def play_game():
    while 42:
        try:
            choice = input('Choose here: ').lower()
            opponent = option_rules()[0][randint(0, 4)]
            assert choice in [line.split()[0] for line in data]
            if choice == opponent:
                print('Tie!')
                my_log.warning(f"Tie!")
            else:
                if (choice, opponent) in win_dict.keys():
                    winner = choice
                    winning_rule = win_dict[(choice, opponent)]
                    print(f'You win! {winning_rule}!')
                    my_log.warning(f"You win! {winning_rule}")
                else:
                    winner = opponent
                    winning_rule = win_dict[(opponent, choice)]
                    print(f'You lose! {winning_rule}!')
                    my_log.warning(f"You lose! {winning_rule}")

            again = 42
            while again:
                again = input("Play again?").lower()
                if again == "yes":
                    break
                if again != "yes" and again != "no":
                    print("must insert yes or no")
                if again == "no":
                    print("bye!")
                    break

        except (AssertionError, ValueError):
            print('Please choose on of the options above!')


play_game()