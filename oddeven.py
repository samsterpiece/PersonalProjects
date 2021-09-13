#Small program that ask user for a number and tells them if odd or even


#Asks the user what number they would like to input
userInput = int(input("What number would you want to check?"))

#conditional statement that checks the number
if userInput % 2 == 0: 
    print("The number is even")
else:
    print("The number is odd")