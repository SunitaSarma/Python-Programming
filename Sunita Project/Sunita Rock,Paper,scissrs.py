# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:02:32 2024

@author: sarma
"""

import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock-Paper-Scissors!")
    
    play_again = 'yes'
    while play_again.lower() == 'yes':
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()
        
        if user_choice in choices:
            computer_choice = random.choice(choices)
            print("Computer's choice:", computer_choice)
            
            result = determine_winner(user_choice, computer_choice)
            print(result)
            
            if result == "You win!":
                user_score += 1
            elif result == "You lose!":
                computer_score += 1
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")
        
        print("\nScores - You:", user_score, "Computer:", computer_score)
        play_again = input("Do you want to play again? (yes/no): ")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()