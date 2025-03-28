import random
def valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            return 'Enter a valid number'
min_value=valid_number("enter a minimum number")
max_value=valid_number("enter a max number")
#print(min_value)
#print(max_value)
def play_game():
    while True:
        min_value = valid_number("enter a minimum number")
        max_value = valid_number("enter a max number")
        if min_value>=max_value:
            print("Enter a minimum number in min_value")
        else:
            break
    target_number=random.randint(min_value,max_value)
    attempts = 0

    print(f"\nI've generated a number between {min_value} and {max_value}. Let's start guessing!")

# Main guessing loop
    while True:
        guess = valid_number("Enter your guess: ")
        attempts += 1

    # Check if guess is within the specified range
        if guess < min_value or guess > max_value:
            print(f"Please enter a number between {min_value} and {max_value}.")
            continue

    # Provide feedback
        if guess < target_number:
            print("Too low! Try a higher number.")
        elif guess > target_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {target_number}!")
            print(f"It took you {attempts} attempts.")
            break

# Ask to play again
    while True:
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'.")

    if play_again == "yes":
        print("\nStarting a new game...\n")
        play_game()  # Restart the game
    else:
        print("Thanks for playing! Goodbye!")


# Start the game
play_game()