#Miguel Davis
#11/23/2024
#P5HW
#Math Quiz

import random

def display_menu():
    print("\nWelcome to the math quiz")
    print("Main Menu")
    print("-----------------")
    print("1. Adding random numbers")
    print("2. Subtracting random numbers")
    print("3. Exit")
    print("\nPlease choose one of the menu options:")

def get_random_numbers():
    return random.randint(0, 999), random.randint(0, 999)

def addition_quiz():
    num1, num2 = get_random_numbers()
    correct_answer = num1 + num2
    guesses = 0
    
    print(f"\nWhat is {num1} + {num2}?")
    
    while True:
        try:
            guess = int(input("Enter your answer: "))
            guesses += 1
            
            if guess == correct_answer:
                print(f"\nCongratulations! That's correct!")
                print(f"Number of guesses: {guesses} {'guess' if guesses == 1 else 'guesses'}")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid number.")

def subtraction_quiz():
    num1, num2 = get_random_numbers()
    correct_answer = num1 - num2
    guesses = 0
    
    print(f"\nWhat is {num1} - {num2}?")
    
    while True:
        try:
            guess = int(input("Enter your answer: "))
            guesses += 1
            
            if guess == correct_answer:
                print(f"\nCongratulations! That's correct!")
                print(f"Number of guesses: {guesses} {'guess' if guesses == 1 else 'guesses'}")
                break
            elif guess < correct_answer:
                print("Sorry, guess is too low.")
            else:
                print("Sorry, guess is too high.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input()
        
        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("\nThank you for playing... Bye!!")
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()