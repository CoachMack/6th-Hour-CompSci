#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Def Functions
import random

#This is a def function. These are custom functions designed to "segment" and organize your code in
#Python! You can also use them to reuse the same code but with different sets of data (called "arguments")
#in a way that doesn't require copying and pasting said same code over and over again.
def hello_world():
    print("Hello World!")

#This is how you "call" a function.
hello_world()

#You can place variables to be used for arguments inside of where the def function is created.
#This allows you to assign a value to a variable using an argument and so it will use that data
#wherever that variable is used inside of the function.
def class_roster(name):
    print(name, "is in 5th hour.")

#In this case, we put the value "Evan" as our argument and so it set the name variable to = "Evan".
#So as it is written, it will print out "Evan is in 5th hour."
    print(name, "is in 6th hour.")

class_roster("Evan")

#You can make multiple variables and assign multiple arguments to each one. When written on
#their own, arguments are assigned in order, so the first number in the argument would be assigned to
#a and the second to b.
def subtraction(a, b):
    print(a - b)

#However, you can do what are called "positional arguments" and assign them specfically like in the
#call below.
subtraction(b = 1, a = 3)

#Using a single asterisk in front of the variable, you can turn all of your arguments into a list,
#and pull their values like you would a normal list.
def student_list(*student):
    print("The 2nd student's name is", student[1])

student_list("Ryan", "Seeley", "Jax")

#You can also do the same thing and make it a dictionary by using two asterisks in front of the variable.
def student_info(**student):
    print("This student's last name is " + student["lname"])
    print("He is a " + student["grade"])

#Just be sure to give every value a keyword in front of it like you would with a dictionary.
student_info(fname = "Elijah", lname = "Raji", grade = "Senior", vidya = "Insurgency: Sandstorm")

#This is a quick and dirty example of how you can use def functions to repeat specific kinds of code.
def number_game():
    playerNum = int(input("Enter Number Between 1 and 10"))
    opponentNum = random.randint(1,10)

    print("Opponent got ", opponentNum)
    if playerNum > opponentNum:
        print("You win!")
    elif playerNum < opponentNum:
        print("You lose!")
    else:
        print("Tie!")

    replayInput = input("Would like to play again? Y/N")

    #Note here how you can call the function inside of itself to repeat the code.
    if replayInput == "Y":
        number_game()
    else:
        exit()

number_game()


#You can also change variables outside of the def function using the "global" command. By establishing
#the variable outside the function and then "calling" it inside, you can change the variable in any way
#you want and it will change the value outside of the function too. This is a good way to "count"
#results inside of the def function.
x = 0

def make_x_1():
    # This is how you call the variable and make it global.
    global x
    x = 1

def print_new_x():
    print(x)

#If you don't call any function that changes the variable globally, any other function that
#uses the variable will use its original value, NOT the changed value.
make_x_1()
print_new_x()


