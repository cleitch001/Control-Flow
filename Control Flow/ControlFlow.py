
# Date: 2.3.20
# Programmer: Carsyn Leitch

# Declare Global Variables Here

 name = input("\nwhat is your name: ")
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

# Print Sum
def printSum(x,y):
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

# Call Functions Here.....

print("\nGreetings Function\n")
greeting()
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