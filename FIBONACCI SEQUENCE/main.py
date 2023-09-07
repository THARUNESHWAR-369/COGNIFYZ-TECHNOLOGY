def generate_fibonacci_sequence(n):
    fibonacci_sequence = []
    
    if n <= 0:
        return fibonacci_sequence

    # Initialize the first two terms of the sequence
    a, b = 0, 1

    # Add the first term to the sequence
    fibonacci_sequence.append(a)

    # Generate the Fibonacci sequence up to the nth term
    for _ in range(1, n):
        # Calculate the next term
        a, b = b, a + b
        # Add it to the sequence
        fibonacci_sequence.append(a)

    return fibonacci_sequence

# Get the number of terms from the user
try:
    num_terms = int(input("\nEnter the number of Fibonacci terms to generate: "))
    if num_terms < 0:
        print("Please enter a non-negative integer.")
    else:
        # Generate and print the Fibonacci sequence
        result = generate_fibonacci_sequence(num_terms)
        if result:
            print("\nFibonacci Sequence: ", end='')
            print(result)
        else:
            print("No terms to generate for n = 0.")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
