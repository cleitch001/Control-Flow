
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

for i in range(5):
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