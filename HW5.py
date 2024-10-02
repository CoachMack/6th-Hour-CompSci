#Name:
#Class: 6th Hour
#Assignment: HW5

import random
#1. Print "Hello World!"
print("Hello World!")
#2. Create a list that contains 3 integers
numList = [random.randint(1,1000), random.randint(1,1000), random.randint(1,1000)]
print(numList)
#3. Create an if statement that prints out whichever of the three numbers is the highest
if numList[0] > numList[1] and numList[0] > numList[2]:
    print("The first number is the biggest number")
elif numList[1] > numList[0] and numList[1] > numList[2]:
    print("The second number is the biggest number")
elif numList[2] > numList[0] and numList[2] > numList[1]:
    print("The third number is the biggest number")
else:
    print("There is no biggest number.")

print(max(numList), "is the biggest number.")