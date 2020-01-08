"""
Programmer: Carsyn Leitch
Date: 12.20.19
Program: Guess My Number
"""


myNumber = 7

print('\nGuess a number between 1 & 10\n')

# Ask Users to Guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations, you guessed my number!!!\n")





"""
Programmer: Carsyn Leitch
Date: 12.20.19
Program: 1 - 10
"""

x = 1

# While Loop will see if a condition has been met
# If not is will run again until the condition
# Has been met

while x <= 10:
    print(x)
    x+=1