from random import randint
from art import logo

random_num = randint(1, 100)
easy_level_turns = 10
hard_level_turns = 5
is_game_over = False
print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a Number between 1 to  100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def difficulty():
    if level == "easy":
        return easy_level_turns
    elif level == "hard":
        return hard_level_turns


def guess_number(random_number):
    global easy_level_turns, hard_level_turns, is_game_over
    guess = int(input("Make a Guess:" ))
    # print(random_number)
    if guess > random_number:
        print("Too high!")
        if level == "easy":
            easy_level_turns -= 1
        elif level == "hard":
            hard_level_turns -= 1
        if easy_level_turns < 1 or hard_level_turns < 1:
            print("You have run out of guesses, you lose.")
            is_game_over = True
    elif guess < random_number:
        print("Too low!")
        easy_level_turns -= 1
        hard_level_turns -= 1
        if easy_level_turns < 1 or hard_level_turns < 1:
            print("You have run out of guesses, you lose.")
            is_game_over = True
    else:
        print(f"You got it the answer was {random_number}.")
        is_game_over = True


while not is_game_over:
    if level == "easy" or level == "hard":
        print(f"You have {difficulty()} attempts remaining to guess the number.")
        guess_number(random_num)
    else:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()