#!/usr/bin/python3

# game.py

import random


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the Rock, Paper, Scissors game.

    Args:
        user_choice (str): The user's choice (rock, paper, or scissors).
        computer_choice (str): The computer's choice (rock, paper, or scissors)

    Returns:
        str: A message indicating the result of the game (win, lose, or tie).
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """
    Play a round of Rock, Paper Scissors game.

    Genetes a random choice for the computer and determines the winner based on their choices.
    """
    user_score = 0
    computer_score = 0

    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose your weapon: rock, paper, or scissors.")
        user_choice = input("Your choice: ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Ivalid choice! Please choose again.")
            continue
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nYou score: {user_score}")
        print(f"Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break
