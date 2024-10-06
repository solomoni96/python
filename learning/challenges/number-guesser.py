import sys
from random import choice

rounds = 0
player_wins = 0
numbers = range(1, 2)

def guess_the_number(name):
    global rounds, player_wins
    
    first_number = min(numbers)
    last_number = max(numbers)
    player_input = input(f"\n{name}, can you guess which of these number i'm thinking of between {first_number} and {last_number}?\n\n")
    
    # Error handling for non numeric value
    try:
        player_choice = int(player_input)
    except ValueError:
        print("\nPlease enter a valid number.")
        return guess_the_number(name)
        
    computer_choice = choice(numbers)
    
    print(f"\nYou chose {player_choice}. I was thinking of the number {computer_choice}\n")
    
    if player_choice == computer_choice:
        player_wins += 1
        print(f"🎉 You win this round, {name}!\n")
    else:
        print(f"👎 Sorry wrong number\n")

    rounds += 1
    
    print(f"Number of rounds: {rounds}")
    print(f"{name}'s correct guess: {player_wins}")
    print(f"Your winning percentage: {player_wins/rounds:.2%}\n")

    play_again = input("Try again?\nYes (Y) or No (N)...\n")
    
    if play_again.strip().upper() == "Y":
        return guess_the_number(name)
    else:
        sys.exit("\nThank you for playing. Bye! 👋")
    
# Start the game
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()
    print(f"Hello {args.name}! Lets play a guessing game...")
    guess_the_number(args.name)
