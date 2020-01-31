
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

# Call Functions Here.....

#greeting()
#printSomething()
#print(x)
printNumber(28)
printNumber(38)