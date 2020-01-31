
# Date: 2.3.20
# Programmer: Carsyn Leitch

# Declare Global Variables Here

# name = input("\nwhat is your name: ")
x = 15


# Create Functions Here....

# Greeting Function
def greeting(): 
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)

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

# Call Functions Here.....

#greeting()
#printSomething()
#print(x)
#printNumber(28)
#printNumber(38)
printTwoNumbers(23,78)
printTwoNumbers(45)