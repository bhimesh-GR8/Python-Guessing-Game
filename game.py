"""Core game logic for the Number Guessing Game."""

import random

# Handle negative integers too
def is_string_integer(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def play_game(low = 0, high = 100):
    """
    Start the number guessing game.
    
    Players try to guess a random number between 'low' and 'high'.
    They can quit at any time by entering 'q'.
    """
    print(" Welcome to the Number Guessing Game! ")
    name = input("Please enter your name: ")
    
    # Swap the values if low is bigger than high
    if (low > high):
        low, high = high, low

    while True:
        print(f"I am thinking of a number between {low} and {high}.")
        secret_number = random.randint(low, high)
        attempts = 0

        while True:
            guess = input("Enter your guess (or type 'q' to quit): ")

            if guess.lower() == 'q':
                print("You quit the game. The number was", secret_number)
                # If the player quits, then I don't think they'd like to play again
                return

            if not is_string_integer(guess):
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"Very Congratulations To {name}! You guessed the number in {attempts} attempts.")
                break

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"Thanks for playing {name}! We hope to see you again soon.")
            break


def main(low = 0, high = 100):
    """Entry point for the game."""
    play_game(low, high)


if __name__ == "__main__":
    main()
