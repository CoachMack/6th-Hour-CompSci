#Name: Coach Mack
#Class: 6th Hour
#Assignment: Lecture - Def Functions
import random

def hello_world():
    print("Hello World!")

hello_world()

def class_roster(name):
    print(name, "is in 6th hour.")

class_roster("Evan")

def subtraction(a, b):
    print(a - b)

subtraction(b = 1, a = 3)

def student_info(**student):
    print("This student's last name is " + student["lname"])
    print("He is a " + student["grade"])

student_info(fname = "Elijah", lname = "Raji", grade = "Senior", vidya = "Insurgency: Sandstorm")


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

    if replayInput == "Y":
        number_game()
    else:
        exit()

number_game()


