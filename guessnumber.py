#program that limits the user to 5 guesses
#guess the number computer gives
#incomplete
import random


def guessNumber():
    #gives a random number between 0 to 100
    randnumber = random.randint(0,100)

    #stores the number of guesses user has
    numGuesses = 0
    playGame = True

    while playGame == True:
        while numGuesses <= 5:
            userGuess = int(input("What is your guess?"))
            if userGuess < randnumber:
                print("Guess is too low!")
                numGuesses += 1
            elif userGuess > randnumber:
                print("Guess is too high!")
                numGuesses += 1
            elif userGuess == randnumber:
                print("You guessed the right number! Number is: ", randnumber)
            elif numGuesses == 5:
                retryGame = input("You ran out of guesses. Try again?")


#When user run out of guesses
guessNumber()
retryGame = input("You ran out of guesses. Try again?")
if retryGame == "y" or "yes":
    guessNumber()
elif retryGame == "no" or "n":
    exit()


