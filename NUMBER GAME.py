import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the player's guess
        guess = input("Enter your guess: ")

        # Ensure the input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
number_guessing_game()
