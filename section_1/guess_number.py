import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high)
chances = 100
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {guess_counter} attempts.')
        break

    elif guess_counter >= chances and guess != num:
        print(f'sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')