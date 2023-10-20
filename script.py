import art
import random

print("Welcome to the Number Guessing Game!")
random_num = random.choice(range(1, 101))
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

while difficulty != "easy" and difficulty != "hard":
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def play_game():
    lives = 0
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    guess = int(input("Make a guess: "))

    while lives > 0 and guess != random_num:
        if guess < random_num:
            lives -= 1
            print(
                f"Too low.\nGuess again.\nYou have {lives} remaining to guess the number")
        elif guess > random_num:
            lives -= 1
            print(
                f"Too high.\nGuess again.\nYou have {lives} remaining to guess the number")
        guess = int(input("Make a guess: "))

    if guess == random_num:
        print("Congratulations, you guess the number!")
    else:
        print(f"You lost, the number was {random_num}")


play_game()
