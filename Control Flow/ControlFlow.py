"""
Programmer: Carsyn Leitch
Date: 1.8.20
Program: Running total

This program asks users for five numbers
It then sums up the numbers
"""

sum = 0

for i in range(5):
    enter_a_number = input("enter a number: ")
    sum = sum +enter_a_number

print("\nSum of your number is: " + str(sum))