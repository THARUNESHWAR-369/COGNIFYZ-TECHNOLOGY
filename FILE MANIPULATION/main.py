# Function to count word occurrences in a text file
def count_word_occurrences(file_path):
    word_counts = {}

    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            # Read the file line by line
            for line in file:
                # Split each line into words
                words = line.split()

                # Count the occurrences of each word
                for word in words:
                    # Remove punctuation and convert to lowercase
                    word = word.strip('.,!?():;"').lower()
                    
                    # Increment the count for the word
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

    return word_counts

# Function to display word counts in alphabetical order
def display_word_counts(word_counts):
    if word_counts:
        # Sort the word counts alphabetically by word
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[0])

        # Display the results
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")
    else:
        print("No word counts to display.")

# Get the file path from the user
file_path = input("Enter the path to the text file: ")

# Count word occurrences and display the results
word_counts = count_word_occurrences(file_path)
display_word_counts(word_counts)
