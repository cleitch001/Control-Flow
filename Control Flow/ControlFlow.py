
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