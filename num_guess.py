# Name: Edgar Valerio
# GiftHub Username: Valerioe1
# Date: 10/16/24
# Description: by inputting an integer you will have to guess that integer and once you get it right it will list how many attempts you took.

integer = int(input("Enter the integer for the player to guess."))
attempts = 0
guess = int(input("Enter your guess."))
if guess == integer:
    attempts += 1
    print("You guessed it in " + str(attempts) + " try.")
else: attempts += 1

while guess != integer:
    attempts += 1
    if guess > integer: guess = int(input("Too high - try again:"))
    elif guess < integer: guess = int(input("Too low - try again:"))
    if guess == integer: print("You guessed it in " + str(attempts) + " tries.")
