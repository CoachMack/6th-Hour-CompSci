#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW13
import random

#1. Create a list containing 10 integers of your choice.
numList = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),]
#2. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
print(numList)
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
for i in numList:
    if i % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
# Print the total count of even and odd numbers.
print(f"The number of even numbers is {evenNumbers} and the number of odd numbers is {oddNumbers}")