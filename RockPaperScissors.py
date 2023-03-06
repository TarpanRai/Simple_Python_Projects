# Simple Rock-Paper-Scissors game.

import random

print('Welcome to Rock-Paper-Scissors')
# Choices
options = ["rock", "paper", "scissors"]
# Score
wins, losses, ties = 0, 0, 0

while True:
    user_input = input("Type rock, paper or scissors: ").lower()

    # Invalid inputs
    if user_input not in options:
        print("Invalid input. Type rock, paper or scissors only!")
        continue

    # Computer choice
    computer_input = random.choice(options)
    print("Computer chooses", computer_input)

    # Check who won and adds score
    if user_input == computer_input:
        print("Its a tie")
        ties += 1
    elif user_input == "rock":
        if computer_input == "paper":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif user_input == "paper":
        if computer_input == "scissors":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1
    elif user_input == "scissors":
        if computer_input == "rock":
            print("You lose!")
            losses += 1
        else:
            print("You win!")
            wins += 1

    # Print score of player
    print("Wins:", wins, "Losses:", losses, "Ties:", ties)

    # Prompt to play again
    play_again = input("Play again? (y/n) ").lower()
    if play_again != "y":
        break

print("Good Bye")
