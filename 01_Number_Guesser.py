import math
import random

print("Hello! Welcome to Number guesser game!\n")
print("\n")
print("You will have to guess the number the computer generates in 10 tries\n")
print("\n")
print("You can give the lower and upper limit which you want the computer to use for the game")
# Selecting Range of guessing

ll = int(input("Enter the lower limit\n"))
ul = int(input("Enter the upper limit\n"))

# Generating a random number and printing the challenge for 

x = random.randint(ll, ul)

print("you will be guessing a number between", ll, "and", ul, "\n")

# Logic building

for i in range(1, 11):
    guess = int(input("Enter your guess\n"))
    if guess == x:
        print("Congratulations! You guessed the number correctly!\n")
        print("Your guess number = ", i)
        break
    elif guess > x and guess <= ul and guess >= ll:
        print("You guessed a little too high!\n")
    elif guess < x and guess <= ul and guess >= ll:
        print("you guessed a little too low!\n")
    else:
        print("Please stick to the game parameters of the game\n")
        print("As a penalty, one guess will be used up\n")

if guess != x:
    print("Better Luck Next Time!\n")