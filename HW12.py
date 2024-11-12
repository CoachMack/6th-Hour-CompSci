#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW12

#1. Create a for loop with variable i that counts down from 5 to 1
#and then prints "Hello World!" at the end.
for i in range (5, 0, -1):
    print(i)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers
#between 1 and 30.
#(HINT: Look back to HW6 on how to see if a number is divisible by another)
for j in range(1, 31):
    if j % 2 == 0:
        print(j)
#3. Create a for loop that prints 5 different animals from a list.
animals = ["Joe Bradley", "Dog", "Cat", "Whale", "Flamingo"]

for k in animals:
    print(k)
#4. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for z in input("Give me a word: ")[::-1]:
    print(z)