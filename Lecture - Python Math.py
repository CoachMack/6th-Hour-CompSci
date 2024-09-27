#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Python Math

#This is a library import. We will touch more on these later.
import math

#Here is how you handle some of the mathematical operations within Python.

#Addition
add = 2 + 2

#Subtraction
subtract = 4 - 2

#Multiplication
multiply = 2 * 2

#Division
divide = 2 / 2

#Exponent
exp = 2 ** 2

#Square Root
sq = math.sqrt(4)

#Rounding

#Round rounds up or down, same as you would in math.
round = round(3.14)

#Ceiling, or ceil, always rounds up
roundUp = math.ceil(3.14)

#Floor always rounds down
roundDown = math.floor(3.14)

#You can ask the user to imput their own numbers.
#This is a way to do math through user input.
x = int(input("Please Enter First Number: "))
y = int(input("Please Enter Second Number: "))
z = x + y

print(z)

