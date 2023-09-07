import random

# Define the range for the random number
min_range = 1
max_range = 50

# Generate a random number within the specified range
random_number = random.randint(min_range, max_range)

print("\n\tWelcome to the Number Guesser Game!")
print(f"\tI've selected a random number between {min_range} and {max_range}.\n")

while True:
    try:
        # Get user input as an integer
        user_guess = int(input("Guess the number: "))

        # Check if the guess is within the valid range
        if user_guess < min_range or user_guess > max_range:
            print(f"Please enter a number between {min_range} and {max_range}.")
            continue

        # Check if the guess is correct
        if user_guess == random_number:
            print(f"\nCongratulations! You guessed the correct number {random_number}.")
            break
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")
