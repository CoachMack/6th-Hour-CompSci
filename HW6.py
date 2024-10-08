#Name:
#Class: 5th Hour
#Assignment: HW6


#Objectives

#1. Print Hello World!
print("Hello World!")
#2. Create a variable named num and assign it a number.
num = 36
#3. Create a nested if statement follows this structure:


if num % 2 == 0: #If num is divisible by 2
    if num % 3 == 0: #if num is divisible by 3
        print(num / 2) #print the result of num being divided by 2
        print(num / 3) #print the result of num being divided by 3
    else: #else
        print("Number not divisible by 3") #print that it is not divisible by 3
        print(num / 2) #print the result of num being divided by 2
else: #else
    if num % 3 == 0: #if num is divisible by 3
        print("Number not divisible by 2") #print that num is not divisible by 2
        print(num / 3) #print the result of num being divided by 3
    else: #else
        print("Number not divisible by 2 or 3.") #print that neither is divisible by 2 or 3
