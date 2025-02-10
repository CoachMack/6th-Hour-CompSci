#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers.
def average(a,b,c):
    print((a + b + c)/3)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animals):
    print("The 3rd animal in the list is:", animals[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def counting(x):
    for i in range(1, x + 1):
        print(i)
#5. Call all of the functions created in 1 - 4 with relevant arguments.