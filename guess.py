#!/usr/bin/env python
import random

number = random.randint(1, 100)
print("Welcome to Guess the Number")
print("===========================")
print("I've thought of a number between 1 to 100. Try to guess it in as few tries as possible.")
print(number)

guess = int(input("Your guess:\t"))
while(guess != number):
    guess = int(input("Guess again:\t"))

print("Congratulations! You guessed it right. The number is {}".format(number))
print("================")
print("Have a nice day!")
print("================")
