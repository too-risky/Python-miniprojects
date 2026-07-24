#Random numbers 

import random

low = 1
high = 100
ans = random.randint(low, high)
guesses = 0


print("Welcome to number guessing game")
print(f"Select a number between {low} to {high}")

while True :
    guess = input("Guess a number : ")

    if guess.isdigit() :
        guess = int(guess)
        guesses += 1

        if guess < low or guess > high :
            print("Invalid Guess")
            print(f"Select a number between {low} to {high}")
            guess = input("Guess a number : ")

        elif guess < ans :
            print("Too low, try again")

        elif guess > ans :
            print("Too high, try again")

        else :
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break

    else :
        print("Invalid Guess")
        print(f"Select a number between {low} to {high}")
        guess = input("Guess a number : ")
        