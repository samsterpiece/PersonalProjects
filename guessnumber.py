#program that limits the user to 5 guesses
#guess the number computer gives
#incomplete
import random

def tryAgain():
    retryGame = input("You ran out of guesses. Try again?")
    if retryGame == "yes" or "y":
        guessNumber()
    elif retryGame == "no" or "n":
        exit

def winGame():
    winGame = input("You won the game. Try again?")
    if winGame == "y" or "yes":
            guessNumber()
    elif winGame == "no" or "n":
            exit()


def guessNumber():
        #gives a random number between 0 to 100
        randnumber = random.randint(0,100)

        #stores the number of guesses user has
        numGuesses = 4
        while numGuesses <= 4 and numGuesses >= 0:
            userGuess = int(input("What is your guess?"))
            if userGuess < randnumber:
                print("Guess is too low!")
                print("# Guesses left: " , numGuesses)
                numGuesses -= 1
            elif userGuess > randnumber:
                print("Guess is too high!")
                print("# Guesses left: " , numGuesses)
                numGuesses -= 1
            elif userGuess == randnumber:
                print("You guessed the right number! Number is: ", randnumber)
                winGame()
        else:
                print("Number was: ", randnumber)
                tryAgain()
guessNumber()