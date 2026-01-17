import random

print(" Welcome to the Number Guessing Game! ")

while True:
    print("I am thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or type 'q' to quit): ")

        if guess.lower() == 'q':
            print("You quit the game. The number was", secret_number)
            break

        if not guess.isdigit():
            print(" Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! ")
        break