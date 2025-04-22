# Avery rock,paper,scissors

import random

# Track scores
user_score = 0
computer_score = 0

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Game loop
while True:
    user_choice = input("Enter rock, paper, scissors, or 'quit' to exit: ").lower()

    # Check if the user wants to quit
    if user_choice == "quit":
        print("Thanks for playing!")
        print(f"Final Score - You: {user_score} | Computer: {computer_score}")
        break

    # Validate user input
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display current score
    print(f"Score - You: {user_score} | Computer: {computer_score}")