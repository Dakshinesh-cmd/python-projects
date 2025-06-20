import random

def play_game():
    print("🎲 Welcome to the Number Guessing Game!")
    print("Choose difficulty: Easy (10 attempts) or Hard (5 attempts)")
    difficulty = input("Enter 'easy' or 'hard': ").lower()
    
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    number_to_guess = random.randint(1, 100)
    guess = None
    tries = 0

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess == number_to_guess:
            print(f"🎉 Correct! You guessed the number in {tries} attempts.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        attempts -= 1
        if attempts == 0:
            print(f"😞 You're out of attempts. The number was {number_to_guess}.")
        else:
            print(f"Attempts left: {attempts}")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again == "yes":
        play_game()
    else:
        print("Thanks for playing! 👋")


