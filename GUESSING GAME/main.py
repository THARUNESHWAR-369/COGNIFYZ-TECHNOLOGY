import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of guesses
num_guesses = 0

print("\n\n\tWelcome to the Guessing Game!")
print("\tI've selected a random number between 1 and 100.\n")

while True:
    try:
        # Get user input as an integer
        user_guess = int(input("Guess the number: "))
        num_guesses += 1

        # Check if the guess is correct
        if user_guess == random_number:
            print(f"\n\tCongratulations! You guessed the correct number {random_number} in {num_guesses} attempts.")
            break
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")

