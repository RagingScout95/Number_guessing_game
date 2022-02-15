import os
import random
from os import system

system('cls')
print("\n================ Welcome to Number gussing game ================")

while True:
    upper_range = input("\nHey!! Type a number : ")

    if upper_range.isdigit():
        if int(upper_range) <=0:
            print("\nPlease type a number greater than 0 :/ ")
        else:
            break
    else:
        print("\nPlease type a number :/ ")
    
random_number = random.randint(0, int(upper_range))
print("\n----------------------------------------------------------------")
guesses = 0
while True:
    guesses +=1
    guess = input("\nGuess a number : ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print('\nPlease enter a number :/ ')
        # continue
    
    if guess == random_number:
        print("\n----------------------------------------------------------------")
        print("\nWow You got it!! :)")
        break
    else:
        if guess > random_number:
            print("\nYou were above the number!!")
        else:
            print("\nYou were below the number!!")

print("\nYou got it in", guesses, "guesses")
print("\nThx for playing :)\n")
