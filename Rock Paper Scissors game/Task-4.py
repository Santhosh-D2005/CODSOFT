import random

def get_user_choice():
    while True:
        print("\n Choose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        try:
            choice = int(input("Enter the number of your choice(1-3):"))

            if choice == 1:
                return "rock"
            elif choice == 2:
                return "paper"
            elif choice == 3:
                return "scissors"
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Enter a valid number.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 0
    
    if(
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return 1
    
    return -1

def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        user_choice = get_user_choice()  # User choosing
        computer_choice = get_computer_choice()  # Computer choosing

        # Choices viewed
        print(f"\n You chose: {user_choice}")
        print(f"\n Computer chose: {computer_choice}")

        # Round winner
        result = determine_winner(user_choice, computer_choice)

        # Updating scores and result viewing
        if result == 1:
            print("You won this round")
            user_score += 1
        elif result == -1:
            print("Computer won this round")
            computer_score += 1
        else:
            print("It's a tie")

        rounds_played += 1  # Update rounds
        print(f"\nScore - You: {user_score} | Computer: {computer_score}")  # Viewing scores

        play_again = input("\n Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\n ---GAME OVER---")  # Final 
    print(f"Total Rounds Played: {rounds_played}")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

    # Final winner
    if user_score > computer_score:
        print("Lucky you won the game!!")
    elif user_score < computer_score:
        print("HAHA!...You lost")
    else:
        print("It's a draw!")
    
    print("GOOD GAME MATE!")    

if __name__ == "__main__":
    print("WELCOME TO ROCK PAPER SCISSORS GAME!!")
    play_game()
