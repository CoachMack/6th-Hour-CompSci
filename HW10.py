#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print("Hello World!")

#2. Create a while loop that prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
j = 1
while j <= 30:
    if j % 2 == 0:
        print(j)
    j += 1

#3. Create a while loop that asks for a number input until the user
#inputs the number 0.

k = int(input("Enter Zero to Continue!"))
while k != 0:
    k = int(input("Wrong number! Enter Zero to Continue!"))