
name = input("\nwhat is your name: ")

# Greeting Function
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)

print("\nGreetings Function\n")
greeting()

#Programmer: Carsyn Leitch
#Date: 12.20.19
#Program: Guess My Number




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



#Programmer: Carsyn Leitch
#Date: 12.20.19
#Program: 1 - 10


x = 1

# While Loop will see if a condition has been met
# If not is will run again until the condition
# Has been met

while x <= 10:
    print(x)
    x+=1


#Programmer: Carsyn Leitch
#Date: 1.23.20
#Program: While Loop Nested Inside a For Loop


for i in range(4):
    print("For Loop: " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        x = x - 1

#Programmer: Carsyn Leitch
#Date: 1.8.20
#Program: Running total

#This program asks users for five numbers
#It then sums up the numbers


sum = 0
how_many_numbers = int(input("\nHow many numbers would you like to sum up: "))
print("")

for i in range(how_many_numbers):
    enter_a_number = int(input("\nEnter a Number: "))
    sum = sum +enter_a_number

print("\nSum of your number is: " + str(sum))

#Programmer: Carsyn Leitch
#Date: 1.20.20
#Program: Double For Loop

for i in range(3):
    print("Outer For Loop" + str(i))
    for k in range(4):
        print("\tInner For Loop" + str(k))

#Programmer: Carsyn Leitch
#Date: 1.8.20
#Program:Average Test Scores

#This program asks users how many tests they wish to average


total = 0 
how_many_tests = int(input("How many tests would you like to average: "))
print("")

for i in range(how_many_tests): 
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score
average = total / how_many_tests

print("\nAverage: " + str(round(average, 2)))





print("\n*******************************\n")

# Date: 2.3.20
# Programmer: Carsyn Leitch

# Declare Global Variables Here


x = 15


# Create Functions Here....



# Functions & Local Variable x
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): #function name = printNumber with a PARAMETER of age
    print(age)

# Default Parameter Values
def printTwoNumbers(x, y = 71):
    print("First Parameter(Number): " + str(x))
    print("Second Parameter(Number): " + str(y))

# Print Sum
def printSum(x,y):
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

# Call Functions Here.....


print("\nPrint Something Function\n")
printSomething()
# print(x)
print("\nPrint Number Function\n")
printNumber(28)
printNumber(38)
print("\nPrint Two Numbers Function\n")
printTwoNumbers(23,78)
printTwoNumbers(45)
print("\nPrint Sum Function\n")
printSum(36,29)
print("\nPrint Multiple Times Function\n")
printMultipleTimes("I love Computer Science", 13)

