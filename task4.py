import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to make your choice.")
    print("Type 'quit' to exit the game.\n")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Your choice (rock, paper, scissors): ").lower()

        
        if user_choice == "quit":
            print("\nThanks for playing!")
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            break

        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
            continue

        
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("You lose this round.")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer\n")

play_game()