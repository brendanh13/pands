# This is Week 4 - Lab 2

# User keeps guessin a number until they choose the correct number

# Author: Brendan Heeney

numberToGuess = 13

guess = int(input("please guess a number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else:
        print("too high")
    # print("wrong")
    guess = int(input("please guess again: "))

print ("Well done! Yes the number was", numberToGuess)
