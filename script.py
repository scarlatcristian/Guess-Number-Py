import art
import random

print("Welcome to the Number Guessing Game!")
random_num = random.randint(1, 100)


def select_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while difficulty not in ["easy", "hard"]:
        difficulty = input("Invalid input. Choose 'easy' or 'hard': ").lower()
    return 10 if difficulty == "easy" else 5


def play_game():
    lives = select_difficulty()
    print("Guess the number between 1 and 100")

    while lives > 0:
        guess = int(input("Make a guess: "))
        if guess < random_num:
            print(
                f"Too low.")
        elif guess > random_num:
            print(
                f"Too high.")
        else:
            print(f"Congratulation! You guess the number {random_num}!")
            return
        lives -= 1
        print(f"Guess again.\nYou have {lives} remaining to guess the number")

    print(f"Sorry you run out of lives, the number was {random_num}")


play_game()